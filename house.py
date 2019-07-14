class House:
    house = []

    @classmethod
    def total_square_feet(cls):
        total = 0
        for room in cls.house:
            total += room.square_feet()
        return total

# name width length
    @classmethod
    def print_rooms_nicely(cls):
        for room in sorted(cls.house):
            print("{} is {}".format(room.name, room.square_feet()))


class Room:

    pass

    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    def __lt__(self, other):
        return self.square_feet() < other.square_feet()

    def __gt__(self, other):
        return self.square_feet() > other.square_feet()

    def __eq__(self, other):
        return self.square_feet() == other.square_feet()

    def square_feet(self):
        return self.width * self.length


kitchen = Room("kitchen", 10, 15)
livingroom = Room("livingroom", 15, 10)
bathroom = Room("bathroom", 10, 10)
closet = Room("closet", 5, 5)
basement = Room("basement", 10, 10)
#
House.house.append(closet)
House.house.append(kitchen)
House.house.append(bathroom)


# print(kitchen)
# print(House)
# print(House.house)
#
print(House.total_square_feet())
# print(House.print_rooms_nicely())
print(kitchen == livingroom)
# print(House)
# class Room:
#     pass
#
#     def __init__(self, name, width, height):
#         self.name = name
#         self.width = width
#         self.height = height
#
#
# kitchen = Room("kitchen", 23, 23)
# print(kitchen)
