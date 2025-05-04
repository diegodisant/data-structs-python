from structs.tree.binary import BinaryTree

def test_zeroed_binary_tree() -> None:
  binary_tree = BinaryTree[int]()

  assert binary_tree.calc_size() == 0
  assert binary_tree.calc_depth() == 0

def test_binary_tree_one_insertion() -> None:
  binary_tree = BinaryTree[int]()

  binary_tree.insert(10)

  assert binary_tree.calc_size() == 1
  assert binary_tree.calc_depth() == 1

def test_binary_tree_insertion() -> None:
  binary_tree = BinaryTree[int]()

  binary_tree.insert(10)
  binary_tree.insert(9)
  binary_tree.insert(11)
  binary_tree.insert(12)

  assert binary_tree.calc_size() == 4
  assert binary_tree.calc_depth() == 2
