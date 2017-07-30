def shortest_path_dfs(graph, curr, search):
  if curr == search:
    return graph[curr]['dist']

  distances = []
  for neighbor in graph[curr]['neighbors']:
    if graph[neighbor]['dist'] == None:
      graph[neighbor]['dist'] = graph[curr]['dist'] + 1
      dist = shortest_path_dfs(graph, neighbor, search)
      if dist:
        distances.append(dist)
    if distances:
      return min(distances)
    else:
      return -1