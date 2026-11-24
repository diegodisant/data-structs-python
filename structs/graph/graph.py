from structs.graph.node import GraphNode, GraphData, GraphLinkData
from structs.graph.operations import GraphInterface
from structs.graph.error import CyclicNodeRefError, TagNotFoundError, RouteNotFoundError

VISITED = True
UNVISITED = False

class Graph(GraphInterface):
  tag_map: dict[str, GraphNode] = {}

  def add(self, tag: str, data: GraphData) -> None:
    # print(f'Add node: {tag}')
    # print(f'with data: {data}')

    node = GraphNode(tag, data)

    self.tag_map[tag] = node

  def get_unexistent_tags(self, tags: list[str]) -> list[str]:
    tags_set = set(tags)
    mapped_tags_set = set(self.tag_map.keys())

    unexistent_tags = tags_set - mapped_tags_set

    return list(unexistent_tags)

  def rel(self, tag: str, ref_tags: list[str]) -> None:
    print(f'Relate node: {tag} to nodes: {ref_tags}')

    if tag in ref_tags:
      raise CyclicNodeRefError(tag, 'rel')

    at_node = self.tag_map.get(tag)

    if at_node is None:
      raise TagNotFoundError(tag, 'rel')

    unexistent_tags = self.get_unexistent_tags(ref_tags)
    unexistent_tags_size = len(unexistent_tags)

    if unexistent_tags_size > 0:
      raise TagNotFoundError(f'with unexistent tags {unexistent_tags}', 'rel')

    for ref_tag in ref_tags:
      to_node = self.tag_map[ref_tag]

      link_data = GraphLinkData(
        at_node.data,
        to_node.data,
        tag,
        ref_tag,
      )

      at_node.refs[ref_tag] = link_data

  def traverse(self, tags: list[str]) -> None:
    print(f'Traversing with following route: {' -> '.join(tags)}')

    unexistent_tags = self.get_unexistent_tags(tags)
    unexistent_tags_size = len(unexistent_tags)

    if unexistent_tags_size > 0:
      raise TagNotFoundError(f'with unexistent tags {unexistent_tags}', 'rel')

    while len(tags) > 1:
      at_tag = tags[0]
      to_tag = tags[1]

      at_node = self.tag_map[at_tag]
      link = at_node.refs.get(to_tag)

      if link is None:
        raise RouteNotFoundError(f'{at_tag} -> {to_tag}', 'rel')

      to_node = self.tag_map[to_tag]

      print(f'[traverse] Connecting routes: {link.route}')
      print(f'[traverse] visited: {at_tag}')
      print(f'[traverse] distance: {link.distance}')
      print(f'[traverse] from: {at_node.data}')
      print(f'[traverse] to: {to_node.data}')

      tags.pop(0)

  def route(self, from_tag: str, to_tag: str) -> list[str]:
    from_node = self.tag_map.get(from_tag)

    if from_node is None:
      raise TagNotFoundError(from_tag, 'route')

    if to_tag not in self.tag_map:
      raise TagNotFoundError(from_tag, 'route')

    target_found = False
    selected_route: list[str] = [ from_tag ]
    traverse_queue: dict[str, bool] = { from_tag: False }

    current_node = from_node.copy()
    next_queue_node: GraphNode | None = None

    target_link: GraphLinkData | None = None
    current_link: GraphLinkData | None = None

    while not target_found:
      target_link = current_node.refs.get(to_tag)

      if target_link is not None:
        target_found = True

        selected_route.append(to_tag)

        continue

      current_link = self.get_next_unvisited_link(current_node.refs)

      if current_link is not None:
        current_node = self.tag_map[current_link.to_tag]

        current_link.visited = True

        selected_route.append(current_node.tag)

        continue

      traverse_queue[current_node.tag] = VISITED

      next_queue_node = self.get_next_unvisited_node(traverse_queue)

      selected_route = [ from_tag ]

      if next_queue_node is None:
        raise RouteNotFoundError(f'{from_tag} -> {to_tag}', 'route')

      current_node = next_queue_node

    return selected_route

  def get_next_unvisited_link(self, refs: dict[str, GraphLinkData]) -> GraphLinkData | None:
    if not refs:
      return None

    unvisited_links: list[GraphLinkData] = [
      link
      for link in refs.values()
      if link.visited == UNVISITED
    ]

    if not unvisited_links:
      return None

    first_link = unvisited_links[0]

    return first_link

  def get_next_unvisited_node(self, queue: dict[str, bool]) -> GraphNode | None:
    unvisited_tags: list[str] = [
      tag
      for tag, links_visited in queue.items()
      if links_visited == UNVISITED
    ]

    if not unvisited_tags:
      return None

    first_tag = unvisited_tags[0]
    first_node = self.tag_map[first_tag]

    return first_node
