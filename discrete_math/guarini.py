from itertools import *
import networkx as nx

g = nx.Graph()

# create representation of all possible formations as nodes of graph G
for arrangement in permutations(range(8), 4):
  node = ['*'] * 8
  node[arrangement[0]] = 'W'
  node[arrangement[1]] = 'W'
  node[arrangement[2]] = 'B'
  node[arrangement[3]] = 'B'
  g.add_node("".join(node))
# determine rules for creating edges
moves = [ [] for _ in range(8)]
moves[0] = [4, 6]
moves[1] = [5, 7]
moves[2] = [3, 6]
moves[3] = [2, 7]
moves[4] = [0, 5]
moves[5] = [1, 4]
moves[6] = [0, 2]
moves[7] = [3, 1]

print(g.nodes())

def add_edge(g, n1, n2):
  if not g.has_edge(n1, n2):
    g.add_edge(n1, n2)

for node in g.nodes():
  configuration = [ c for c in node ]
  for i in range(8):
    if configuration[i] == '*':
      continue
    for new_pos in moves[i]:
      if configuration[new_pos] != '*':
        continue
      new_configuration = list(configuration)
      new_configuration[new_pos] = configuration[i]
      new_configuration[i] = '*'
      print new_configuration, configuration
      add_edge(g, "".join(configuration), "".join(new_configuration))

print(nx.number_of_nodes(g))
print(nx.number_of_edges(g))
print(nx.number_connected_components(g))


for n1, n2 in g.edges():
  print n1[0], n1[1], n1[2], '\n', n1[3], ' ', n1[4], '\n', n1[5], n1[6], n1[7]
  print ' \\/'
  print n2[0], n2[1], n2[2], '\n', n2[3], ' ', n2[4], '\n', n2[5], n2[6], n2[7], '\n'
