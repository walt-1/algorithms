# Kruskals Algorithm

# Greedy algorithm in graph theory
# Seeks to create a minimum spanning tree given a graph with weighted edges

def Kruskal(G):
A = ∅
for v in G:
 MAKE-SET(v)
  for each(u, v) in G.E ordered by weight(u, v), increasing do
   if FIND-SET(u) ≠ FIND-SET(v) then
      A: = A ∪ {(u, v)}
       UNION(FIND-SET(u), FIND-SET(v))
    return A
