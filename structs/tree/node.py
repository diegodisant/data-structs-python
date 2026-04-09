from typing import Self

class TreeNode[T]:
  value: T

  left_node: Self | None = None
  right_node: Self | None = None
  backref_node: Self | None = None

  def __init__(self, value: T):
    self.value = value

  def less(self, current_value: T) -> bool:
    current_number = self.numerical_value(current_value)
    actual_number = self.numerical_value(self.value)

    return current_number < actual_number

  def numerical_value(self, value: T) -> int | float:
    return int(value) # pyright: ignore[reportArgumentType]

