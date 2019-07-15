class System:
    pass

    systems = []

    @classmethod
    def total_system_mass(cls):
        total_mass = 0
        for system in cls.systems:
            for body in system.bodies:
                total_mass += body.mass
        return total_mass


    def __init__(self, bodies=[]):
        self.bodies = bodies
        System.systems.append(self)

    def add(self, body):
        in_list = False

        for i in self.bodies:
            if i == body:
                in_list = True
        if in_list is False:
            self.bodies.append(body)
            return "Added!"
        else:
            return "Nope!!!"

    def total_mass(self):
        total = 0
        for body in self.bodies:
            total += body.mass
        return total


class Body:
    pass

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


class Planet(Body):
    pass

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

    def __str__(self):
        return "{}".format(self.name)

    def all(self, system):
        planet = []
        for body in system.bodies:
            if type(body).__name__ == "Planet":
                planet.append(body)
        return planet


class Star(Body):
    pass

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

    def add(self, system):
        star = []
        for body in system.bodies:
            if type(body).__name__ == "Star":
                star.append(body)
        return star


class Moon(Body):
    pass

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet


planet = Planet("Mars", 22, 20, 20)
star = Star("Sun", 22, "blue")
moon = Moon("Moon", 22, 12, "blue")
# print(planet)

system = System()
system1 = System()
print(system.add(planet))
print(system.add(star))
print(system1.add(star))
print(system.add(star))
# print(system.add(star))
print(system.add(moon))
# print(planet.all(system))
# print(system.bodies)
# print(system.total_mass())
print(System.total_system_mass())
