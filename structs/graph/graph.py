from structs.graph.node import GraphNode, GraphData, GraphLinkData
from structs.graph.operations import GraphInterface
from structs.graph.error import CyclicNodeRefError, TagNotFoundError, RouteNotFoundError

class Graph(GraphInterface):
  tag_map: dict[str, GraphNode] = {}

  def add(self, tag: str, data: GraphData) -> None:
    # print(f'Add node: {tag}')
    # print(f'with data: {data}')

    node = GraphNode(tag, data)

    self.tag_map[tag] = node

  def get_unexistent_tags(self, tags: list[str]) -> list[str]:
    tags_set = set(tags)
    mapped_tags_set = set(self.tag_map.keys())

    unexistent_tags = tags_set - mapped_tags_set

    return list(unexistent_tags)

  def rel(self, tag: str, ref_tags: list[str]) -> None:
    print(f'Relate node: {tag} to nodes: {ref_tags}')

    if tag in ref_tags:
      raise CyclicNodeRefError(tag, 'rel')

    at_node = self.tag_map.get(tag)

    if at_node is None:
      raise TagNotFoundError(tag, 'rel')

    unexistent_tags = self.get_unexistent_tags(ref_tags)
    unexistent_tags_size = len(unexistent_tags)

    if unexistent_tags_size > 0:
      raise TagNotFoundError(f'with unexistent tags {unexistent_tags}', 'rel')

    for ref_tag in ref_tags:
      to_node = self.tag_map[ref_tag]

      link_data = GraphLinkData(
        at_node.data,
        to_node.data,
        tag,
        ref_tag,
      )

      at_node.refs[to_node.tag] = link_data

  def traverse(self, tags: list[str]) -> None:
    print(f'Traversing with following route: {' -> '.join(tags)}')

    unexistent_tags = self.get_unexistent_tags(tags)
    unexistent_tags_size = len(unexistent_tags)

    if unexistent_tags_size > 0:
      raise TagNotFoundError(f'with unexistent tags {unexistent_tags}', 'rel')

    while len(tags) > 1:
      at_tag = tags[0]
      to_tag = tags[1]

      at_node = self.tag_map[at_tag]
      link = at_node.refs.get(to_tag)

      if link is None:
        raise RouteNotFoundError(f'{at_tag} -> {to_tag}', 'rel')

      to_node = self.tag_map[to_tag]

      print(f'[traverse] Connecting routes: {link.route}')
      print(f'[traverse] visited: {at_tag}')
      print(f'[traverse] distance: {link.distance}')
      print(f'[traverse] from: {at_node.data}')
      print(f'[traverse] to: {to_node.data}')

      tags.pop(0)

  # TODO: implement route(at_tag, to_tag) find the possible route between two tags
  # raises RouteNotFound when cannot find the route
