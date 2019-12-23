import random
from time import sleep


class Warrior:
    # defining character
    def __init__(self, name='Anonymus', health=100, attack_pt=1, defense_pt=1):
        self.name = name
        self.health = health
        self.attack_pt = attack_pt
        self.defense_pt = defense_pt

    # defining attack action
    def attack(self):
        return random.randint(0, self.attack_pt)*random.randint(1,5)

    # defining defense action
    def defense(self):
        return random.randint(0, self.defense_pt)*random.randint(1,2)
    # defining reduction of health
    def minus_health(self,damage):
        self.health -= damage
        # checking if character is alive
        if self.health <= 0:
            print(self.name + " die")

    # checking if character is alive
    def isexist(self):
        if self.health <= 0:
            return False
        else:
            return True

    # returning name of character
    def __str__(self):
        return self.name


# defining fight action
def fight(knight, monkey):
    round_number = 1
    # checking if characters are alive
    while(knight.isexist() and monkey.isexist()):
        print('Round: ', round_number)
        ptr_statistic(knight, monkey)

        # if 0 knight action if 1 monkey action
        if random.randint(0, 1) == 0:
            battle(knight, monkey)
        else:
            battle(monkey, knight)

        print('')
        sleep(5)
        round_number += 1

    if knight.isexist():
        print('Well done! The knight has won!')
    else:
        print('Well done! The monkey has won!')

# battle action
def battle(player_1, player_2):
    print(player_1, 'attacked ', player_2)
    damage = player_1.attack_pt - player_2.defense_pt
    print(player_1, 'damage ', damage)
    player_2.minus_health(damage)

# print statistic of character
def ptr_statistic(player_1,player_2):
    for i in (player_1,player_2):
        print(i, "have ", i.health, ' HP')

knight = Warrior('Geralt', 100, 10, 0)
monkey = Warrior('Monkey Warior', 80, 5,0)

fight(knight,monkey)