from it_team_solution import Name
from skill import BackendSkill

class Dev:
  def __init__(self, name, experience, backend_skill):
    self.name = name
    self.experience = experience
    self.backend_skill = backend_skill


class JuniorDev(Dev):
  def __init__(self, name, experience, backend_skill):
    if 0 <= experience <= 2:
      # if the condition is met, build the object
      super().__init__(name, experience, backend_skill)
    else:
      # if not, stop the program
      raise Exception('xp should be between 0 and 2')


class BackendJuniorDev(JuniorDev):
  def __init__(self, name, experience, backend_skill: BackendSkill):
    if backend_skill.rating > 5:
      super().__init__(name, experience, backend_skill)
    else:
      raise Exception('skill should be higher')

  def show(self):
    self.name.show()
    self.backend_skill.show()


jr = BackendJuniorDev(Name('First', 'Last'), 2, BackendSkill(6))
jr.show()

