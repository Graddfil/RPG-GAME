class Potion:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount
        
class Weapon:
    def __init__(self, name, damage_bonus, price):
        self.name = name
        self.damage_bonus = damage_bonus
        self.price = price

class Armor:
    def __init__(self, name, damage_reduction, price):
        self.name = name
        self.damage_reudction = damage_reduction
        self.price = price