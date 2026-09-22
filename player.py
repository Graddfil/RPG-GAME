import random
from items import *


# PLAYER
 
class Player:
    #define stats
    def __init__(self,player_class, name, level=1, ):
        self.player_class = player_class
        self.name = name
        self.level = level
        self.exp = 0
        self.exp_to_next_lvl = 50
        self.hp = player_class.hp
        self.max_hp = player_class.max_hp
        self.min_damage = player_class.min_damage
        self.max_damage = player_class.max_damage
        self.gold = 0
        self.equipped_weapon = None
        self.equipped_armor = None
        self.inventory = []
    
     #exp counter
    def gain_exp(self, amount):
        self.exp += amount
        print(f"\n{self.name} gains {amount} EXP!\n Total EXP: {self.exp} / {self.exp_to_next_lvl}")
        while self.exp >= self.exp_to_next_lvl:
            self.level_up()

    #Levelup
    def level_up(self):
        # if self.level < 10: # levelcap
        self.level += 1
        self.exp -= self.exp_to_next_lvl
        self.exp_to_next_lvl = int(self.exp_to_next_lvl * 1.5)
        self.max_hp += 10
        self.min_damage += 5
        self.max_damage += 5
        self.hp = self.max_hp # to heal full on lvl
        print(f"\n{self.name} leveled upt to {self.level}!\n")
    
    # Use potion
    def use_potion(self):
        potion_used = False
        for item in self.inventory:
            if isinstance(item, Potion):
                heal_amount = min(self.max_hp - self.hp, item.heal_amount)  # Heal for 20 HP, or the amount needed to max HP
                self.hp += heal_amount
                self.inventory.remove(item)
                print(f"{self.name} uses a potion and heals for {item.heal_amount} HP. Potions left: {len(self.inventory)}.")
                print(f"{self.name} now has {self.hp}/{self.max_hp} HP.\n")
                potion_used = True
                break
            else:
                print(f"{self.name} has no potions left!")
        return potion_used
        
    #gear
    def equip_gear(self, item):
        if item in self.inventory:
            if isinstance(item, Weapon):
                if self.equipped_weapon is not None:
                    self.inventory.append(self.equipped_weapon)
                    self.equipped_weapon = item
                    self.inventory.remove(item)
                    print(f"You are now using {self.equipped_weapon.name}")
                else:
                    self.equipped_weapon = item
                    self.inventory.remove(item)
                    print(f"You are now using {self.equipped_weapon.name}")
                    
            elif isinstance(item, Armor):
                if self.equipped_weapon is not None:
                    self.inventory.append(self.equipped_armor)
                    self.equipped_armor = item
                    self.inventory.remove(item)
                    print(f"You are now using {self.equipped_armor.name}")
                else:
                    self.equipped_armor = item
                    self.inventory.remove(item)
                    print(f"You are now using {self.equipped_armor.name}")
    
    def remove_gear(self):
        if isinstance(Weapon):
            if self.equipped_weapon is not None:
                self.inventory.append(self.equipped_weapon)
                self.equipped_weapon = None
                print(f"You are now using fists")
            else:
                self.equipped_weapon = None
                print(f"You dont have weapon")
                
        elif isinstance(Armor):
            if self.equipped_armor is not None:
                self.inventory.append(self.equipped_armor)
                self.equipped_armor = None
                print(f"You are now without armor")
            else:
                self.equipped_armor = None
                print(f"You dont have armor")
                    
    def show_inventory(self):
        if not self.inventory:
            print("Inventory is empty")
        
        else:
            for i, item in enumerate(self.inventory, start=1):
                print(f"You have:\n{i}, {item.name}")
                 
    #combat
    def attack(self, target):
        if self.equipped_weapon is None:
            damage = random.randint(self.min_damage, self.max_damage)
        else:
            weapon_bonus = self.equipped_weapon.damage_bonus
            damage = weapon_bonus + random.randint(self.min_damage, self.max_damage)
        print(f"\n{self.name} attacks {target.name}!")
        target.take_damage(damage)
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage\n")

    def is_alive(self):
        return self.hp > 0
    
    
