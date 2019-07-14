import pdb

# ipdb_set_trace()


class Vampire:

    """pass"""

    coven = []
    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(vampire)
        return vampire

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today


vamp1 = Vampire.create("piglet", 27, False, False)
print(vamp1)
