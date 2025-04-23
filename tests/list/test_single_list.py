from structs.list.single.list import SingleList

def test_zeroed_single_list() -> None:
  list = SingleList()

  assert list.is_empty() == True
  assert list.calc_size() == 0

def test_single_list_insertion() -> None:
  list = SingleList[int]()

  list.insert(1)
  list.insert(2)
  list.insert(3)
  list.insert(4)
  list.insert(5)

  assert list.calc_size() == 5
