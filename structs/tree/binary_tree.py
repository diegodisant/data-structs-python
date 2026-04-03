from typing import Generator

from structs import Printable
from structs.tree.node import TreeNode
from structs.tree.operations import TraverseOrder, TreeInterface

class BinaryTree[T](TreeInterface[T], Printable):
  depth: int = 0
  nodes_counter: int = 0
  root_node: TreeNode[T] | None = None

  def insert(self, value: T, current_node: TreeNode[T] | None = None) -> None:
    if self.root_node is None:
      self.nodes_counter += 1
      self.root_node = TreeNode(value)

      return

    if current_node is None:
      current_node = self.root_node

    if current_node.left_node is None and value < current_node.value:
      self.nodes_counter += 1

      current_node.left_node = TreeNode(value)

      return
    elif current_node.left_node is not None and value < current_node.value:
      return self.insert(value, current_node.left_node)

    if current_node.right_node is None and value > current_node.value:
      self.nodes_counter += 1

      current_node.right_node = TreeNode(value)

      return
    elif current_node.right_node is not None and value > current_node.value:
      return self.insert(value, current_node.right_node)

  def calc_size(self) -> int:
    return self.nodes_counter

  def calc_depth(self) -> int:
    # size
    return self.depth

  def traverse(
    self,
    order: TraverseOrder = TraverseOrder.IN_ORDER,
    node: TreeNode | None = None,
  ) -> Generator[T]:
    if node is None:
      node = self.root_node

    if order == TraverseOrder.PRE_ORDER:
      yield node.value

      if node.left_node is not None:
        yield from self.traverse(order, node.left_node)

      if node.right_node is not None:
        yield from self.traverse(order, node.right_node)

    if order == TraverseOrder.IN_ORDER:
      if node.left_node is not None:
        yield from self.traverse(order, node.left_node)

      yield node.value

      if node.right_node is not None:
        yield from self.traverse(order, node.right_node)

    if order == TraverseOrder.POST_ORDER:
      if node.left_node is not None:
        yield from self.traverse(order, node.left_node)

      if node.right_node is not None:
        yield from self.traverse(order, node.right_node)

      yield node.value

  # TODO: define printing algo for binary tree
  def print(self, message: str = "") -> None:
    print()
    print(message)

    if self.root_node is None:
      print('()')
