import time, queue as q, math
start_time = time.time()

locations = open('junction_boxes.txt').read().strip().split('\n')
locations = [tuple(map(int, l.split(','))) for l in locations]

rounds = {}

for l in locations:
  rounds[l] = set()
  rounds[l].add((l))

def get_distance(x, y):
  return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[2] - x[2]) ** 2)

def print_top_circuits():
  circuit_sizes = []
  visited = set()
  for r in rounds:
    if r not in visited:
      visited = visited.union(rounds[r])
      circuit_sizes.append(len(rounds[r]))

  sorted_sizes = sorted(circuit_sizes, reverse=True)
  print(sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2])

weights = q.PriorityQueue()
for i in range(len(locations)-1):
  for j in range(i+1, len(locations)):
    weights.put((get_distance(locations[i], locations[j]), [locations[i], locations[j]]))

i = 0
while not weights.empty():
  # part a
  if i == 1000:
    print_top_circuits()

  w = weights.get()
  pair = w[1]
  if pair[0] not in rounds[pair[1]]:
    circuit = rounds[pair[0]].union(rounds[pair[1]])

    # part b
    if len(circuit) == len(locations):
      print(pair[0][0] * pair[1][0])
      break
    for c in circuit:
      rounds[c] = circuit

  i += 1

print(time.time() - start_time)