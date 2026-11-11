from abc import ABC, abstractmethod

from structs.graph.node import GraphData

class GraphInterface(ABC):
  @abstractmethod
  def add(tag: str, data: GraphData) -> None:
    pass

  @abstractmethod
  def rel(tag: str, ref_tags: list[str]) -> None:
    pass

  @abstractmethod
  def traverse(tags: list[str]) -> None:
    pass
