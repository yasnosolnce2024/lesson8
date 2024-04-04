from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец не выбрал оружие для атаки."

class Monster:
    def __init__(self, name):
        self.name = name

def main():
    fighter = Fighter("Боец")
    sword = Sword()
    bow = Bow()

    weapons = [sword, bow]

    for weapon in weapons:
        print(f"Боец выбирает {weapon.__class__.__name__}.")
        fighter.change_weapon(weapon)
        print(fighter.attack())
        print("Монстр побежден!\n")

if __name__ == "__main__":
    main()
