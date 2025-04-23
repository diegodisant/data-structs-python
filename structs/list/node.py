from typing import Self

class Node[T]:
  value: T
  next_node: Self

  def __init__(self, value: T, next_node: Self = None) -> None:
    self.value = value
    self.next_node = next_node
