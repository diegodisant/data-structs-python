from random import randint
from tests.profiler import profile_test
from structs.tree import BinaryTree
from structs.tree.operations import TraverseOrder

def test_zeroed_binary_tree() -> None:
  tree = BinaryTree[int]()

  assert tree.calc_size() == 0
  assert tree.calc_depth() == 0

def test_binary_tree_one_insertion() -> None:
  tree = BinaryTree[int]()

  tree.insert(10)

  assert tree.calc_size() == 1
  assert tree.calc_depth() == 0

def test_binary_tree_insertion() -> None:
  tree = BinaryTree[int]()

  tree.insert(10)
  tree.insert(9)
  tree.insert(11)
  tree.insert(12)

  assert tree.calc_size() == 4
  assert tree.calc_depth() == 0

def test_binary_tree_insert_order() -> None:
  tree = BinaryTree[int]()

  tree.insert(5)
  tree.insert(4)
  tree.insert(6)
  tree.insert(3)
  tree.insert(2)
  tree.insert(7)

  root_node = tree.root_node

  assert root_node.value == 5
  assert root_node.left_node.value == 4
  assert root_node.right_node.value == 6

def test_binary_tree_pre_order_traverse() -> None:
  tree = BinaryTree[int]()

  tree.insert(20)
  tree.insert(15)
  tree.insert(25)
  tree.insert(12)
  tree.insert(17)
  tree.insert(27)
  tree.insert(23)

  current_traversal: list[int] = []
  expected_traversal: list[int] = [20, 15, 12, 17, 25, 23, 27]

  for value in tree.traverse(TraverseOrder.PRE_ORDER):
    current_traversal.append(value)

  assert expected_traversal == current_traversal

def test_binary_tree_in_order_traverse() -> None:
  tree = BinaryTree[int]()

  tree.insert(20)
  tree.insert(15)
  tree.insert(25)
  tree.insert(12)
  tree.insert(17)
  tree.insert(27)
  tree.insert(23)

  current_traversal: list[int] = []
  expected_traversal: list[int] = [12, 15, 17, 20, 23, 25, 27]

  for value in tree.traverse():
    current_traversal.append(value)

  assert expected_traversal == current_traversal

def test_binary_tree_post_order_traverse() -> None:
  tree = BinaryTree[int]()

  tree.insert(20)
  tree.insert(15)
  tree.insert(25)
  tree.insert(12)
  tree.insert(17)
  tree.insert(27)
  tree.insert(23)

  current_traversal: list[int] = []
  expected_traversal: list[int] = [12, 17, 15, 23, 27, 25, 20]

  for value in tree.traverse(TraverseOrder.POST_ORDER):
    current_traversal.append(value)

  assert expected_traversal == current_traversal


def test_traverse_in_order_1k_items() -> None:
  tree = BinaryTree[int]()

  max_limit = 1000
  random_root_value = randint(max_limit // 2, max_limit)

  tree.insert(random_root_value)

  for value in range(1, max_limit):
    tree.insert(value)

  for value in tree.traverse():
    print(f'{value}, ')

  print()
