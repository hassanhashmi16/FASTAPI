from Enemy import *
import random
class Titan(Enemy):
    def __init__(self , hp , att_damage):
        super().__init__(
                        type_of_enemy='Titan',
                        hp = hp ,
                        att_damage=att_damage)

    def talk(self):
        print("Bro cant talk" )

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.damage += 25
            self.health -= 50
            print("Titan got angry and increased damage by 5 points but lost 50hp")