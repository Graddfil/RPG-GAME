from player import Player







def hub(player):
    
    print("----------------------------------------\n")
    print("WELCOME TO TOWN")
    print("----------------------------------------\n")

    if player.hp > player.max_hp:
        player.hp = player.max_hp
        print(f"You feel refreshed and heal {player.hp}/{player.max_hp}")

    action = None
    player_choice = input(f"1. Enter combat\n2. Shop\n3. Inventory\n4. Quit game\n\n")
    
    if player_choice == "1":
        action = "combat"
        return action
    
    elif player_choice == "2":
        action = "shop"
        return action
    
    elif player_choice == "3":
        action = "inventory"
        return action
    
    elif player_choice == "4":
        action = "quit"
        return action
    else:
        print("Ei ollut vaihtoehto")