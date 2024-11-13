"""
tp4.3
Par Yul Kim
Groupe:405
exercise de tp4.3
"""

from enum import Enum
from dataclasses import dataclass
import random


@dataclass
class Alignment(Enum):
    NOT_DEFINED = 0
    LAWFUL_GOOD = 1
    NEUTRAL_GOOD = 2
    CHAOTIC_GOOD = 3
    LAWFUL_NEUTRAL = 4
    TRUE_NEUTRAL = 5
    CHAOTIC_NEUTRAL = 6
    LAWFUL_EVIL = 7
    NEUTRAL_EVIL = 8
    CHAOTIC_EVIL = 9


@dataclass
class DataItem:
    nombre: list[int]
    item: list[str]


class Backpack:
    def __init__(self):
        self.list_item = [[], []]
        self.item_number = len(self.list_item[0])
        self.item_data = DataItem(self.list_item[1], self.list_item[0])

    def backpack_info(self):
        print("Vous regardez votre inventaire et il y a:")
        self.item_number = len(self.list_item[0])
        for i in range(self.item_number):
            print(f'{self.list_item[0][i - 1]}:{self.list_item[1][i - 1]}')

    def add_item(self, item, nombre):
        self.item_number = len(self.list_item[0])
        for i in range(self.item_number):
            if self.list_item[0][i-1] == item:
                self.list_item[1][i-1] += nombre
                return
            else:
                pass
        self.list_item[0].append(item)
        self.list_item[1].append(nombre)

    def remove_item(self, item, nombre):
        self.item_number = len(self.list_item[0])
        for i in range(self.item_number):
            if self.list_item[0][i-1] == item:
                self.list_item[1][i-1] -= nombre
                if self.list_item[1][i-1] <= 0:
                    self.list_item[0].pop(i-1)
                    self.list_item[1].pop(i - 1)
                return
            else:
                pass
        print("The item is not found")


backpack = Backpack()
backpack.add_item("Vodka", 3)
backpack.backpack_info()
backpack.remove_item("Vodka", 2)
backpack.backpack_info()


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice_list = [dice1, dice2, dice3, dice4]
    dice_list.sort()
    del dice_list[0]
    return sum(dice_list)


def roll_name():
    first_name_list = ['John ', 'Vincent ', 'Joe ', 'James ', 'Michael ', 'Robert ']
    last_name_list = ['Junior', 'Smith', 'Brown', 'Davis', 'William', 'Jackson']
    return random.choice(first_name_list) + random.choice(last_name_list)


def roll_non_monster_race():
    race_list = ['Human', 'Elf', 'Dwarf', 'Dragonborn']
    return random.choice(race_list)


def roll_non_monster_species(race):
    if race == 'Elf':
        return random.choice(['Wood Elf', 'High Elf', 'Half-Elf', 'Dark Elf', 'Moon Elf'])
    elif race == 'Human':
        return random.choice(['Calishite', 'Mulan', 'Shou', 'Iluskan', 'Turami'])
    elif race == 'Dwarf':
        return random.choice(['Gray Dwarf', 'Ember Dwarf', 'Stone Dwarf', 'Tundra Dwarf'])
    elif race == 'Dragonborn':
        return random.choice(['Gray', 'Gold', 'Steel', 'Mithral'])
    else:
        return 'error'


def roll_non_monster_profession():
    non_monster_profession_list = ['Thief', 'Mage', 'Alchemist', 'Knight', 'Priest', 'Blacksmith', 'Archer']
    return random.choice(non_monster_profession_list)


@dataclass
class NpcData:
    force: int
    agilite: int
    constitution: int
    intelligence: int
    sagesse: int
    charisme: int
    armor: int
    name: str
    race: str
    species: str
    health_point: int
    profession: str
    alignment: 0


class NpcMain:
    def __init__(self):
        self.dataNpc = NpcData(roll_dice(), roll_dice(), roll_dice(), roll_dice(), roll_dice(), roll_dice(),
                               random.randint(1, 12), roll_name(), roll_non_monster_race(), "",
                               random.randint(1, 20), roll_non_monster_profession(), random.choice(list(Alignment)))
        self.dataNpc.species = roll_non_monster_species(self.dataNpc.race)
        self.backpack = Backpack()

    def information(self):
        print(f'\nName:{self.dataNpc.name}  Race/Species:{self.dataNpc.race}/{self.dataNpc.species}'
              f' Alignment:{str(self.dataNpc.alignment.name.capitalize().replace("_", " "))}'
              f' Hp:{self.dataNpc.health_point}'
              f'\nProfession:{self.dataNpc.profession}'
              f'\nStr:{self.dataNpc.force}'
              f' | Agi:{self.dataNpc.agilite}'
              f'\nCon:{self.dataNpc.constitution}'
              f' | Int:{self.dataNpc.intelligence}'
              f'\nWis:{self.dataNpc.sagesse}'
              f' | Cha:{self.dataNpc.charisme}\n')

    @staticmethod
    def attaque(cible):
        attaque_roll = random.randint(1, 20)
        if attaque_roll == 1:
            damage = 0
            cible.receve_damage(damage)
        elif attaque_roll == 20:
            damage = attaque_roll
            cible.receve_damage(damage)
        elif 1 < attaque_roll < 20:
            damage = attaque_roll
            cible.receve_damage(damage)

    def receve_damage(self, damage):
        if damage == 0:
            print(f'L enemie a rate.{self.dataNpc.name} a {damage} de dommage.')
        elif damage == 20:
            print(f'L enemie a fait une attque critique.{self.dataNpc.name} a recu {damage} de dommage.')
            self.dataNpc.health_point -= damage
        elif 1 < damage < 20:
            if self.dataNpc.armor > damage:
                damage = 0
                print(f'L armour de {self.dataNpc.name} a bloque l attaque du enemie.'
                      f'{self.dataNpc.name} a recu {damage} de dommage.')
            elif self.dataNpc.armor < damage:
                damage -= self.dataNpc.armor
                print(f'L armour de {self.dataNpc.name} a bloque l attaque du enemie.'
                      f'{self.dataNpc.name} a recu {damage} de dommage.')
                self.dataNpc.health_point -= damage

    def verify_death(self):
        if self.dataNpc.health_point <= 0:
            print(f'{self.dataNpc.name} est mort.')
        else:
            print(f'{self.dataNpc.name} est vivant')


npc = NpcMain()
npc.information()


class KoboldMain(NpcMain):
    def __init__(self):
        super().__init__()
        self.dataNpc.race = 'Kobold'
        self.dataNpc.species = random.choice(['Ocean Kobold', 'Volcano Kobold', 'Mine Kobold', 'Forest Kobold'])

    def information(self):
        super().information()


class Hero(NpcMain):
    def __init__(self):
        super().__init__()

    def information(self):
        super().information()


hero = Hero()
kobold = KoboldMain()
kobold.attaque(npc)
npc.verify_death()
npc.information()
hero.backpack.backpack_info()
