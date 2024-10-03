import random


tank_defense = 51
tank_hp = 51
mage_intelligence = 51
mage_mana = 51
ninja_damage = 51
ninja_agility = 51

defense = 99
hp = 99
intelligence = 99
mana = 99
damage = 99
agility = 99

# Program to simulate the first mission of an RPG game
print("???? - Your adventure begins here!!!")
print("PERSIAN - Hello, my name is Persian. I am a great mage and will also be your advisor during your adventure!")
name = input("PERSIAN - First, tell me the name of your hero: ")
print("\n")

print(f"PERSIAN - Great, it's a pleasure to meet you {name}!")
print("PERSIAN - In this world, young adventurers can choose between three classes:")
print("PERSIAN - Tank, Mage, or Ninja.")
print()
print("PERSIAN - The tank class has increased defense and health, but less agility. They are the ones who can take a beating!")
print()
print("PERSIAN - Mages gain increased intelligence and mana, used in spells during battle, but they don't have great defense.")
print()
print("PERSIAN - Ninjas gain a great advantage in damage and agility, however, they have lower mana, which is important for healing.")
print()
print("1) Tank, 2) Mage, 3) Ninja")
class_choice = int(input("PERSIAN - Now it's your turn, which class do you want to choose?: "))

if class_choice == 1:
    print("PERSIAN - You chose tank, it seems you are strong!")
    defense += tank_defense
    hp += tank_hp
    agility -= 19
    intelligence += 1
    mana += 1
    damage += 1
elif class_choice == 2:
    print("PERSIAN - You chose mage, ready to cast spells?")
    defense -= 19
    hp += 1
    intelligence += mage_intelligence
    mana += mage_mana
    agility += 1
    damage += 1
elif class_choice == 3:
    print("PERSIAN - You chose ninja, be agile and stealthy!")
    hp += 1
    intelligence += 1
    mana -= 19
    damage += ninja_damage
    agility += ninja_agility
    defense += 1

print(f"PERSIAN - You have: {defense} defense points; {hp} health points; {intelligence} intelligence points; {mana} mana points; {damage} damage points; {agility} agility points.")
print()

print("PERSIAN - Before heading out on your first mission, you can choose one item from each category!")
print("PERSIAN - They are [Melee Weapon], [Armor], [Potions], and [Passive]")
weapon_list = [
    "Katana (+25 damage; -10 agility)",
    "Dual Daggers (+15 damage; +15 agility)",
    "Mace (+35 damage; -15 agility)",
    "Spear (+20 damage; -2 agility)"
]
print("Melee Weapon", weapon_list)
print()
print("1) Katana, 2) Dual Daggers, 3) Mace, 4) Spear.")
weapon = int(input("Choose the weapon you want [1], [2], [3], [4]: "))

if weapon == 1:
    damage += 25
    agility -= 10
    print("You chose Katana!")
elif weapon == 2:
    damage += 15
    agility += 15
    print("You chose Dual Daggers!")
elif weapon == 3:
    damage += 35
    agility -= 15
    print("You chose Mace!")
elif weapon == 4:
    damage += 20
    agility -= 2
    print("You chose Spear!")
print()

armor_list = [
    "Knight's Armor (+30 defense; -15 agility)",
    "Agility Cloak (+25 agility)",
    "Magic Bracelet (+20 mana; +5 agility)",
    "Attack Armor (+10 damage; -10 agility)"
]
print("Armor", armor_list)
print()
print("1) Knight's Armor, 2) Agility Cloak, 3) Magic Bracelet, 4) Attack Armor.")
armor = int(input("Choose the armor you want [1], [2], [3], [4]: "))

if armor == 1:
    defense += 30
    agility -= 15
    print("You chose Knight's Armor!")
elif armor == 2:
    agility += 25
    print("You chose Agility Cloak!")
elif armor == 3:
    mana += 20
    agility += 5
    print("You chose Magic Bracelet!")
elif armor == 4:
    damage += 10
    agility -= 10
    print("You chose Attack Armor!")
print()

potion_list = [
    "Healing Potion (+20 health)",
    "Speed Potion (+20 agility)",
    "Fury Potion (+20 damage)",
    "Mage Potion (+20 mana)"
]
print("Potion", potion_list)
print()
print("1) Healing Potion, 2) Speed Potion, 3) Fury Potion, 4) Mage Potion.")
potion = int(input("Choose the potion you want [1], [2], [3], [4]: "))

if potion == 1:
    hp += 20
    print("You chose Healing Potion!")
elif potion == 2:
    agility += 20
    print("You chose Speed Potion!")
elif potion == 3:
    damage += 20
    print("You chose Fury Potion!")
elif potion == 4:
    mana += 20
    print("You chose Mage Potion!")
print()

