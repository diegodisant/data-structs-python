from abc import ABC, abstractmethod
from structs.tree.binary.node import BinaryTreeNode

class BinaryTreeInterface[T](ABC):
  @abstractmethod
  def insert(self, value: T, current_node: BinaryTreeNode[T] = None) -> None:
    """Inserts one element in binary tree"""

  @abstractmethod
  def calc_size(self) -> int:
    """Calculates the node size of the binary tree"""

  @abstractmethod
  def calc_depth(self) -> int:
    """Calculates the deep of tree based on node size"""
