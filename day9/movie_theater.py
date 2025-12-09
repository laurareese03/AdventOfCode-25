import time, math
start_time = time.time()

tiles = open('tile_locations.txt').read().strip().split('\n')
tiles = [tuple(map(int, t.split(','))) for t in tiles]

max_size = -1
for i in range(len(tiles)-1):
  for j in range(i+1, len(tiles)):
    a = tiles[i]
    b = tiles[j]
    max_size = max(max_size, (abs(a[0]-b[0])+1)*(abs(b[1]-a[1])+1))

print(max_size)