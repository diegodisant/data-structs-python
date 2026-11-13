import pytest

from tests.profiler import profile_test

from structs.graph import Graph, GraphData, CyclicNodeRefError, TagNotFoundError, RouteNotFoundError

def build_graph_data(lat: float, lon: float, address: str) -> GraphData:
  graph_data = {
    "lat": lat,
    "lon": lon,
    "address": address,
  }

  data = GraphData(**graph_data)

  return data

def test_add() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))
  graph.add('B', build_graph_data(1, 1, 'Address B'))
  graph.add('C', build_graph_data(2, 2, 'Address C'))

  expected_tags = ['A', 'B', 'C']
  graph_tags = list(graph.tag_map.keys())

  assert graph_tags == expected_tags

@profile_test
def test_add_1m() -> None:
  graph = Graph()
  gen_limit = 10**6
  current_tag = 'R'

  for number in range(gen_limit):
    current_tag = f'R{number}'

    graph.add(
      current_tag,
      build_graph_data(
        number,
        number,
        f'Address {current_tag}',
      ),
    )

  assert len(graph.tag_map) == gen_limit

def test_rel_cyclic() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))
  graph.add('B', build_graph_data(1, 1, 'Address B'))
  graph.add('C', build_graph_data(2, 2, 'Address C'))

  with pytest.raises(CyclicNodeRefError):
    graph.rel('A', ['A'])

def test_rel_tag_not_found() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))

  with pytest.raises(TagNotFoundError):
    graph.rel('A', ['B'])

def test_rel_unexistent_ref_tags() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))
  graph.add('B', build_graph_data(1, 1, 'Address B'))
  graph.add('C', build_graph_data(2, 2, 'Address C'))

  with pytest.raises(TagNotFoundError):
    graph.rel('A', ['B', 'C', 'D'])

def test_rel() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))
  graph.add('B', build_graph_data(1, 1, 'Address B'))
  graph.add('C', build_graph_data(2, 2, 'Address C'))

  graph.rel('A', ['B', 'C'])

  node_a = graph.tag_map['A']
  related_nodes = node_a.refs

  related_tags = list(related_nodes.keys())
  expected_tags = ['B', 'C']

  assert related_tags == expected_tags

def test_traverse_unexistent_ref_tags() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))
  graph.add('B', build_graph_data(1, 1, 'Address B'))
  graph.add('C', build_graph_data(2, 2, 'Address C'))

  with pytest.raises(TagNotFoundError):
    graph.traverse(['A', 'B', 'C', 'D'])


def test_traverse_route_not_found() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))
  graph.add('B', build_graph_data(1, 1, 'Address B'))
  graph.add('C', build_graph_data(2, 2, 'Address C'))
  graph.add('D', build_graph_data(3, 3, 'Address C'))

  graph.rel('A', ['B'])
  graph.rel('B', ['C'])

  with pytest.raises(RouteNotFoundError):
    graph.traverse(['A', 'B', 'C', 'D'])


# TODO: fix algo
def test_traverse() -> None:
  graph = Graph()

  graph.add('A', build_graph_data(0, 0, 'Address A'))
  graph.add('B', build_graph_data(1, 1, 'Address B'))
  graph.add('C', build_graph_data(2, 2, 'Address C'))
  graph.add('D', build_graph_data(3, 3, 'Address D'))
  graph.add('E', build_graph_data(4, 4, 'Address E'))
  graph.add('F', build_graph_data(5, 5, 'Address F'))

  graph.rel('A', ['B', 'C', 'D', 'F'])
  graph.rel('B', ['C'])
  graph.rel('C', ['D', 'F'])
  graph.rel('F', ['D', 'E'])
  graph.rel('D', ['E'])

  graph.traverse(['B', 'E'])
