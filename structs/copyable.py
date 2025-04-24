from abc import ABC, abstractmethod

class Copyable[T](ABC):
  @abstractmethod
  def copy(self) -> T:
    pass
