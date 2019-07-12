import random

class Zombie:

  max_speed = 5
  max_strength = 8
  horde = []
  plague_level = 10
  default_speed = 1
  default_strength = 3

  def __init__(self, speed=1, strength=3):
    """Initializes zombie's speed
        Initializes zombie's strength
    """
    if speed > Zombie.max_speed:
      self.speed = Zombie.default_speed
    else:
        self.speed = speed

    if strength > Zombie.max_strength:
        self.strength = Zombie.default_strength
    else:
        self.strength = strength



  def __str__(self):
     return "Zombie speed: {}".format(self.speed)
  def __repr__(self):
     return "Zombie speed: {}".format(self.speed)

  @classmethod
  def spawn(cls):
    """Spawns a random number of new zombies, based on the plague level,
    adding each one to the horde.  Each zombie gets a random speed.
    """
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
      speed = random.randint(1, Zombie.max_speed)
      Zombie.horde.append(Zombie(speed))
      count += 1

  @classmethod
  def new_day(cls):
    """Represents the events of yet another day of the zombie apocalypse.
    Every day some zombies die off (phew!), some new ones show up,
    and sometimes the zombie plague level increases.
    """
    Zombie.spawn()
    Zombie.some_die_off()
    Zombie.increase_plague_level()

  @classmethod
  def some_die_off(cls):
    """Removes a random number (between 0 and 10) of zombies from the horde.
    """
    how_many_die = random.randint(0, 10)
    counter = 0
    while counter < how_many_die and len(Zombie.horde) > 0:
      random_zombie = random.randint(0,len(Zombie.horde) - 1)
      Zombie.horde.pop(random_zombie)
      counter += 1

  @classmethod
  def increase_plague_level:
      rate = random.randint(0, 2)
      Zombie.plauge_level += rate

  def encounter(self):
    """This instance method represents you coming across a zombie! This can end in two possible outcomes:
    1. You outrun the zombie and escape unscathed!
    2. You don't outrun the zombie. It eats your brains and you die. :(
    Returns a summary of what happened.
    """
    outrun = self.chase()

    if outrun:
      return 'You escaped!'
    else:
      fight = self.fight()
      if fight:
          zombieSelf = Zombie()
          Zombie.horde.append(zombieSelf)
          return ("BASlasjggggggggggaljfaks")
      else:
          return "You died"


      return 'You died.'

  def chase(self):
    """Represents you trying to outrun this particular zombie.
    Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
    """
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed

  def fight(self):
    your_strength = random.randint(1, Zombie.max_strength)
    return your_strength > self.strength

zombie1 = Zombie(2)
print(zombie1)
print(Zombie)
print(Zombie.spawn())
print(Zombie.horde)
print(Zombie.new_day())
print(Zombie.horde)
print(zombie1.encounter())
