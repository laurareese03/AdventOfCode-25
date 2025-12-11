import time, re, numpy as np, queue as q
start_time = time.time()

manual = open('manual.txt').read().strip().split('\n')

# why did that dog have to eat the manual i'm having a crisis here
# "this is why he has behavioral issues. no boundries."
man = []
for m in manual:
  diagram = re.match(r'\[.*\]', m).group(0)
  diagram = [ 1 if bulb == '#' else 0 for bulb in diagram[1:-1]]

  wirings = re.search(r'\(.*\)', m).group(0).split(' ')
  wirings = [ [int(i) for i in w[1:-1].split(',')] for w in wirings]

  # "joltage doesn't matter" hmmmmm. that's suspicious. that's weird.
  joltage_requirements = re.search(r'{.*}', m).group(0) 
  man.append([diagram, wirings, joltage_requirements])

def get_sorted_bins(i):
  sorted_bins = q.PriorityQueue()
  for i in range(2**i):
    sorted_bins.put((str(bin(i)).count('1'), bin(i)))
  return sorted_bins

# oh this code is UGLY ugly
count = 0
for line in man:
  expected = line[0]
  buttons = line[1]

  bins = get_sorted_bins(len(buttons))
  while not bins.empty():
    current = [0] * len(expected)
    c, toggles = bins.get()
    toggles = toggles[2:]
    if len(toggles) != len(buttons):
      toggles = ((len(buttons)-len(toggles)) * '0') + toggles

    toggles = [int(i) for i in toggles]
    for i in range(len(toggles)):
      if toggles[i]:
        b = buttons[i]
        for j in b:
          current[j] = not current[j]
    if current == expected:
      count += c
      break

print(count)