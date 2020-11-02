# 3. Exercises with lists
list1 = [1, 3, 45, -7, 89, 3, 1, 12, 3, 3, 1, 3]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]

# a. eliminate all elements from list3
# list3.clear()

# b. eliminate all 3s from list1
print(list1)
while 3 in list1:
  list1.remove(3)
print(list1)

# c. sort list1 from the biggest number to the lowest
list1.sort(reverse=True)
print(list1)

# d. sort list2 without "Zz"
print(list2)
list2.pop()
list2.sort()
print(list2)

# e. make list3 in the reverse order
print(list3)
list3.reverse()
print(list3)

# f. eliminate last 3 elements from list 2, last element from list3 and last 2 elements from list1
i = 3
print(list2)
# while i > 0:
#   list2.pop()
#   i -= 1
# print(list2)

list2 = list2[:-2]
print(list2)

# g. how many "b" values are in list2
print(list2.count('b'))
