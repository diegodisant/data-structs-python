from structs.graph.node import GraphNode
from structs.graph.operations import GraphInterface

class Graph(GraphInterface):
  tag_map: dict[str, GraphNode]

  def add(tag: str, data: GraphData) -> None:
    pass

  def rel(tag: str, ref_tags: list[str]) -> None:
    pass

  def traverse(tags: list[str]) -> None:
    pass
