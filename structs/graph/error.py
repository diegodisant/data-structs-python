from abc import ABC, abstractmethod

class GraphError(BaseException):
  context: str
  message: str

  def __init__(self, *args: object) -> None:
    super().__init__(*args)

    content = str(args[0])
    self.context = str(args[1])

    self.build_message(content)

    print(self.message) # TODO: remove in future debug only

  def build_message(self, content: str) -> None:
    self.message = f'[{self.context}] Error {content}'

class NotFoundError(GraphError, ABC):
  @property
  @abstractmethod
  def element(self) -> str:
    pass

  def build_message(self, content: str) -> None:
    self.message = f'[{self.context}] Error: {self.element} not found: {content}'

class RouteNotFoundError(NotFoundError):
  @property
  def element(self) -> str:
    return 'route'

class TagNotFoundError(NotFoundError):
  @property
  def element(self) -> str:
    return 'tag'

class CyclicNodeRefError(GraphError):
  def build_message(self, content: str) -> None:
    self.message = f'[{self.context}] Error cannot associate the same tag node: {content}'
