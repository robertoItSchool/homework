# 1. Find all numbers between 2000 and 3200 which are divisible by 7 but are not a multiple of 5

i = 2000
list = []
while i < 3200:
  if i % 7 == 0 and i % 5 != 0:
      list.append(i)
  i += 1

print(list)




