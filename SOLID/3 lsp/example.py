from dataclasses import dataclass


@dataclass
class Position:
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"({self.x}, {self.y})"

class Character:
    """Суперкласс персонажей."""
    def __init__(self, name: str):
        self.name = name
        self.position = Position()

    def move(self, destination: Position):
        print("{name} двигается с {start} на {end}".format(
            name=self.name, start=self.position, end=destination
        ))
        self.position = destination


class Human(Character):
    """Дочерний класс, соблюдающий логику родителя."""
    def move(self, destination: Position):
        print("{name} идёт с {start} на {end}".format(
            name=self.name, start=self.position, end=destination
        ))
        self.position = destination

    def buy(self):
        """Добавляет свою логику."""
        print("Купить предмет.")


class Dragon(Character):
    """Дочерний класс, соблюдающий логику родителя."""
    def move(self, destination: Position):
        print("{name} летит с {start} на {end}".format(
            name=self.name, start=self.position, end=destination
        ))
        self.position = destination

    def attack(self):
        """Добавляет свою логику."""
        print("Извернуть пламя на противника.")


def move(character: Character, destination: Position):
    """
    Клиент, который использует `Character` и его потомков,
    не замечая разницы.
    """
    character.move(destination)


spirit = Character("Spirit")
john = Human("John")
dragon = Dragon("Dragon")

meeting_point = Position(x=300, y=250)

move(spirit, meeting_point)
move(john, meeting_point)
move(dragon, meeting_point)

# Output:
# Spirit двигается с (0, 0) на (300, 250)
# John идёт с (0, 0) на (300, 250)
# Drogon летит с (0, 0) на (300, 250)