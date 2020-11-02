# 2. What values should x,y have so the following if statements are True? What about False?

x = 7
a = x > 6 and x < 12
print(a)

x = 13
a = x > 6 and x < 12
print(a)

y = 11
b = x > 10 or y > 10
print(b)

x = 9
y = 10
b = x > 10 or y > 10
print(b)

x = 10
c = x < 9 or True
print(c)

y = 100
d = y > 99 and False
print(d)

x = 11
e = x > 10 and x < 10
print(e)

x = False
f = not x
print(f)

x = 10
g = x > 10 or x < 10
print(g)

x = 15
y = 90
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)
