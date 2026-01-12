from Enemy import *

class Zombie(Enemy):

    def __init__(self , hp , att_damage ):
        super().__init__(type_of_enemy="Zombie",
                         hp=hp ,
                         att_damage = att_damage)
    def talk(self):
        print("Grrrrrrr")

    def spread_disease(self):
        print("The zombie is spreading infection")