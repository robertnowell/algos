def shortest_path_dfs(graph, curr, search):
  if curr == search:
    # print 'returning curr {} == search {}, dist {}'.format(curr, search, graph[curr]['dist'])
    return graph[curr]['dist']

  distances = []
  for neighbor in graph[curr]['neighbors']:
    # print 'new neighbor. curr {}, neighbor {}, distances {}'.format(curr, neighbor, distances)
    if graph[curr]['dist'] == None:
      import pdb; pdb.set_trace()
    if graph[neighbor]['dist'] == None or neighbor == search:
      graph[neighbor]['dist'] = graph[curr]['dist'] + 1
      dist = shortest_path_dfs(graph, neighbor, search)
      distances.append(dist)
  # print ('loop exited. curr {}, distances {}'.format(curr, distances))
  if distances == []:
    # Don't rely on this for really big graphs.
    return 1000000
  return min(distances)

def reset_graph(graph, start):
  for k, d in graph.iteritems():
    if k == start:
      d['dist'] = 0
    else:
      d['dist'] = None

if __name__ == '__main__':
  graph = {
    'A': {'neighbors': ['C','F'],       'dist': 0},
    'B': {'neighbors': ['C','D'],       'dist': None},
    'C': {'neighbors': ['A', 'B', 'E'], 'dist': None},
    'D': {'neighbors': ['B', 'F', 'G'], 'dist': None},
    'E': {'neighbors': ['C','G'],       'dist': None},
    'F': {'neighbors': ['A', 'F', 'G'], 'dist': None},
    'G': {'neighbors': ['D','E', 'F'],  'dist': None},
  }

  assert shortest_path_dfs(graph, 'A', 'G') == 3
  reset_graph(graph, 'A')
  assert shortest_path_dfs(graph, 'A', 'F') == 1
  reset_graph(graph, 'A')
  assert shortest_path_dfs(graph, 'A', 'A') == 0
  reset_graph(graph, 'A')
  assert shortest_path_dfs(graph, 'A', 'G') == 3
  reset_graph(graph, 'C')
  assert shortest_path_dfs(graph, 'C', 'G') == 2