passive_list = [
    "Brawler's Will (+10 damage; +10 defense)",
    "Mage's Wisdom (+10 intelligence; +10 mana)",
    "The Swift (+20 agility)",
    "Fortified (+20 defense)"
]
print("Passive", passive_list)
print()
print("1) Brawler's Will, 2) Mage's Wisdom, 3) The Swift, 4) Fortified.")
passive = int(input("Choose the passive you want [1], [2], [3], [4]: "))

if passive == 1:
    damage += 10
    defense += 10
    print("You chose Brawler's Will!")
elif passive == 2:
    intelligence += 10
    mana += 10
    print("You chose Mage's Wisdom!")
elif passive == 3:
    agility += 20
    print("You chose The Swift!")
elif passive == 4:
    defense += 20
    print("You chose Fortified!")
print()

print(f"PERSIAN - Your final status is:")
print(f"Defense: {defense}, Health: {hp}, Intelligence: {intelligence}, Mana: {mana}, Damage: {damage}, Agility: {agility}")
print()

print(f"PERSIAN - Now {name}, you are ready for your first mission.")
print("PERSIAN - Go talk to my friend TYR at the tavern, he will instruct you further. See you later.")
print()
print(f"???? - Upon arriving at the tavern, {name} encounters a huge and drunk man.")
print()
print(f"TYR - Hello, you must be {name}, PERSIAN told me you would show up.")
print("TYR - I am a scientist and research monsters and DNA, aiming to tame monsters to help us in battle.")
print()
print("TYR - I need help with one of our dragon hatchlings.")
print("TYR - It was stolen by goblins who live in the evil forest, the little dragon is tame and scared, so help it.")
print()
print("MISSION 1 - Find and rescue the Dragon Hatchling.")
print("\n")

goblins_hp = 220
total_damage = 0
magic_attack = mana + intelligence
print(f"???? - Upon arriving at the evil forest, {name} encountered 3 small but cunning goblins...")
print("Goblins (220 health together.)")
print()

while hp > 0 and goblins_hp > 0:
    print("\nChoose your attack: ")
    print("1) Normal Attack (Requires 100 damage)")
    print("2) Magic Attack (Requires 110 mana and 110 intelligence)")
    print("3) Quick Attack (Requires 115 agility)")
    attack_choice = int(input("Which attack do you want to choose? "))

    if attack_choice == 1:
        total_damage = damage
        print(f"{name} chose Normal Attack!")

    elif attack_choice == 2 and mana >= 110 and intelligence >= 110:
        total_damage = magic_attack
        print(f"{name} chose Magic Attack!")

    elif attack_choice == 3 and agility >= 115:
        total_damage = agility
        print(f"{name} chose Quick Attack!")

    goblins_hp = max(goblins_hp - total_damage, 0)

    if total_damage > 0:
        print(f"The goblins lost {total_damage} health!")
        print(f"Remaining goblins' health: {goblins_hp}")

    if goblins_hp > 0:
        player_damage = 10
        hp -= player_damage
        print(f"The goblins counterattacked! {name} lost {player_damage} health.")
        print(f"Remaining player's health: {hp}")

    elif goblins_hp == 0:
        print(f"{name} defeated the goblins, congratulations!")
        print(f"Remaining player's health: {hp}")
        break

    if hp <= 0:
        print(f"{name} was defeated by the goblins...")
        break

