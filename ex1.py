# 1. Are the following if statements True or False:
if True and False:
  print('it is false')
else:
  print('we are in else')


if False or True:
  print('this will always be true')
else:
  print('will not be reached')


x = 10 >= 10 and 67 > 66
print('ex 3 = ')
print(x)

d = 10 < 10 and 10 >= 9
print(d)


e = -1 < -2 or -2 > -1
print(e)


f = True or False and True
print(f)

g = True and False or False and True
print(g)

h = not True and not False
print(h)

i = not True or True
print(i)

j = False and not False
print(j)