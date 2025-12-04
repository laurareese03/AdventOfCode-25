import time
start_time = time.time()

ratings = open('joltage_ratings.txt').read().split('\n')

def get_next_highest_digit(rating, length):
  for i in range(9, 0 , -1):
    ind = rating[:length].find(str(i))
    if ind > -1:
      return ind
    
def calculate_joltage(rating, length):
    joltage = ''
    while len(joltage) < length:
      ind = get_next_highest_digit(rating, len(rating) - (length-len(joltage)) +1)
      joltage += str(rating[ind])
      rating = rating[ind+1:]
    return int(joltage)

count_a, count_b = 0, 0
for rating in ratings:
  count_a += calculate_joltage(rating, 2)
  count_b += calculate_joltage(rating, 12)

print(count_a)
print(count_b)
print(time.time()-start_time)