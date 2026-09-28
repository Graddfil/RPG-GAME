import random
from items import *
from weapons import*
from potions import *
from armors import *





class Enemy:
    def __init__(self, name, hp, max_damage, min_damage, exp_drop, drop_table=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.max_damage = max_damage
        self.min_damage = min_damage
        self.exp_drop = exp_drop
        self.drop_table = drop_table if drop_table else []

    def get_drops(self):
        for item, drop_rate in self.drop_table:
            if random.random() <= drop_rate:
                drop_list = []
                drop_list.append(item.name)
                return drop_list
        return None

    def attack(self, target):
        damage = random.randint(self.min_damage, self.max_damage)
        print(f"\n{self.name} attacks {target.name}!")
        target.take_damage(damage)
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage\n")

    def is_alive(self):
        return self.hp > 0
    
    @classmethod
    def goblin(cls):
        drop_table = [(rusty_dagger, 1), (leather_vest, 1),(healing_potion,1)]
        return cls(name="Goblin", hp=50, min_damage = 7, max_damage = 17, exp_drop = 10, drop_table = drop_table)           
        
    @classmethod
    def orc(cls):
        drop_table = [(iron_sword, 1), (leather_vest, 1),(healing_potion, 1)]
        return cls(name="Orc", hp=65, min_damage=11, max_damage=21, exp_drop=15, drop_table=drop_table)
    
    @classmethod
    def lizardman(cls):
        drop_table = [(lumber_axe, 1), (leather_vest, 1),(big_potion, 1)]
        return cls(name="Lizardman", hp=75, min_damage=14, max_damage=24, exp_drop=20, drop_table=drop_table)
    
    @classmethod
    def wolf(cls):
        return cls(name="Wolf", hp=110, min_damage = 20, max_damage = 30, exp_drop = 30)
    
    @classmethod
    def ogre(cls):
        return cls(name="Ogre", hp=100, min_damage = 25, max_damage = 35, exp_drop = 35)
