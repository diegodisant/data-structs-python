from structs.collection import CollectionInterface
from structs.list.single.node import SingleNode

class SingleList[T](CollectionInterface[T]):
  nodes_counter = 0
  header_node: SingleNode[T] = None
  record_node: SingleNode[T] = None

  def insert(self, value: T) -> None:
    self.nodes_counter += 1

    if self.is_empty():
      self.header_node = SingleNode(value)

      return

    self.record_node = SingleNode(value, self.header_node)

    self.header_node = self.record_node

  def delete(self, value: T) -> bool:
    pass

  def contains(self, value: T) -> bool:
    iter_node = self.record_node.copy()

    while iter_node is not None:
      if iter_node.value == value:
        return True

      iter_node = iter_node.next_node

    return False

  def print(self) -> None:
    pass

  def represent[RT](self) -> RT:
    pass

  def is_empty(self) -> bool:
    return self.header_node is None

  def calc_size(self) -> int:
    return self.nodes_counter
