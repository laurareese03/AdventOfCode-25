import textwrap, time
start_time = time.time()

id_ranges = open('product_ids.txt').read().replace('\n', '').split(',')

coprime_factors = {
  1: [],
  2: [1],
  3: [1],
  4: [2],
  5: [1],
  6: [2,3],
  7: [1],
  8: [4],
  9: [3],
  10: [2, 5]
}

count_a, count_b = 0, 0 
for id_range in id_ranges:
  r = id_range.split('-')
  for i in range(int(r[0]), int(r[1])+1):
    # part a
    i = str(i)
    if i[len(i)//2:] == i[:len(i)//2]:
      count_a += int(i)
    
    # part b
    # chunk the id into equal length strings and check if all are the same
    # I wonder how much faster I can make it without checking the 1 factor
    # (dropped from 67s to 41s to 31s only checking needed duplicates)
    for j in coprime_factors[len(i)]:
      holder = textwrap.wrap(i, j)
      if len(set(holder)) == 1:
        count_b += int(i)
        break

print(count_a)
print(count_b)
print(time.time()-start_time)