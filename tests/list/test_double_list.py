from structs.list.double.double_list import DoubleList

def test_zeroed_double_list() -> None:
  double_list = DoubleList()

  assert double_list.is_empty() is True

def test_double_list_insertion() -> None:
  double_list = DoubleList[int]()

  double_list.insert(1)
  double_list.insert(2)
  double_list.insert(3)
  double_list.insert(4)
  double_list.insert(5)

  double_list.print("double list")

  assert double_list.is_empty() is False
  assert double_list.calc_size() == 5

def test_double_list_1m_items_insertion() -> None:
  max_number = 10**6
  double_list = DoubleList[int]()

  for number in range(1, max_number):
    double_list.insert(number)

  assert double_list.is_empty() is False
  assert double_list.calc_size() == max_number - 1

def test_double_list_search_in_1m_items() -> None:
  max_number = 10**6
  seek_number = max_number - 5
  double_list = DoubleList[int]()

  for number in range(1, max_number):
    double_list.insert(number)

  search_result = double_list.contains(seek_number)

  assert search_result is True

def test_double_list_reverse_search_in_1m_items() -> None:
  max_number = 10**6
  seek_number = max_number - 5
  double_list = DoubleList[int]()

  for number in range(1, max_number):
    double_list.insert(number)

  search_result = double_list.contains(seek_number, reverse=True)

  assert search_result is True

def test_double_list_parallel_search_in_1m_items() -> None:
  max_number = 10**6
  seek_number = max_number - 5
  double_list = DoubleList[int]()

  for number in range(1, max_number):
    double_list.insert(number)

  search_result = double_list.parallel_search(seek_number)

  assert search_result is True
