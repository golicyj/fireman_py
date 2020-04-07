class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        print(cls)

    @classmethod
    def gamer_from_string(cls, data_string):
       nickname, age, level, score = data_string.split(',')
       return cls(nickname, age, level, score)

    def __init__(self, nickname, age, level, score):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.score = score
        Gamer.active_gamers += 1

    def log_out(self):
        Gamer.active_gamers -= 1

    def get_nicname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score

    def is_adult(self):
        return self.age >= 18

    def get_adult_permission(self):
        if self.is_adult():
            print('You can go tu adult level')
        else:
            print('You cant go tu adult level')

#print(Gamer.active_gamers)
#gamer_1 = Gamer('darkmaSSter', 23, 489, 40000)
#print(Gamer.active_gamers)
#gamer_2 = Gamer('whitemaSSter', 12, 889, 160000)

#a = Gamer.gamer_from_string('Badb, 39, 12 lvl, 9999')
#b = Gamer.gamer_from_string('kukuha, 49, 12 lvl, 9999')

#print(a.get_age())
#print(a.get_level())

slowar = dict.fromkeys((1,2,3), ('apple'))
print(slowar)