import time, numpy as np
start_time = time.time()

diagram = np.genfromtxt('diagram.txt', dtype = str, delimiter=1)

start = np.nonzero(diagram == 'S')
queue = [(start[0][0], start[1][0])]
count = 0

# part a
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