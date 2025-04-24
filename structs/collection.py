from abc import ABC, abstractmethod
class CollectionInterface[T](ABC):
  @abstractmethod
  def insert(self, value: T) -> None:
    """Inserts a new value in the structure"""

  @abstractmethod
  def delete(self, value: T) -> bool:
    """Deletes a value in the structure"""

  @abstractmethod
  def contains(self, value: T) -> bool:
    """ Verifies if a value exists in structure"""

  @abstractmethod
  def print(self) -> None:
    """Prints structure with string representation"""

  @abstractmethod
  def represent[RT](self) -> RT:
    """Pepresents the structure with desired format"""

  @abstractmethod
  def is_empty(self) -> bool:
    """Check if the collection is empty"""

  @abstractmethod
  def calc_size(self) -> int:
    """Get collection size"""
