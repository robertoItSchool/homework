# make a public voting system
# there are 100 users who can vote (name0, name1, ..., name99)
# there are 4 parties which can be voted (party0, party1, party2, party3)
# register the votes in a file, w/o the user who voted
# register the users who voted in a file so a user can't vote 2 times

class User:
  def __init__(self, name):
    # save to object
    self.name = name

  def vote(self, party_id):
    if self.has_user_already_voted():
      return
    self.register_the_vote(party_id)
    self.register_to_users_who_voted()

  def has_user_already_voted(self):
    # create a File object, to read users.txt
    read_users = open('users.txt')
    # read the file with readlines(), receive a list with the strings from each line
    users_who_voted = read_users.readlines()
    has_user_already_voted = False
    # check if the user already voted
    if (self.name + "\n") in users_who_voted:
      print('User ' + self.name + ' has already voted')
      has_user_already_voted = True
    return has_user_already_voted

  def register_the_vote(self, party_id):
    # create a File object, to append the votes (write at the end)
    votes_file = open('votes.txt', 'a')
    # convert party_id to string and write it at the end of the file
    votes_file.write(str(party_id) + "\n")
    # close the file
    votes_file.close()

  def register_to_users_who_voted(self):
    # create a File object to write the users who voted
    users_file = open('users.txt', 'a')
    # write the name of the user
    users_file.write(self.name + "\n")
    # close the file
    users_file.close()


class Party:
  def __init__(self, id):
    # save to object
    self.id = id


list_parties = [Party(0), Party(1), Party(2), Party(3)]
list_users = []
# range(0, 99) = [0, 1, 2, 3, ..., 99]
for i in range(0, 99):
  # concatenate/glue together the string name with i converted to string
  new_user = User('name' + str(i))
  # add the User object to the list
  list_users.append(new_user)

# test the vote
list_users[50].vote(0)
list_users[51].vote(1)
list_users[52].vote(2)
