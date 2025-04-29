from abc import ABC, abstractmethod

class QueueInterface[T](ABC):
  @abstractmethod
  def enqueue(self, value: T) -> None:
    """Inserts a new value till the end"""

  @abstractmethod
  def dequeue(self) -> T | None:
    """Removes and get value from the first element from the queue"""

  @abstractmethod
  def at_start(self) -> T:
    """Gets value from queue at starts"""

  @abstractmethod
  def at_end(self) -> T:
    """Gets value from queue at ends"""

  @abstractmethod
  def is_empty(self) -> bool:
    """Check if the queue is empty"""

  @abstractmethod
  def calc_size(self) -> int:
    """Gets the queue size"""
