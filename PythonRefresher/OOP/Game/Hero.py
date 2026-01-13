from Weapon import *

class Hero:
    def __init__(self , health , damage):
        self.health = health
        self.damage = damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None

    def equip_weapon(self ):
        if self.is_weapon_equipped is not None and not self.is_weapon_equipped:
            self.damage += self.weapon.attack_increase
            self.is_weapon_equipped = True
            # self.weapon = weapon
        # else:
        #     return

    def attack(self):
        print(f"Hero attacks for {self.damage}")

