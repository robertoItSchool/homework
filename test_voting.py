import unittest
from voting import User
from unittest import mock


class TestVoting(unittest.TestCase):
  @mock.patch('voting.User.read_file', return_value=['name2\n'])
  def test_user_has_not_voted(self, read_file):
    # set up - made it manually
    # execution
    user = User('name1')
    has_voted = user.has_user_already_voted()
    # assertion
    self.assertFalse(has_voted)

  @mock.patch('voting.User.read_file', return_value=['name2\n'])
  def test_user_voted(self, read_file):
    # set up - made it manually: write name2 to users.txt
    # execution
    user = User('name2')
    has_voted = user.has_user_already_voted()
    # assertion
    self.assertTrue(has_voted)

  @mock.patch('voting.User.write_file')
  def test_vote_was_registered(self, write_file):
    # execution
    user = User('name2')
    user.register_the_vote(1)
    # assertion
    write_file.assert_called_once_with("1\n")


if __name__ == '__main__':
  unittest.main()
