from typing import Self

class TreeNode[T]:
  value: T
  left_node: Self
  right_node: Self

  def __init__(self, value: T, left_node: Self = None, right_node: Self = None):
    self.value = value
    self.left_node = left_node
    self.right_node = right_node
