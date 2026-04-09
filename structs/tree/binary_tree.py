from typing import Generator
from structs import Printable
from structs.tree.node import TreeNode
from structs.tree.operations import TraverseOrder, TreeInterface

class BinaryTree[T](TreeInterface[T], Printable):
  depth: int = 0
  nodes_counter: int = 0
  root_node: TreeNode[T] | None = None
  side_left_node: TreeNode[T] | None = None
  side_right_node: TreeNode[T] | None = None

  def insert(self, value: T) -> None:
    if self.root_node is None:
      self.nodes_counter += 1
      self.root_node = TreeNode(value)

      return

    if self.root_node.value == value:
      return

    current_node = self.root_node
    left_node: TreeNode[T] | None = None
    right_node: TreeNode[T] | None = None
    has_less_value: bool = False

    # TODO: check if node adding follow the main branch
    # without traverse in children
    traversed_in_left: bool = False
    traversed_in_right: bool = False

    while current_node is not None:
      left_node = current_node.left_node
      has_less_value = current_node.less(value)

      if has_less_value and left_node is None:
        self.nodes_counter += 1

        current_node.left_node = TreeNode(value)
        current_node.left_node.backref_node = current_node

        if traversed_in_left == True and traversed_in_right == False:
          self.side_left_node = current_node.left_node

        return
      elif has_less_value and left_node is not None:
        current_node = left_node

        traversed_in_left = True

        continue

      right_node = current_node.right_node

      if not has_less_value and right_node is None:
        self.nodes_counter += 1

        current_node.right_node = TreeNode(value)
        current_node.right_node.backref_node = current_node

        if traversed_in_left == False and traversed_in_right == True:
          self.side_right_node = current_node.right_node

        return
      elif not has_less_value and right_node is not None:
        current_node = right_node

        traversed_in_right = True

        continue

  def traverse(
    self,
    order: TraverseOrder = TraverseOrder.IN_ORDER,
    node: TreeNode | None = None
  ) -> Generator[T]:
    node = self.root_node

    if order == TraverseOrder.IN_ORDER:
      node = self.side_left_node

    if order == TraverseOrder.POST_ORDER:
      node = self.side_right_node

    while node is not None:
      if order == TraverseOrder.IN_ORDER:
        yield node.value

        node = node.backref_node

  def calc_size(self) -> int:
    return self.nodes_counter

  def calc_depth(self) -> int:
    return self.depth

  # TODO: define printing algo for binary tree
  def print(self, message: str = "") -> None:
    print()
    print(message)

    if self.root_node is None:
      print('()')
