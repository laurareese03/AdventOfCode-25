import time
start_time = time.time()

ratings = open('joltage_ratings.txt').read().split('\n')

def get_next_highest_digit(rating, length):
  for i in range(9, 0 , -1):
    print(rating, rating[:length])
    ind = rating[:length].find(str(i))
    if ind > -1:
      return ind

count_a, count_b = 0, 0
for rating in ratings:
  joltage = ''

  while len(joltage) < 12:
    ind = get_next_highest_digit(rating, len(rating) - (12-len(joltage)) +1)
    joltage += str(rating[ind])
    rating = rating[ind+1:]

  count_b += int(joltage)

print(count_a)
print(count_b)
print(time.time()-start_time)