from classes.magic import Spell
from classes.inventory import Item
from classes.player_classes import *


# Create Skills
triple_shot = Spell("Triple Shot", 50, 400, "skill")
power_shot = Spell("Power Shot", 50, 1400, "skill")
holy_shield = Spell("Holy Shield", 50, 40, "skill")
divine_shield = Spell("Divine Shield", 50, 15, "skill")

# Create Black Magic
element = Spell("Element", 25, 600, "black")
meteor = Spell("Meteor", 40, 1250, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")
renew = Spell("Renew", 30, 400, "white")


# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 9999)
phoenixdown = Item("Phoenix Down", "revival", "Cures KO and heals for 500 HP", 500)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


black_mage_spells = [element, meteor, quake]
white_mage_spells = [cure, cura, renew]
rogue_skills = [triple_shot, power_shot]
tank_skills = [holy_shield, divine_shield]

enemy_spells = [element, meteor, curaga]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2}, {"item": grenade, "quantity": 5},
                {"item": phoenixdown, "quantity": 3}]


# Instantiate People
player1 = Rogue("Zidane ", 3260, 150, 400, 25, 20, rogue_skills, player_items, "alive")
player2 = BlackMage("Vivi   ", 4160, 200, 150, 34, 10, black_mage_spells, player_items, "alive")
player3 = WhiteMage("Dagger ", 3089, 200, 150, 34, 10, white_mage_spells, player_items, "alive")
player4 = Tank("Steiner", 3089, 50, 200, 34, 40, tank_skills, player_items, "alive")

enemy1 = Person("Add 1 ", 1250, 130, 560, 325, enemy_spells, [], "alive")
enemy2 = Person("Boss  ", 18200, 701, 525, 25, enemy_spells, [], "alive")
enemy3 = Person("Add 2 ", 1250, 130, 560, 325, enemy_spells, [], "alive")

players = [player1, player2, player3, player4]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0


while running:

    print(BColors.FAIL + BColors.BOLD)
    print("========================================================================")
    print("                             ACTIVE BATTLE")
    print("========================================================================")
    print(BColors.ENDC)

    print("\n==========")
    print("Your Team:")
    print("==========")
    print("\nNAME                  HP                                      MP")
    for player in players:
        player.get_stats()

    print("\n==========")
    print("Enemy team")
    print("==========")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        if player.status == "alive":
            player.choose_action()
        else:
            continue
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg[0])
            print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg[0], "points of damage. It's a " + dmg[1] + " hit.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose line: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(BColors.FAIL + "\nNot enough MP\n" + BColors.ENDC)
                continue

            if spell.type == "white":
                if spell.name == "Renew":
                    for i in players:
                        if i.status == "alive":
                            magic_dmg = spell.generate_damage()
                            i.heal(magic_dmg)
                            print(BColors.OKBLUE + "\n" + spell.name + " heals " + i.name.replace(" ", "") + " for", str(magic_dmg), "HP." + BColors.ENDC)

                else:
                    players[player.choose_target(players)].heal(magic_dmg)

                    print(BColors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + BColors.ENDC)
            elif spell.type == "black":

                if spell.name == "Quake":

                    for i in enemies:
                        magic_dmg = spell.generate_damage()
                        i.take_damage(magic_dmg)
                        print(BColors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + i.name.replace(" ", "") + BColors.ENDC)

                        if i.get_hp() == 0:
                            print(i.name.replace(" ", "") + " has died.")
                            del i
                else:
                    enemy = player.choose_target(enemies)

                    enemies[enemy].take_damage(magic_dmg)

                    print(BColors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                          "points of damage to " + enemies[enemy].name.replace(" ", "") + BColors.ENDC)

                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") + " has died.")
                        del enemies[enemy]

            elif spell.type == "skill":
                if spell.name == "Triple Shot":
                    for i in enemies:
                        magic_dmg = spell.generate_damage()
                        i.take_damage(magic_dmg)
                        print(BColors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + i.name.replace(" ", "") + BColors.ENDC)
                        if i.get_hp() == 0:
                            print(i.name.replace(" ", "") + " has died.")
                            del i

                if spell.name == "Power Shot":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(magic_dmg)
                    print(BColors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace(" ", "") + BColors.ENDC)
                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") + " has died.")
                        del enemies[enemy]

                if spell.name == "Holy Shield":
                    players[player.choose_target(players)].defence += magic_dmg
                    print(BColors.OKBLUE + "\n" + spell.name + " increases defence for", str(magic_dmg), "HP." + BColors.ENDC)

                if spell.name == "Divine Shield":
                    for i in players:
                        if i.status == "alive":
                            magic_dmg = spell.generate_damage()
                            i.defence += magic_dmg
                            print(BColors.OKBLUE + "\n" + spell.name + " increases defence of " + i.name.replace(" ", "") + " by", str(magic_dmg), "HP." + BColors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(BColors.FAIL + "\n" + "None left..." + BColors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(BColors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + BColors.ENDC)
            elif item.type == "elixir":

                if item.name == "MegaElixir":
                    for i in players:
                        if i.status == "alive":
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(BColors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + BColors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(BColors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name + BColors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

            elif item.type == "revival":
                testint = int(player.choose_target_to_revive(players))
                if players[testint].status == "fainted":
                    players[testint].status = "alive"
                    players[testint].hp = 500
                    print(BColors.FAIL + "\n" + item.name + " revives " + players[testint].name.replace(" ", "") + " with 500HP!" + BColors.ENDC)
                else:
                    print(BColors.FAIL + "\n" + item.name + " failed to revive alive player, you lost an item..." + BColors.ENDC)

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.status == "fainted":
            defeated_players += 1

    if defeated_enemies == 2:
        print(BColors.OKGREEN + "You win!" + BColors.ENDC)
        running = False

    elif defeated_players == 2:
        print(BColors.FAIL + "Your enemies have defeated you!" + BColors.ENDC)
        running = False

    print("\n")
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for " + str(enemy_dmg) + " points of damage. Player defence reduced it to " + str(enemy_dmg - 5 * player.defence))

            if players[target].get_hp() == 0:
                print(players[target].name.replace(" ", "") + " has fainted.")

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(BColors.OKBLUE + spell.name + " heals " + enemy.name.replace(" ", "") + " for", str(magic_dmg), "HP." + BColors.ENDC)
            elif spell.type == "black":

                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)

                print(BColors.OKBLUE + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage to " + players[target].name.replace(" ", "") + ". Player defence reduced it to " + str(magic_dmg - 5 * player.defence) + BColors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has fainted.")
