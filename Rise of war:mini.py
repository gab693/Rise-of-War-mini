import random
import time

print("welcome to Rise of War: Mini or for short RWM")
print("this is just a prototype and this is version 0.1 more updates in the future")
print("this is not ai generated I made the code myself")
print("credits to ai for helping me learn code")

player_hp = 50
enemy_hp = 50
turn = 0
heal_cooldown = 0

name = input("Enter your name: ")
print(f"Hello {name}, welcome to RWM!")

# Main game loop
while player_hp > 0 and enemy_hp > 0:
    print(f"\n--- Turn {turn + 1} ---")  # fixed the \n
    print(f"Your HP: {player_hp} | Enemy HP: {enemy_hp}")
    action = input("Do you attack or heal? ").lower()

    if action == "attack":
        dmg = random.randint(1, 10)
        crit = random.randint(1, 5)
        if crit == 1:
            dmg *= 2
            print(f"💥 Critical hit! You dealt {dmg} damage!")
        else:
            print(f"You did {dmg} damage!")
        enemy_hp -= dmg  # moved out so it works both for normal and crit attacks

    elif action == "heal":
        if heal_cooldown == 0:
            heal = random.randint(1, 10)
            player_hp += heal
            print(f"✨ You healed for {heal} HP!")
            heal_cooldown = 5
        else:
            print(f"You can’t heal yet! Wait {heal_cooldown} turns.")

    else:
        print("Invalid action! You stand still thinking what to do...")

    # Enemy counterattack
    if enemy_hp > 0:
        enemy_dmg = random.randint(4, 9)
        player_hp -= enemy_dmg
        print(f"The enemy hits you for {enemy_dmg} damage!")

    # Cooldown + turn counter
    if heal_cooldown > 0:
        heal_cooldown -= 1
    turn += 1

# End of battle
if player_hp > 0:
    print("\n🏆 You won! You defeated the enemy!")
else:
    print("\n☠️ We have lost a soldier... the enemy won.")
