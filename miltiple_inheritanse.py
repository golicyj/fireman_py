class Swimmible:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello, my name is {self.name} I can swim!')


class Walkable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello, my name is {self.name} I can walk!')

class Flyeble:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello, my name is {self.name} I can fly!')

class GameCharacter(Swimmible, Walkable, Flyeble):
    def __init__(self, name):
        self.name = name
        Swimmible.__init__(self, name)
        Walkable.__init__(self, name)
        Flyeble.__init__(self, name)

    #def greeting(self):
        #print(f'Hello, my name is {self.name}')


ryba = GameCharacter('James')
ryba.greeting()