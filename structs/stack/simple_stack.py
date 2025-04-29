from structs import Printable
from structs.list.single import SingleNode
from structs.list.single import SingleList
from structs.stack.operations import StackInterface
class Stack[T](StackInterface[T], Printable):
  single_list: SingleList[T] = None

  def __init__(self) -> None:
    self.single_list = SingleList[T]()

  def pop(self) -> T | None:
    if self.single_list.is_empty():
      return None

    self.single_list.nodes_counter -= 1

    top_node: SingleNode[T] = self.single_list.header_node
    node_value: T = top_node.value

    self.single_list.header_node = top_node.next_node

    return node_value

  def push(self, value: T) -> None:
    self.single_list.insert(value)

  def print(self, message: str = "") -> None:
    if self.single_list.is_empty():
      print("[ ]")

      return

    print()
    print(message)

    top_node: SingleNode[T] = self.single_list.header_node

    while top_node is not None:
      print(f"[ {top_node.value} ]")

      top_node = top_node.next_node

    print()
