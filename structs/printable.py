from abc import ABC, abstractmethod

class Printable(ABC):
  @abstractmethod
  def print(self, message: str = "") -> None:
    """Prints structure with string representation"""
