from Enemy import *

class Titan(Enemy):
    def __init__(self , hp , att_damage):
        super().__init__(
                        type_of_enemy='Titan',
                        hp = hp ,
                        att_damage=att_damage)

    def talk(self):
        print("Bro cant talk" )