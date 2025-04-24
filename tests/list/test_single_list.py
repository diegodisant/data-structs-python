from tests.profiler import profile_test
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

def test_contains_success() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  assert single_list.contains(1) is True

@profile_test
def test_contains_failed() -> None:
  single_list = SingleList[int]()

  single_list.insert(1)
  single_list.insert(2)
  single_list.insert(3)
  single_list.insert(4)
  single_list.insert(5)

  assert single_list.contains(-1) is False
