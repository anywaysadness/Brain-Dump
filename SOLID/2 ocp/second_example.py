class Attacker:
    """Интерфейс для атакующих классов."""
    def attack(): 
        raise NotImplementedError


class Weapon(Attacker):
    """Задает общую структуру орудий."""
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage


class Sword(Weapon):
    """
    Наследует структуру орудия и реализует интерфейс для атаки.
    """
    def attack(self):
        print(f"{self.name} наносит удар: -{self.damage} hp")


class Bow(Weapon):
    """
    Наследует структуру орудия и реализует интерфейс для стрельбы.
    """
    def attack(self):
        print(f"{self.name} стреляет: -{self.damage} hp")
        
class Character:
    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()

sword = Sword("Needle", 24, 3)
bow = Bow("Twig", 30, 100)
aria = Character("Aria", sword)

aria.attack() # Output: Needle наносит удар: -24 hp
aria.change_weapon(bow)

aria.attack() # Output: Twig стреляет: -30 hp