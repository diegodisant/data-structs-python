from abc import ABC, abstractmethod

from structs.graph.node import GraphData

class GraphInterface(ABC):
  @abstractmethod
  def add(self, tag: str, data: GraphData) -> None:
    pass

  @abstractmethod
  def rel(self, tag: str, ref_tags: list[str]) -> None:
    pass

  @abstractmethod
  def traverse(self, tags: list[str]) -> None:
    pass

  @abstractmethod
  def route(self, from_tag: str, to_tag: str) -> list[str]:
    pass
