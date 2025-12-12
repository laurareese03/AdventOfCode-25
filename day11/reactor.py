import time, re, queue as q
start_time = time.time()

devices = open('devices.txt').read().strip().split('\n')

device_map = {}
for device in devices:
  d, outputs = re.match(r'(.*): (.*)', device).groups()
  device_map[d] = outputs.split(' ')

def dfs(current, success, failure):
  if current in visited:
    return visited[current]
  if current == success:
    return 1
  if current in failure:
    return 0
  visited[current] = 0 
  for next in device_map[current]:
    visited[current] += dfs(next, success, failure)
  return visited[current]

# part a
count = 0
frontier = q.Queue()
frontier.put('you')
while not frontier.empty():
  current = frontier.get()
  if current == 'out':
    count += 1
  else:
    for f in device_map[current]:
      frontier.put(f)
print(count)

# part b
# i love the advent of code but i HATE when the advent of code makes me write
# search algorithms recursively.

# the thought here at least (that does work) is we count the number of paths between
# dac and out, then the number of paths between fft and dac, and finally the number
# of paths between svr and fft, then multiply the three values together to get the solution
visited = {}
a = dfs('dac', 'out', [])
visited = {}
b = dfs('fft', 'dac', ['out'])
visited = {}
c = dfs('svr', 'fft', ['dac', 'out'])
print(a*b*c)