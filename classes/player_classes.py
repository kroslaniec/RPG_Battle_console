from classes.game import *
import random


class Rogue(Person):

    def __init__(self, name, hp, mp, atk, attribute, defence, magic, items, status):
        super().__init__(name, hp, mp, atk, attribute, magic, items, status)
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.attribute = attribute
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Skills", "Items"]
        self.name = name
        self.status = status
        self.defence = defence

    def generate_damage(self):
        crit_chance = random.randrange(0, 100)
        if crit_chance <= 20:
            return round(random.randrange(self.atkl, self.atkh) * (self.attribute/5)), BColors.FAIL + "CRITICAL" + BColors.ENDC
        else:
            return round(random.randrange(self.atkl, self.atkh)*(self.attribute/10)), "normal"

    def take_damage(self, dmg):
        self.hp -= dmg - self.defence * 5
        if self.hp < 0:
            self.hp = 0
            self.status = "fainted"
        return self.hp


class Tank(Person):

    def __init__(self, name, hp, mp, atk, attribute, defence, magic, items, status):
        super().__init__(name, hp, mp, atk, attribute, magic, items, status)
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.attribute = attribute
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Skills", "Items"]
        self.name = name
        self.status = status
        self.defence = defence

    def generate_damage(self):
        crit_chance = random.randrange(0, 100)
        if crit_chance <= 10:
            return round(random.randrange(self.atkl, self.atkh) * (self.attribute/5)), BColors.FAIL + "CRITICAL" + BColors.ENDC
        else:
            return round(random.randrange(self.atkl, self.atkh)*(self.attribute/10)), "normal"

    def take_damage(self, dmg):
        self.hp -= dmg - self.defence * 5
        if self.hp < 0:
            self.hp = 0
            self.status = "fainted"
        return self.hp


class WhiteMage(Person):

    def __init__(self, name, hp, mp, atk, attribute, defence, magic, items, status):
        super().__init__(name, hp, mp, atk, attribute, magic, items, status)
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.attribute = attribute
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "White Magic", "Items"]
        self.name = name
        self.status = status
        self.defence = defence

    def generate_damage(self):
        crit_chance = random.randrange(0, 100)
        if crit_chance <= 10:
            return round(random.randrange(self.atkl, self.atkh) * (self.attribute/5)), BColors.FAIL + "CRITICAL" + BColors.ENDC
        else:
            return round(random.randrange(self.atkl, self.atkh)*(self.attribute/10)), "normal"

    def take_damage(self, dmg):
        self.hp -= dmg - self.defence * 5
        if self.hp < 0:
            self.hp = 0
            self.status = "fainted"
        return self.hp


class BlackMage(Person):

    def __init__(self, name, hp, mp, atk, attribute, defence, magic, items, status):
        super().__init__(name, hp, mp, atk, attribute, magic, items, status)
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.attribute = attribute
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Black Magic", "Items"]
        self.name = name
        self.status = status
        self.defence = defence

    def generate_damage(self):
        crit_chance = random.randrange(0, 100)
        if crit_chance <= 10:
            return round(random.randrange(self.atkl, self.atkh) * (self.attribute/5)), BColors.FAIL + "CRITICAL" + BColors.ENDC
        else:
            return round(random.randrange(self.atkl, self.atkh)*(self.attribute/10)), "normal"

    def take_damage(self, dmg):
        self.hp -= dmg - self.defence * 5
        if self.hp < 0:
            self.hp = 0
            self.status = "fainted"
        return self.hp
