import random

def fill_output(n):

  out_list = []
  for i in range(n):
    out_list.append(random.randint(1, 9))
    print(out_list[i], end = ' ')

  print()
  
  rev_array = []
  while len(out_list) >= 1:
    j = out_list.pop()
    rev_array.append(j)

  for j in range(len(rev_array)):
    print(rev_array[j], end = ' ')
