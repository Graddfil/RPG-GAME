#CHARACTER CLASS

class Warrior:
    #define stats
    def __init__(self, hp=120, min_damage=15,max_damage=20):
        
        self.hp = hp
        self.max_hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage
        
class Mage:
    #define stats
    def __init__(self, hp=90, min_damage=250,max_damage=300):
        
        self.hp = hp
        self.max_hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage

class Beggar:
    #define stats
    def __init__(self, hp=10, min_damage=1,max_damage=1):
        
        self.hp = hp
        self.max_hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage