from concurrent import futures
from structs import CollectionInterface
from structs import Printable
from structs.list.double import DoubleNode

class DoubleList[T](CollectionInterface[T], Printable):
  nodes_counter = 0
  tail_node: DoubleNode[T] = None
  header_node: DoubleNode[T] = None
  record_node: DoubleNode[T] = None

  def insert(self, value: T) -> None:
    self.nodes_counter += 1

    if self.header_node is None:
      self.header_node = DoubleNode(value)
      self.tail_node = self.header_node

      return

    self.record_node = self.header_node

    self.header_node = DoubleNode(
      value,
      self.record_node,
    )

    self.record_node.prev_node = self.header_node

    if self.tail_node.prev_node is None:
      self.tail_node.prev_node = self.header_node

  def delete(self, value: T) -> bool:
    if self.is_empty():
      return False

    prev_iter_node: DoubleNode[T] = None
    next_iter_node: DoubleNode[T] = None
    iter_node = self.header_node

    while iter_node is not None:
      if iter_node.value == value:
        if prev_iter_node is None and iter_node.next_node is None:
          self.nodes_counter = 0
          self.header_node = None
          self.tail_node = None

          return True

        self.nodes_counter -= 1

        next_iter_node = iter_node.next_node

        if prev_iter_node is not None and next_iter_node is not None:
          prev_iter_node.next_node = next_iter_node
          next_iter_node.prev_node = prev_iter_node

          return True

        if next_iter_node is not None and prev_iter_node is None:
          next_iter_node.prev_node = None
          self.header_node = next_iter_node

          return True

        if prev_iter_node is not None and next_iter_node is None:
          prev_iter_node.next_node = None
          self.tail_node = prev_iter_node

        return True

      prev_iter_node = iter_node
      iter_node = iter_node.next_node

  def contains(self, value: T, reverse: bool = False) -> bool:
    if self.is_empty():
      return False

    iter_node: DoubleNode[T] = None
    selected_node: DoubleNode[T] = None

    if reverse:
      iter_node = self.header_node
    else:
      iter_node = self.tail_node

    while iter_node is not None:
      if iter_node.value == value:
        return True

      selected_node = iter_node.next_node if reverse else iter_node.prev_node
      iter_node = selected_node

    return False

  def parallel_search(self, value: T):
    search_pool = futures.ThreadPoolExecutor(max_workers=2)

    search_task = search_pool.submit(self.contains, value)
    reverse_search_task = search_pool.submit(self.contains, value, True)
    search_tasks = [search_task, reverse_search_task]

    done_tasks, not_done_tasks = futures.wait(
      search_tasks,
      return_when=futures.FIRST_COMPLETED,
    )

    search_not_completed_task = not_done_tasks.pop()
    search_not_completed_task.cancel()

    return done_tasks.pop().result()

  def print(self, message: str = "", reverse: bool = False) -> None:
    print()
    print(message)

    if self.is_empty():
      print('[  ]')

      return

    iter_node: DoubleNode[T] = None
    selected_node: DoubleNode[T] = None

    if reverse:
      iter_node = self.header_node
    else:
      iter_node = self.tail_node

    print('[ ', end='')

    while iter_node is not None:
      selected_node = iter_node.next_node if reverse else iter_node.prev_node

      if selected_node is None:
        print(iter_node.value, end='')

        break

      print(iter_node.value, end=', ')

      iter_node = iter_node.next_node if reverse else iter_node.prev_node

    print(' ]')

  def represent[RT](self) -> RT:
    pass

  def is_empty(self) -> bool:
    return self.header_node is None and self.tail_node is None

  def calc_size(self) -> int:
    return self.nodes_counter
