class MyClass:
    pass

num_class = MyClass()
#print(type(num_class))

class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed, ):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        print(self.name + 'car is driving to ' + city)

mazda_car = Car(name = 'bmw x7', year = '2020', color = 'red', is_crashed=False)

cars_wheels_of_three = Car.wheels_number * 3
#print(cars_wheels_of_three)

opel_car = Car('Opel Tigra', 'graey', '2000', True)


class Circle:
    pi = 3.1415

    def __init__(self, radius = 1):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_ference(self):
        return 2 * self.pi *self.radius


circle1 = Circle(3)
print(circle1.get_area())
print(circle1.get_ference())