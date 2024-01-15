from human import Human
from robot import Robot


class Planet:
    def __init__(self, name):
        self.name = name
        self.inhabitants = {
            'humans': [],
            'robots': []
        }

    def add_human(self, human):
        self.inhabitants['humans'].append(human)

    def remove_human(self, human):
        self.inhabitants['humans'].remove(human)

    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)

    def remove_robot(self, robot):
        self.inhabitants['robots'].remove(robot)

    def __repr__(self):
        return f"planet({self.name}, humans={self.inhabitants['humans']}, robots= {self.inhabitants['robots']}"

    def __str__(self):
        return f"Planet {self.name} has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."


if __name__ == '__main__':
    planet = Planet("Earth")
    print(repr(planet))
    prins = Human("Prins")
    planet.add_human(prins)
    print(repr(planet))
    print(planet)