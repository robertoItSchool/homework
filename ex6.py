# 6. Make a game in which the user has to guess a number between 100 and 199.
#    If the user types 'stop', even with whitespaces or some uppercase letters, the game stops.
#    If the user's number is not between 100 and 199, inform him.
#    If the user does not enter a number, inform him.
import random

list = []
i = 100
while i < 199:
  list.append(i)
  i += 1
while True:
  computer_guess = random.choice(list)
  x = input('Guess a number between 100 and 199\n')
  x = x.strip().lower()
  if x == 'stop':
    break
  if x.isdigit():
    x_as_int = int(x)
    if x_as_int > 100 and x_as_int < 199:
      if computer_guess == x:
        print('you won')
      else:
        print('you lost, computer chose ' + str(computer_guess))
    else:
      print('please give a number beween 100 and 199')
  else:
    print('please give a number')