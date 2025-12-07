import time, re
start_time = time.time()

lines = open('homework.txt').read().strip('\n').split('\n')

# part a
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

# oh my god.

# part b
# the thought here is that the operation is always in the same column as the leftmost digit
# theoretically, i'm gonna try to use this fact to split the columns so the whitespace is preserved

splits = re.findall(r"\+\s+|\*\s+", lines[-1])

# first, we segment the lines into their columns with whitespace
operands = []
operand_count = len(lines)-1
index = 0
for split in splits:
  holder = []
  for i in range(operand_count):
    holder.append(lines[i][index:index+len(split)-1])
  operands.append(holder)
  index += len(split)

# next, we create the new operands from the columns
# (more like NEST we create amiright)
equation_set = []
for i in range(len(operands)):
  equation = []
  for j in range(len(operands[i][0])-1,-1,-1):
    new_ints = [''] * len(operands[i])
    for k in range(len(operands[i])):
      new_ints[k] += operands[i][k][j]
    equation.append(int(''.join(new_ints)))
  equation.append(splits[i].strip())
  equation_set.append(equation)


# finally, we iterate each through each nested list
# and perform the operation, adding it to the mega total
mega_total = 0
for e in equation_set:
  total = 0 if e[-1] == '+' else 1
  for i in range(len(e)-1):
    if e[-1] == '+':
      total += e[i]
    else:
      total *= e[i]
  mega_total += total
print(mega_total)

print(time.time() - start_time)