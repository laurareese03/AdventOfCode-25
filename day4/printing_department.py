import time, numpy as np
start_time = time.time()

diagram = np.genfromtxt('diagram.txt', dtype = str, delimiter=1)

def get_nearby_rolls(x, y):
  x_offset = 0 if x == 0 else 1
  y_offset = 0 if y == 0 else 1
  neighbors = diagram[x-x_offset:x+2, y-y_offset:y+2]

  return np.count_nonzero(neighbors == '@')

original_count = np.count_nonzero(diagram == '@')

count = 0
last_removed_count = 1
iteration = 0
while last_removed_count > 0:
  last_removed_count = 0
  pairings = []
  for i in range(len(diagram)):
    for j in range(len(diagram[0])):
      if diagram[i][j] == '@' and get_nearby_rolls(i, j) < 5:
        count += 1
        last_removed_count += 1
        pairings.append((i,j))

  for pairing in pairings:
    diagram[pairing] = '.'

  if iteration == 0:
    print(count)
  iteration += 1
  
new_count = np.count_nonzero(diagram == '@')
print(original_count - new_count)

print(time.time() - start_time)