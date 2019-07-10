class Position:
    ''' Help me please '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def move_north(self):
        self.y += 1

    def move_south(self):
        self.y -= 1

    def move_east(self):
        self.x += 1

    def move_west(self):
        self.x -= 1

class Person:
    ''' Help  '''

    def __init__(self, fname, lname, x=0, y=0):
        self.first_name = fname
        self.last_name = lname
        self.position = Position(x, y)

    def __str__(self):
        return "Person Object: {} position at {}".format(self.full_name(), self.position)

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def move(self, directions):
        for direction in directions:
            if direction == 'N':
                self.position.move_north()
            elif direction == 'S':
                self.position.move_south()
            elif direction == 'E':
                self.position.move_east()
            elif direction == 'S':
                self.position.move_west()

daniel = Person("Daniel", "Ang")
daniel.x_position = 20
# print(daniel)
daniel.move(['N', 'E', 'E', 'E', 'E', 'E'])
print(daniel)
# daniel.first_name = "Daniel"
# daniel.last_name = "Ang"
# print(daniel)
# print(daniel.first_name)
# print(type(daniel))
