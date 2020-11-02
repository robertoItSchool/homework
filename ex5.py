import random

while True:
  computer_guess = random.choice(["piatra", "foarfece", "hartie"])
  user_guess = input("Pick piatra, foarfece or hartie\n")
  user_guess = user_guess.strip().lower()
  if user_guess == "stop":
    break
  if user_guess == computer_guess:
    print('you are equals')
  elif user_guess == "piatra":
    if computer_guess == "foarfece":
      print('you won')
    else:
      print('you lost')
  elif user_guess == "foarfece":
    if computer_guess == "piatra":
      print("you lost")
    else:
      print('you won')
  elif user_guess == "hartie":
    if computer_guess == "piatra":
      print("you won")
    else:
      print('you lost')
  else:
    print('please choose a valid option')

