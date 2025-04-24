from structs import Printable
from structs import CollectionInterface
from structs.list.single.node import SingleNode
class SingleList[T](CollectionInterface[T], Printable):
  nodes_counter = 0
  header_node: SingleNode[T] = None

  def insert(self, value: T) -> None:
    self.nodes_counter += 1

    if self.is_empty():
      self.header_node = SingleNode(value)

      return

    self.header_node = SingleNode(value, self.header_node)

  def delete(self, value: T) -> bool:
    if self.is_empty():
      return False

    prev_node: SingleNode[T] = None
    iter_node = self.header_node.copy()

    if iter_node.value == value:
      self.nodes_counter -= 1
      self.header_node = iter_node.next_node

      return True

    while iter_node is not None:
      if iter_node.value == value:
        self.nodes_counter -= 1
        prev_node.next_node = iter_node.next_node

        if self.nodes_counter == 1:
          self.header_node = prev_node

        return True

      prev_node = iter_node
      iter_node = iter_node.next_node

    return False

  def contains(self, value: T) -> bool:
    iter_node = self.header_node.copy()

    while iter_node is not None:
      if iter_node.value == value:
        return True

      iter_node = iter_node.next_node

    return False

  def print(self, message: str = "") -> None:
    print()
    print(message)

    if self.is_empty():
      print('[]')

      return

    iter_node = self.header_node.copy()

    print('[', end='')

    while iter_node is not None:
      if iter_node.next_node is None:
        print(iter_node.value, end='')

        break

      print(iter_node.value, end=', ')

      iter_node = iter_node.next_node

    print(']')

  def represent[RT](self) -> RT:
    pass

  def is_empty(self) -> bool:
    return self.header_node is None

  def calc_size(self) -> int:
    return self.nodes_counter
