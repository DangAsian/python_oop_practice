emotions = {
	'Happiness': 3,
	"Fear": 1,
	"Saddness": 2
}

class Person:
    """Person class"""

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def feeling_moment(self):
        for i in emotions:
            if emotions[i] == 3:
                print("{} is feeling a high amount of {}".format(self.name, i))
            elif emotions[i] == 2:
                print("{} is feeling a medium amount of {}".format(self.name, i))
            elif emotions[i] == 1:
                print("{} is feeling a low amount of {}".format(self.name, i))

    # def __str__(self):
    #     return "{} is feeling a high amount of {}.".format(self.name, self.emotions)

human = Person("Daniel", emotions)
print(human.feeling_moment())
