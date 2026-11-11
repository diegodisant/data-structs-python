from typing import Self
from dataclasses import dataclass, asdict

@dataclass
class GraphData:
  lat: float
  lon: float
  address: str

@dataclass
class GraphLinkData:
  distance: float #in kms

class GraphLink:
  from_node: GraphNode
  to_node: GraphNode
  data: GraphLinkData

class GraphNode:
  tag: str
  # TODO: relate graph data in every link
  # data: dict
  refs: list[GraphLink]

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
'''
