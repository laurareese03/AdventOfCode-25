import time, numpy as np
start_time = time.time()

diagram = np.genfromtxt('diagram.txt', dtype = str, delimiter=1)
diagram_copy = diagram.copy()

start = np.nonzero(diagram == 'S')
queue = [(start[0][0], start[1][0])]
count = 0

# part a
# oops queue.pop makes it dfs
while queue:
  current = queue.pop()
  diagram[current] = '|'
  below = (current[0]+1, current[1])

  if below[0] == len(diagram):
    continue
  if diagram[below] == '.':
    queue.append(below)
  elif diagram[below] == '^':
    count += 1
    queue.append((below[0], below[1]-1))
    queue.append((below[0], below[1]+1))
print(count)

# part b
# we use the same dfs we did for part a, but add memoization to count each path
# without it, the code will run for 2 hours and crashes VSCode before finishing
# with it, it runs in 51 miliseconds. huzzah.
visited = {}
def dfs(queue):
  current = queue.pop()
  if current not in visited:
    if current[0] == len(diagram):
      visited[current] = 1
    else:
      below = (current[0]+1, current[1])
      if diagram[current] == '.':
        queue.append(below)
        visited[current] = dfs(queue)
      else: # diagram[current] == '^':
        visited[current] = 0
        queue.append((below[0], below[1]-1))
        visited[current] += dfs(queue)
        queue.append((below[0], below[1]+1))
        visited[current] += dfs(queue)
  return visited[current]

queue = [(start[0][0], start[1][0])]
diagram = diagram_copy
diagram[start] = '.'
print(dfs(queue))

print(time.time() - start_time)