# 3. Generate the first 30 numbers of the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers. First 2 numbers are 0 and 1, after that list[x] = list[x-1] + list[x-2]
# The result should be this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

x = input('How many numbers? ')

list = [0, 1]
while len(list) < int(x):
  new = list[len(list) - 1] + list[len(list) - 2]
  list.append(new)

print(list)

