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

def test_stack_with_1m_elements() -> None:
  last_value = 0
  numbers_till = 10**6
  simple_stack = Stack[int]()

  for number in range(1, numbers_till):
    simple_stack.push(number)

  for number in range(1, numbers_till):
    last_value = simple_stack.pop()

  assert last_value == 1

def test_check_non_valid_expression() -> None:
  expression = '{[(<<<a expression>>)]}'
  stack = Stack[str]()
  open_symbols = ['{', '[', '(', '<']
  close_symbols = ['>', ')', ']', '}']
  expression_symbols = [*open_symbols, *close_symbols]

  open_symbols_counter = 0
  close_symbols_counter = 0

  for symbol in expression:
    if symbol not in expression_symbols:
      print(f'ignoring not expression symbol: {symbol}')

      continue

    print(f'pushing symbol in the stack: {symbol}')

    stack.push(symbol)

  stack_value: str | None = stack.pop()

  while stack_value is not None:
    if stack_value in open_symbols:
      open_symbols_counter += 1

    if stack_value in close_symbols:
      close_symbols_counter += 1

    stack_value = stack.pop()

  if close_symbols_counter != open_symbols_counter:
    print(f'Error open expression symbols doesnt match closed expression symbols')

  if close_symbols_counter > open_symbols_counter:
    print(f'There is more closed symbols, please check the enclosure')

  if open_symbols_counter > close_symbols_counter:
    print(f'There is more open symbols, please check the openings')

  assert close_symbols_counter < open_symbols_counter
