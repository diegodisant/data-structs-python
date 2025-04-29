from structs.stack import Stack

def test_pop_empty_stack() -> None:
  simple_stack = Stack[int]()
  top_value = simple_stack.pop()

  assert top_value is None

def test_stack() -> None:
  top_value: int | None = None
  simple_stack = Stack[int]()

  simple_stack.push(1)
  simple_stack.push(2)
  simple_stack.push(3)

  simple_stack.print("original stack")

  top_value = simple_stack.pop()

  simple_stack.print("popped 3")

  top_value = simple_stack.pop()

  simple_stack.print("popped 2")

  top_value = simple_stack.pop()

  simple_stack.print("popped 1")

  assert top_value is not None
  assert top_value == 1

def test_stack_push_1m_elements() -> None:
  simple_stack = Stack[int]()

  for number in range(1, 10**6):
    simple_stack.push(number)

def test_stack_pop_1m_elements() -> None:
  last_value: int = 0
  numbers_till = 10**6
  simple_stack = Stack[int]()

  for number in range(1, numbers_till):
    simple_stack.push(number)

  for number in range(1, numbers_till):
    last_value = simple_stack.pop()

  assert last_value == 1
