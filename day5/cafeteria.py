import time
start_time = time.time()

ranges, ids = open('ingredient_ids_and_ranges.txt').read().split('\n\n')
ranges = [ r.split('-') for r in ranges.split('\n')]
ingredient_ids = ids.split('\n')

# part a
fresh_count = 0
for ingredient in ingredient_ids:
  for r in ranges:
    if int(ingredient) >= int(r[0]) and int(ingredient) <= int(r[1]):
      fresh_count += 1
      break
  
print(fresh_count)