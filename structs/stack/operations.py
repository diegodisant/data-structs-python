from abc import ABC, abstractmethod

class StackInterface[T](ABC):
  @abstractmethod
  def pop() -> T | None:
    """ pop one value from stack """

  @abstractmethod
  def push(value: T) -> None:
    """ push one value to the stack """
