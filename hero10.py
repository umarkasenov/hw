class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print(f"Hero`s name is {self.name}")

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return (f'Nickname: {self.name}, '
                f'Superpower: {self.superpower}, '
                f'Health {self.health_points}')

    def __len__(self):
        return len(self.catchphrase)

    def crit(self):
        self.damage **= 2


class Hero1(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase,  damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2

    def fly(self):
        self.fly = True

    def phrase(self):
        print("True in the True_phrase")


class Hero2(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase,  damage, fly=False):
        super().__init__ (name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2

    def enable_fly(self):
        self.fly = True

    def phrase(self):
        print("True in the True_phrase")


class Villain(Hero2):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self, other_hero):
        other_hero.damage **= 2



hero = SuperHero("Uzumaki Naruto", "Naruto", "Rassengan", 100, "I win")
hero.display_name()
hero.double_health()
print(hero)
print(f"Lenght of catchphrase:",hero.__len__())


hero2 = Hero2("Iron Man", "Tony Stark", "Powered Suit", 100, "I am Iron Man", damage=15, fly=True)
hero2.double_health()
print(hero2)
hero2.enable_fly()
print(f"{hero2.nickname} can fly: {hero2.fly}")
hero2.phrase()


hero1 = Hero1("Batman", "Bruce Wayne", "Martial Arts", 120, "I'm Batman!", damage=12, fly=True)
villain = Villain("Joker", "The Clown", "Chaos", 80, "Why so serious?", damage=10, fly=False)
print(hero1)
print(f"{hero1.nickname} belongs to the {hero1.people}")
villain.crit(hero1)
print(f"Hero's damage after crit: {hero1.damage}")