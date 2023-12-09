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

hero = SuperHero("Uzumaki Naruto", "Naruto", "Rassengan", 100, "I win")
hero.display_name()
hero.double_health()
print(hero)
print(f"Lenght of catchphrase:",
len(hero.catchphrase))