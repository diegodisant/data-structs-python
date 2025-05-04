from structs.tree.binary.node import BinaryTreeNode
from structs.tree.binary.operations import BinaryTreeInterface
from structs import Printable

class BinaryTree[T](BinaryTreeInterface[T], Printable):
  nodes_counter: int = 0
  root_node: BinaryTreeNode[T] = None

  def insert(self, value: T, current_node: BinaryTreeNode[T] = None) -> None:
    if self.root_node is None:
      self.nodes_counter += 1
      self.root_node = BinaryTreeNode(value)

      return

    if current_node is None:
      current_node = self.root_node

    if value < current_node.value:
      self.nodes_counter += 1

      current_node.left_node = BinaryTreeNode(value)

      return
    elif current_node.left_node is None:
      return self.insert(current_node.left_node)

    if value > current_node.value:
      self.nodes_counter += 1

      current_node.right_node = BinaryTreeNode(value)

      return
    elif current_node.right_node is None:
      return self.insert(current_node.right_node)

  def calc_size(self) -> int:
    return self.nodes_counter

  def calc_depth(self) -> int:
    return (self.nodes_counter // 2) + (self.nodes_counter % 2)

  def print(self, message: str = "") -> None:
    print()
    print(message)

    if self.root_node is None:
      print('()')


