# 2. Draw a game board with the size given by the user. If the user says 3 and 4, it should look like this
#  --- --- --- ---
# |   |   |   |   |
#  --- --- --- ---
# |   |   |   |   |
#  --- --- --- ---
# |   |   |   |   |
#  --- --- --- ---

x = input('Give the row number: ')
y = input('Give the column number: ')

top = ' ---'
side = '|   '

i = 0
while i < int(x):
  print(top * int(y))
  print(side * int(y) + '|')
  i += 1
print(top * int(y))

