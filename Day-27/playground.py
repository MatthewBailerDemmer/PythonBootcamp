# *args => function can receive a unlimited number of arguments
# comes as a tuple
def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6))

#**kwargs -> Key Word Arguments, unlimited too
# comes as a dictionary

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key),
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        # This way if we don´t pass the arguments make and model it´s gonna give us an error
        # self.make = kw["make"]
        # self.model = kw["model"]
        # The function get turns a empty argument into a null, preventing erros
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)