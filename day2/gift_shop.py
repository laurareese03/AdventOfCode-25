import textwrap, time
start_time = time.time()

id_ranges = open('product_ids.txt').read().replace('\n', '').split(',')

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
    # (about 26 seconds, not awful)
    for j in range (1, (len(i)//2)+1):
      if len(i)%j == 0:
        # if j == 1 and i[0] != i[1]:
        #   continue
        holder = textwrap.wrap(i, j)
        if len(set(holder)) == 1:
          count_b += int(i)
          break

print(count_a)
print(count_b)
print(time.time()-start_time)