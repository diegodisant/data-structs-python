from structs import Printable
from structs.tree.node import TreeNode
from structs.tree.operations import TreeInterface

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
    elif current_node.left_node is not None:
      return self.insert(value, current_node.left_node)

    if current_node.right_node is None and value > current_node.value:
      self.nodes_counter += 1

      current_node.right_node = TreeNode(value)

      return
    elif current_node.right_node is not None:
      return self.insert(value, current_node.right_node)

  def calc_size(self) -> int:
    return self.nodes_counter

  def calc_depth(self) -> int:
    # use recursivity to calc the depth
    return self.depth

  # TODO: define printing algo for binary tree
  def print(self, message: str = "") -> None:
    print()
    print(message)

    if self.root_node is None:
      print('()')