if hp > 0:
    print(f"???? - After defeating the goblins, {name} continued to explore the evil forest.")
    print(f"You found a chest containing a random item!")
    items = {
        1: "Life Potion",  # Increase 30 health
        2: "Magic Sword",  # Increase 30 mana and 30 damage
        3: "Shield",  # Increase 30 defense
        4: "Spellbook",  # Increase 30 mana and 30 intelligence
        5: "Running Greaves",  # Increase 30 agility
        6: "Chaos Gloves"  # Increase 30 damage
    }
    random_number = random.randint(1, 6)
    found_item = items.get(random_number)
    print(f"{name} opened the chest and found: {found_item}!")
    print()
    if random_number == 1:
        hp += 30
        print(f"Now you have {hp} health points!")
    elif random_number == 2:
        mana += 30
        damage += 30
        print(f"Now you have {mana} mana points and {damage} damage points!")
    elif random_number == 3:
        defense += 30
        print(f"Now you have {defense} defense points!")
    elif random_number == 4:
        mana += 30
        intelligence += 30
        print(f"Now you have {mana} mana points and {intelligence} intelligence points!")
    elif random_number == 5:
        agility += 30
        print(f"Now you have {agility} agility points!")
    elif random_number == 6:
        damage += 30
        print(f"Now you have {damage} damage points!")

    print(f"Defense: {defense}, Health: {hp}, Intelligence: {intelligence}, Mana: {mana}, Damage: {damage}, Agility: {agility}")
    print()
    print(f"???? - After much exploration, {name} found a completely dark and terrifying cave")
    print(f"???? - Encountering several goblins along the way, that cave was not normal like the others, {name} had a bad feeling")
    print(f"???? - Until they came face to face with a huge monster, an ORC, but the strangest thing was that the monster spoke.")
    print("\n")
    print("DARK ORC - So the human they told me about has finally arrived, they said someone would come after this dragon hatchling")
    print("DARK ORC - Want to recover it, then face me, only one of us will leave this cave alive HAHAHAHAHAHAHA!")
    print()
    print("MISSION 2 - Defeat the DARK ORC and take the dragon hatchling home!")
    print("DARK ORC (500 health and 250 defense)")
    print("\n")

    orc_hp = 500
    orc_defense = 250
    total_damage_1 = 0
    fortified_magic_attack = mana + intelligence
    supreme_attack = damage + mana + intelligence + agility

    while hp > 0 and orc_hp > 0:
        print("\nChoose your attack: ")
        print("1) Normal Attack (Requires 120 damage)")
        print("2) Fortified Magic Attack (Requires 170 mana and 150 intelligence)")
        print("3) Ultra Quick Attack (Requires 150 agility)")
        print("4) Supreme Attack (Requires 130 damage, 130 mana, 130 intelligence, and 130 agility)")
        print("NOTE: The Supreme Attack takes 65 health points from the player, use it wisely!")
        attack_choice_1 = int(input("Which attack do you want to choose? "))

        if attack_choice_1 == 1:
            total_damage_1 = damage
            print(f"{name} chose Normal Attack!")

        elif attack_choice_1 == 2 and mana >= 170 and intelligence >= 150:
            total_damage_1 = fortified_magic_attack
            print(f"{name} chose Fortified Magic Attack!")

        elif attack_choice_1 == 3 and agility >= 150:
            total_damage_1 = agility
            print(f"{name} chose Ultra Quick Attack!")

        elif attack_choice_1 == 4 and damage >= 130 and mana >= 130 and intelligence >= 130 and agility >= 130:
            total_damage_1 = supreme_attack
            hp -= 65
            print(f"{name} chose Supreme Attack!")
            print(f"{name} lost 65 health points!")
            print(f"{hp} health points remaining for the player!")

        if orc_defense > 0:
            orc_defense = max(orc_defense - total_damage_1, 0)

            if total_damage_1 > 0:
                print(f"The DARK ORC lost {total_damage_1} defense!")
                print(f"Remaining DARK ORC defense: {orc_defense}")

            if orc_defense == 0:
                print(f"{name} destroyed the DARK ORC's defense. Now defeat it once and for all!")
                print(f"Remaining player's health: {hp}")

        else:
            orc_hp = max(orc_hp - total_damage_1, 0)
            if total_damage_1 > 0:
                print(f"The DARK ORC lost {total_damage_1} health!")
                print(f"Remaining DARK ORC health: {orc_hp}")

            if orc_hp == 0:
                print(f"{name} defeated the DARK ORC, congratulations!")
                break

        if orc_hp > 0:
            base_orc_damage = 20

            player_damage_2 = max(base_orc_damage - (defense // 40), 1)

            hp -= player_damage_2
            print(f"The DARK ORC counterattacked! {name} lost {player_damage_2} health!")
            print(f"Remaining player's health: {hp}")

        if hp <= 0:
            print(f"{name} was defeated by the DARK ORC...")
            break

    print("\n")
    if hp > 0:
        print(f"???? - {name} recovered the dragon hatchling and returned to the village to meet TYR.")
        print("TYR - Congratulations, you completed your first mission, I thought you wouldn't make it!")
        print("TYR - You can keep this dragon hatchling, it liked you, take good care of it.")
        print(f"TYR - Besides that {name}, as a reward, you have the right to choose one of the following blessings!")
        print()
        print("1) The Courage of the Weak: Grants the player 75 more points in each attribute!")
        print("2) The Superior Mage: Grants the player 150 more mana and intelligence!")
        print("3) Superhuman Speed: Grants the player 200 more agility points!")
        print("4) The Impenetrable Barrier: Grants the player 150 more defense and health points!")
        blessing_choice = int(input("Choose your Blessing [1], [2], [3], [4]: "))

        if blessing_choice == 1:
            defense += 75
            hp += 75
            intelligence += 75
            mana += 75
            damage += 75
            agility += 75
            print(f"{name} chose The Courage of the Weak!")
        elif blessing_choice == 2:
            mana += 150
            intelligence += 150
            print(f"{name} chose The Superior Mage!")
        elif blessing_choice == 3:
            agility += 200
            print(f"{name} chose Superhuman Speed!")
        elif blessing_choice == 4:
            defense += 150
            hp += 150
            print(f"{name} chose The Impenetrable Barrier!")

        print(f"Defense: {defense}, Health: {hp}, Intelligence: {intelligence}, Mana: {mana}, Damage: {damage}, Agility: {agility}")

    print("TYR - You have proven to be very strong, wait for new orders for your next mission!")
    print("\n")
    print("???? - Next mission coming soon!")
