from abc import ABC, abstractmethod

class CollectionInterface[T](ABC):
  @abstractmethod
  def insert(self, value: T) -> None:
    """Inserts a new value in the data structure"""
    pass

  @abstractmethod
  def delete(self, value: T) -> bool:
    """Deletes a value in the data structure"""
    pass

  @abstractmethod
  def contains(self, value: T) -> bool:
    """ Verifies if a value exists in data structure"""
    pass

  @abstractmethod
  def print() -> None:
    """Prints datastructure with string representation"""
    pass

  @abstractmethod
  def represent[RT](self) -> RT:
    """Pepresents the data structure with desired format"""
    pass

  @abstractmethod
  def is_empty(self) -> bool:
    """Check if the collection is empty"""
    pass

  @abstractmethod
  def calc_size(self) -> int:
    """Get collection size"""
    pass
