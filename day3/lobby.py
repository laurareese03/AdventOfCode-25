import time
start_time = time.time()

ratings = open('joltage_ratings.txt').read().split('\n')

def get_tens_digit(rating):
  for i in range(9, 0, -1):
    ind = rating.find(str(i))
    if ind > -1 and ind != (len(rating)-1):
      return ind

def get_singles_digit(rating):
  for i in range(9, 0, -1):
    ind = rating.find(str(i))
    if ind > -1:
      return ind

count_a = 0
for rating in ratings:
  joltage = ''

  ind = get_tens_digit(rating)
  joltage += rating[ind]
  rating = rating[ind+1:]

  ind = get_singles_digit(rating)
  joltage += rating[ind]

  count_a += int(joltage)

print(count_a)
print(time.time()-start_time)