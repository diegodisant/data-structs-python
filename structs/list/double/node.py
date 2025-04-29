from typing import Self
from structs import Copyable
from structs.list import Node
class DoubleNode[T](Node[T], Copyable[Self]):
  prev_node: Self

  def __init__(
    self,
    value: T,
    next_node: Self = None,
    prev_node: Self = None
  ) -> None:
    super().__init__(value, next_node)
    self.prev_node = prev_node

  def copy(self) -> Self:
    copied_node = DoubleNode[T](
      self.value,
      self.next_node,
      self.prev_node,
    )

    return copied_node
