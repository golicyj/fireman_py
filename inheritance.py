class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created')

    def drive(self, city):
        print(self.name + 'car is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color
        print('Color is changed' + new_color)

class Truck(Car):
    wheels_number = 6
    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print('Truck is created')

    def drive(self, city):
        print('Truck ' + self.name + ' is driving to ' + city)

    def load_cargo(self, weight):
        print('Cargo is loaded ' + str(weight) + ' kg')


man_Truck = Truck('Man', 'white', 2020, False)

man_Truck.drive('London')
print(man_Truck.wheels_number)
print(man_Truck.color)
man_Truck.change_color('red')
print(man_Truck.color)
man_Truck.load_cargo(2000)

#polymorphism (mnogo + form)

