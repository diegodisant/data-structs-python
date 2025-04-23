from structs.collection import CollectionInterface
from structs.list.single.node import SingleNode

class SingleList[T](CollectionInterface[T]):
  nodes_counter = 0
  current_node: SingleNode[T] = None
  record_node: SingleNode[T] = None

  def insert(self, value: T) -> None:
    self.nodes_counter += 1

    if self.is_empty():
      self.current_node = SingleNode(value)
      self.current_node.value = value

      return

    self.record_node = SingleNode(value, self.current_node)

    self.current_node = self.record_node

  def delete(self, value: T) -> bool:
    pass

  def contains(self, value: T) -> bool:
    pass

  def print(self) -> None:
    pass

  def represent[RT](self) -> RT:
    pass

  def is_empty(self) -> bool:
    return self.current_node is None

  def calc_size(self) -> int:
    return self.nodes_counter
