def super(list):
    odd_sum = 0
    for num in list:
        if num % 2 == 1:
            odd_sum += num

    return odd_sum

def name(list):
    user = input("Give me name")
    for name in list:
        if (user == name):
            return "uau"
        else:
            return "Who goes there"

userNumber = input('Give me an integer number: ')
print(name(["Dan", "Alb"]))
print(super([1,2,3,4,5]))
