from enum import Enum
from typing import Generator
from abc import ABC, abstractmethod
from structs.tree.node import TreeNode

class TraverseOrder(Enum):
  PRE_ORDER   = 0 # root, left, right
  IN_ORDER    = 1 # left, root, right
  POST_ORDER  = 2 # left, right, root

class TreeInterface[T](ABC):
  @abstractmethod
  def insert(self, value: T) -> None:
    """Inserts one element in binary tree"""

  @abstractmethod
  def calc_size(self) -> int:
    """Calculates the node size of the binary tree"""

  @abstractmethod
  def calc_depth(self) -> int:
    """Calculates the deep of tree based on node size"""

  @abstractmethod
  def traverse(
    self,
    order: TraverseOrder = TraverseOrder.IN_ORDER,
    node: TreeNode | None = None,
  ) -> Generator[T]:
    """Traverse the binary tree with given order"""
