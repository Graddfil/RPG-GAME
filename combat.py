
import time


def combat(player, enemy):
    
    combat_result = None
    
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} HP: {player.hp} / {player.max_hp}")
        print(f"{enemy.name} HP: {enemy.hp} / {enemy.max_hp}\n")
        
        print("------------------------------------------------")
        combat_action = input("\n1 Attack \n2 Use item \n3 Run\n\n")
        print("\n------------------------------------------------")
        if combat_action == "1":
            player.attack(enemy)
            time.sleep(1)
            if enemy.is_alive():
                enemy.attack(player)
                time.sleep(1)
            else:
                combat_result = "won"
                
        elif combat_action == "2":
            potion_used = player.use_potion()
            if potion_used:
                enemy.attack(player)
                time.sleep(1)
            
            
        elif combat_action == "3":
            combat_result = "run"
            break
        
        else: 
            print(f"This was not option, lose 1 hp")
            player.hp -= 1
    
    if player.is_alive() and combat_result == "won":
        print(f"{player.name} defeated {enemy.name}")
        print(f"\n\nYou won!\nYou have {player.hp} hp\nEXP: {player.exp} / {player.exp_to_next_lvl}\n")
        player.gain_exp(enemy.exp_drop)
        dropped_items = enemy.get_drops()
        enemy.hp = enemy.max_hp
        if dropped_items:
            for item in dropped_items:
                print(f"\n{enemy.name} dropped {item.name}!")
                player.inventory.append(item)
            
    elif player.is_alive() and combat_result == "run":
        print(f"{player.name} run successfully")
        enemy.hp = enemy.max_hp
                
    else:
        combat_result = "died"
        print("DEBUG HP:", player.hp)
        print("DEBUG ALIVE:", player.is_alive())
        print("DEBUG RESULT:", combat_result)
        print(f"{enemy.name} defeated {player.name}")
        print("\nYou died. Game over")