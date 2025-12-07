import time, numpy as np
start_time = time.time()

lines = open('homework.txt').read().strip().split('\n')

operands = [''] * len(lines)
for i in range(len(lines)):
  operands[i] = lines[i].split()

mega_total = 0
for i in range(len(operands[i])):
  problem_total = 0
  operation = operands[-1][i]
  problem_total = 0 if operation == '+' else 1
  for j in range(len(operands)-1):
    if operation == '*':
      problem_total *= int(operands[j][i])
    else:
      problem_total += int(operands[j][i])
  mega_total += problem_total

print(mega_total)