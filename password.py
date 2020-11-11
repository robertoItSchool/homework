class Password:
  def __init__(self, password):
    self.__password = password

  #create tests for all strength levels
  def strength_level(self):
    length = len(self.__password)
    if length < 10:
      return 0
    elif length < 20:
      return 1
    else:
      return 2

# change strength levels to 4
# 1st level < 8
# 2nd level < 16
# 3rd level < 24
# 4th level > 24
# update tests for this method