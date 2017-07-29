from collections import deque

def shortest_path(graph, start, search):
  info = {}
  for k, v in graph.iteritems():
    if (k == start):
      dist = 0
    else:
      dist = None
    info[k] = {
      'vertex':     k,
      'neighbors':  v, 
      'dist':       dist, 
      'path':       []
    }
  q = deque(start)
  while q:
    curr = q.popleft()
    if curr == search:
      return info[curr]
    for neighbor in info[curr]['neighbors']:
      if info[neighbor]['dist'] == None:
        info[neighbor]['dist'] = info[curr]['dist'] + 1
        info[neighbor]['path'] = info[curr]['path'] + [curr]
        q.append(neighbor)
  return -1

if __name__ == "__main__":
  adj_dict = {
    'A': ['B', 'E', 'F'],
    'B': ['A', 'D', 'G'],
    'C': ['F'],
    'D': ['B', 'E'],
    'E': ['A', 'D', 'H'],
    'F': ['A', 'C'],
    'G': ['B', 'H'],
    'H': ['E', 'G'],
  }
  res_h = shortest_path(adj_dict, 'A', 'H')
  assert res_h['path'] == ['A', 'E']
  assert res_h['dist'] == 2

  res_g = shortest_path(adj_dict, 'A', 'G')
  assert res_g['path'] == ['A', 'B']
  assert res_g['dist'] == 2

  res_c = shortest_path(adj_dict, 'A', 'C')
  assert res_c['path'] == ['A', 'F']
  assert res_c['dist'] == 2

  res_e = shortest_path(adj_dict, 'A', 'E')
  assert res_e['path'] == ['A']
  assert res_e['dist'] == 1