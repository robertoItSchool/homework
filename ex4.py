# 4. Exercises with dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 'A'}
#     a. remove last element
for key, value in dict1.items():
  try:
    int_value = int(value)
  except:
    continue
  if int_value > 2:
    print(key)

print(dict1)
dict1.popitem()
print(dict1)
#     b. print all keys for the values above 2
for key,value in dict1.items():
  if value > 2:
    print(key)

#     c. remove all keys for the values above 2
keys_to_be_removed = []
for key,value in dict1.items():
  if value > 2:
    keys_to_be_removed.append(key)

for key in keys_to_be_removed:
  dict1.pop(key)
print(dict1)

#     d. print all the values remaining
print(dict1.values())

#     e. remove all remaining elements from dict
dict1.clear()
print(dict1)