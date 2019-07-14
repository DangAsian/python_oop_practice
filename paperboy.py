import pdb

class Paperboy:
    """mailing game"""

    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    #deliver 50 << quota initially
    #quota calc 1/2 of your exp + minimum

    def __str__(self):
        return "{} has this much exp: {} and has earned {}".format(self.name, self.experience, self.earnings)


    def quota(self):
        if self.experience == 0:
            quota = 50
            return quota

    def deliver(self, start, end):
        num = end - start + 1
        self.experience += num
        if num < 50:
            self.earnings += num * 0.25

        if num > 50:
            self.earnings += 50 * 0.25
            self.earnings += (num - 50) * 0.5

        pdb.set_trace()
    def report(self):
        return "I'm {}, and I delivered {} papers and I've earned {}".format(self.name, self.experience, self.earnings)



daniel = Paperboy("Daniel")
print(daniel)
print(daniel.deliver(101, 160))
print(daniel.deliver(101, 160))
print(daniel.earnings)
# print(daniel.deliver(100, 120))
print(daniel.report())
