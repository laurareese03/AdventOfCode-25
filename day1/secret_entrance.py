turns = open('input.txt').read().splitlines()

pointer = 50
counter_a, counter_b = 0, 0

for turn in turns:
  direction = turn[0]
  spin = int(turn[1:])

  if spin > 99:
    old_spin = spin
    counter_b += (spin//100)
    spin = spin % 100

  old_pointer = pointer

  if direction == 'L':
    pointer -= spin
  else:
    pointer += spin

  if pointer == 0 or ((pointer % 100) != pointer and old_pointer != 0): # clunky :/
    counter_b += 1

  pointer %= 100

  if pointer == 0:
    counter_a += 1

print(counter_a, counter_b)