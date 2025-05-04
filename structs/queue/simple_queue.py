from structs.printable import Printable
from structs.queue.operations import QueueInterface
from structs.list.double import DoubleList, DoubleNode

class Queue[T](QueueInterface[T], Printable):
  double_list: DoubleList[T] = None

  def __init__(self) -> None:
    self.double_list = DoubleList[T]()

  def enqueue(self, value: T) -> None:
    self.double_list.insert(value)

  def dequeue(self) -> T | None:
    if self.is_empty():
      return None

    self.double_list.nodes_counter -= 1

    first_node: DoubleNode[T] = self.double_list.tail_node
    prev_node: DoubleNode[T] = first_node.prev_node

    node_value: T = first_node.value

    if prev_node is not None:
      prev_node.next_node = None

    self.double_list.tail_node = prev_node

    return node_value

  # TODO: implement stack printing
  def print(self, message: str = "") -> None:
    print()
    print(message)

    if self.is_empty():
      print('[ ]')

      return

    iter_node: DoubleNode[T] = self.double_list.tail_node

    while iter_node is not None:
      print(' ', end='')
      print(f"[{iter_node.value}]", end='')

      iter_node = iter_node.prev_node

    print()

  def at_start(self) -> T:
    return self.double_list.tail_node.value

  def at_end(self) -> T:
    return self.double_list.header_node.value

  def is_empty(self) -> bool:
    return self.double_list.is_empty()

  def calc_size(self) -> int:
    return self.double_list.calc_size()
