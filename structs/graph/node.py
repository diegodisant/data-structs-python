from typing import Self
from math import sqrt, pow
from dataclasses import dataclass

@dataclass
class GraphData:
  lat: float
  lon: float
  address: str

@dataclass
class GraphLinkData:
  # in kms
  # a = origin node
  # b = destination node
  # distance = sqrt((b.lat - a.lat)^2 + (b.lon - a.lon)^2)
  distance: float

  route: str # A -> B

  def __init__(self,
    at: GraphData,
    to: GraphData,
    at_tag: str,
    to_tag: str,
  ) -> None:
    self.distance = self.calc_distance(at, to)
    self.route = f'{at_tag} -> {to_tag}'

  def calc_distance(self, at: GraphData, to: GraphData) -> float:
    print(f'Calculating distance from {self.route}:')
    print(f'origin: {at}')
    print(f'destination: {to}')
    print()

    lat_sub = to.lat - at.lat
    lat_factor = pow(lat_sub, 2)

    lon_sub = to.lon - at.lon
    lon_factor = pow(lon_sub, 2)

    distance = sqrt(lat_factor + lon_factor)

    return distance

class GraphNode:
  tag: str

  data: GraphData

  # relation with other nodes tags
  refs: dict[str, GraphLinkData]

  def __init__(self, tag: str, data: GraphData) -> None:
    self.tag = tag
    self.data = data

'''
A -- B
|    |
C -- D

insert: A, B, C, D

generate links
# A
rel(A, B)
rel(A, C)

# B
rel(B, A)
rel(B, D)

# C
rel(C, A)
rel(C, D)

# D
rel(D, B)
rel(D, C)

localization
HashMap<tag, node>

<'A', 0x1>
<'B', 0x2>
<'C', 0x3>
<'D', 0x4>

Space Required
O(N + E)

Check if (A, B) exists #improvement
from: O(degree(A))
to: O(1 + N) # faster

Find all neighboors of A
from: O(degree(A))
to: O(1) # super faster

[A, B, C, D]

traversal:
[A, B]
[B, C]
[C, D]
'''
