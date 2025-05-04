from structs.queue import Queue

def test_dequeue_empty() -> None:
  simple_queue = Queue[int]()
  value = simple_queue.dequeue()

  assert value is None

def test_enqueue() -> None:
  simple_queue = Queue[int]()

  simple_queue.enqueue(1)
  simple_queue.enqueue(2)
  simple_queue.enqueue(3)
  simple_queue.enqueue(4)
  simple_queue.enqueue(5)

  assert simple_queue.is_empty() is False
  assert simple_queue.calc_size() == 5

def test_dequeue() -> None:
  simple_queue = Queue[int]()

  simple_queue.enqueue(1)
  simple_queue.enqueue(2)
  simple_queue.enqueue(3)
  simple_queue.enqueue(4)
  simple_queue.enqueue(5)

  simple_queue.print("before dequeue")

  value = simple_queue.dequeue()

  simple_queue.print("after dequeue")

  assert value == 1
  assert simple_queue.calc_size() == 4

def test_queue_at_start() -> None:
  simple_queue = Queue[int]()

  simple_queue.enqueue(1)
  simple_queue.enqueue(2)
  simple_queue.enqueue(3)
  simple_queue.enqueue(4)
  simple_queue.enqueue(5)

  assert simple_queue.at_start() == 1

def test_queue_at_end() -> None:
  simple_queue = Queue[int]()

  simple_queue.enqueue(1)
  simple_queue.enqueue(2)
  simple_queue.enqueue(3)
  simple_queue.enqueue(4)
  simple_queue.enqueue(5)

  assert simple_queue.at_end() == 5

def test_queue_with_1m_elements() -> None:
  last_value = 0
  numbers_till = 10**6
  simple_queue = Queue[int]()

  for number in range(1, numbers_till):
    simple_queue.enqueue(number)

  assert simple_queue.calc_size() == numbers_till - 1

  for number in range(1, numbers_till):
    last_value = simple_queue.dequeue()

  assert last_value == numbers_till - 1
  assert simple_queue.calc_size() == 0
