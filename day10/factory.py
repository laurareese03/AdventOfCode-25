import time, re, numpy as np, random
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

# so, theoretically, we should only ever need to press any button once, right?
# which could make this something of a boolean satisfiability problem?

# it looks very similar to the old 463 SAT solver project, and looking back at
# old notes, i wonder if the WalkSAT algorithm could solve this.
# unfortunately, this means i have to read old java code i wrote in college and
# convert it into something legible here. oofda.

def get_best_button(buttons, expected, current):
  bulbs = -1
  best_button = None
  for button in buttons:
    for b in button:
      current[b] = not current[b]
    diff = (expected == current)
    unique, counts = np.unique(diff, return_counts=True)
    statements = dict(zip(unique, counts))
    if statements[True] > bulbs:
      bulbs = max(bulbs, statements[True])
      best_button = button
    for b in button:
      current[b] = not current[b]
  return best_button

for line in man:
  expected = np.array(line[0])
  current = np.array([0] * len(expected))
  buttons = line[1]

  diff = (expected == current)
  unique, counts = np.unique(diff, return_counts=True)
  statements = dict(zip(unique, counts))

  while statements[True] != len(expected):
    r = random.random()
    if r < .75: # random here
      button = random.choice(buttons)
      for b in button:
        current[b] = not current[b]

      diff = (expected == current)
      unique, counts = np.unique(diff, return_counts=True)
      statements = dict(zip(unique, counts))
    else: # non random here
      button = get_best_button(buttons, expected, current)
      for b in button:
        current[b] = not current[b]

      diff = (expected == current)
      unique, counts = np.unique(diff, return_counts=True)
      statements = dict(zip(unique, counts))
      print(expected, current,)
      print(button)
  print('------')