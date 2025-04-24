from typing import Self
from structs.copyable import Copyable
from structs.list.node import Node

class SingleNode[T](Node[T], Copyable[Self]):
  def copy(self) -> Self:
    copied_node = SingleNode[T](
      self.value,
      self.next_node,
    )

    return copied_node
