# RPG GAEM

import random
from items import *
from player import Player
from classes import *
from enemy import Enemy
from combat import combat
from hub import hub
from weapons import *

print("")
print("")
print("HELLO ADVENTURER")
print("WELCOME TO SHITTY GAME")
print("YOU WILL NOT SURVIVE")
print("YOU WILL DIE")
print("")
print("")

#CHARACTER CREATION

player_name = input("Enter you name: ")
player_choice = input(f"Choose class: 1. Warrior | 2. Mage\n")

def choice(player_choice):
    if player_choice == "1":
        player_choice = Warrior()
        return player_choice
    elif player_choice == "2":
        player_choice = Mage()
        return player_choice
    else:
        player_choice = Beggar()
        return player_choice
        
player_class = choice(player_choice)


def main():
    
    game = True
    
    player = Player(player_class, player_name)
    #player.inventory.append(lumber_axe)
    #player.inventory.append(steel_sword)

    #item = Item()
    enemies = [Enemy.goblin(),
               Enemy.orc(),
               Enemy.lizardman(),]
    
    
    
    print(f"\nWelcome {player.name}\nYour choice was {player_class.__class__.__name__}\nThis gives you:\n{player.hp} hp\n{player.min_damage} to {player.max_damage} damage\nGood luck!")

    new_enemies = False
    while game:
        action = hub(player)
        if action == "combat":
        
            while player.is_alive():
                
                if new_enemies == False and player.level == 5:
                    new_enemies = True
                    enemies.append(Enemy.wolf())
                    enemies.append(Enemy.ogre())  
                                
                enemy = random.choice(enemies)

                
                print("============================")
                print(f"\nA wild {enemy.name} appears!\n")
                print("============================")
                
                combat(player, enemy)
                
                if player.is_alive():
                    action = input("\n1 Keep fighting\n2 Run\n")
                    if action == "2":
                        print("You went home")
                        break
        
        elif action == "inventory":
            if not player.inventory:
                player.show_inventory()
            else:
                player.show_inventory()
                equip_choice = input("Do you want to equip item?\n1. Yes\n2. No")
                if equip_choice == "1":
                    item_choice = int(input("What item number?"))
                    final = player.inventory[item_choice - 1]
                    if item_choice not in player.inventory:
                        print("Invalid choice")
                    player.equip_gear(final)
            
            
        
        elif action == "shop":
            pass

        elif action == "quit":
            break            
        
                
    
if __name__ == "__main__":
    main()
            
        