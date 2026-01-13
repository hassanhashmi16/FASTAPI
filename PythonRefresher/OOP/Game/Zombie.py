from Enemy import *
import random

class Zombie(Enemy):

    def __init__(self , hp , att_damage ):
        super().__init__(type_of_enemy="Zombie",
                         hp=hp ,
                         att_damage = att_damage)
    def talk(self):
        print("Grrrrrrr")

    def spread_disease(self):
        print("The zombie is spreading infection")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.80
        if did_special_attack_work:
            self.health += 50
            print("Zombie regenerated health by 50")