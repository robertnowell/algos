# list of dictionaries
# [
#   {'name': 'abc', 'type': 'START', 'time': 100},
#   {'name': 'abc', 'type': 'END',   'time': 200},
# ]

# use a stack, push to stack when new function call is started
# pop from stack when function call is ended
# we can be sure that when we pop, it will be the most recent call that has finished.
# keeping track of timing
# once target function begins,
# inclusive = {
#   start:
#   end:
#   total:
# }

# exclusive = {
#   target_start:,
#   target_end:,
#   extra_time: {
#      name: {
#        start,
#        end
#      }, ...
#   }
# }

def function_times(inputs, name):
  exclusive = {
    target_start:,
    target_end:,
    children_start:,
    children_end:
  }
  inclusive = {
    start:
    end:
    total:
  }
  stack = stack()
  for elem in inputs:
    if elem.type = 'START':
      stack.push(elem)
      if elem.name == name:
        inclusive.start = elem.time
        exclusive.target_start = elem.time
      elif exclusive.target_start:
        exclusive.extra_time[elem.name] = {'start': elem.time}
    if elem.type = 'END':
      test = stack.pop()
      if elem.name == name:
        inclusive.end = elem.time
        exclusive.target_end = elem.time
      else:
        exclusive.extra_time[elem.name].