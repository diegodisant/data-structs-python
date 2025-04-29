from structs.list.single import SingleList

def test_zeroed_single_list() -> None:
  single_list = SingleList()

  assert single_list.is_empty() is True
  assert single_list.calc_size() == 0

def test_single_list_insertion() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  assert single_list.calc_size() == 5

def test_single_list_contains_success() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  assert single_list.contains(1) is True

def test_single_list_contains_failed() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  assert single_list.contains(-1) is False

def test_search_in_1m_items() -> None:
  seeked_number = 2
  single_list = SingleList[int]()

  for number in range(1, 10**6):
    single_list.insert(number)

  assert single_list.contains(seeked_number) is True

def test_single_list_delete_in_middle() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  single_list.print("before deletion")

  single_list.delete(3)

  single_list.print("after deletion")

  assert single_list.calc_size() == 4

def test_single_list_delete_in_head() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  single_list.print("before deletion")

  single_list.delete(5)

  single_list.print("after deletion")

  assert single_list.calc_size() == 4

def test_single_list_delete_in_tail() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  single_list.print("before deletion")

  single_list.delete(1)

  single_list.print("after deletion")

  assert single_list.calc_size() == 4

def test_single_list_delete_all_from_tail() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)

  single_list.print("before deletion")

  single_list.delete(1)
  single_list.delete(2)
  single_list.delete(3)

  single_list.print("after deletion")

  assert single_list.calc_size() == 0

def test_delete_all_from_head() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)

  single_list.print("before deletion")

  single_list.delete(3)
  single_list.delete(2)
  single_list.delete(1)

  single_list.print("after deletion")

  assert single_list.calc_size() == 0
