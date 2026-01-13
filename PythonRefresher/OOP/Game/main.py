from Enemy import *
from Zombie import *
from Titan import *
from Hero import *
from Weapon import *

def battle(e1: Enemy , e2: Enemy):
    e1.talk()
    e2.talk()


    while e1.health > 0 and e2.health > 0:
        print("-------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()} : {e1.health}hp left"
              f"{e2.get_type_of_enemy()} : {e2.health}hp left")
        e2.attack()
        e1.health -= e2.damage
        e1.attack()
        e2.health -= e1.damage
    print('-----------')

    if e1.health > 0:
        print(f"{e1.get_type_of_enemy()} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")

def hero_battle(hero: Hero , e: Enemy):
    e.talk()

    while hero.health > 0 and e.health > 0:
        print("-------")
        e.special_attack()
        print(f"hero : {hero.health}hp left"
              f"{e.get_type_of_enemy()} : {e.health}hp left")
        e.attack()
        hero.health -= e.damage
        hero.attack()
        e.health -= hero.damage
    print('-----------')

    if hero.health > 0:
        print(f"Hero wins!")
    else:
        print(f"{e.get_type_of_enemy()} wins!")

zombie = Zombie(100, 10)
titan = Titan(250 , 25)
hero = Hero(100 , 30)
weapon = Weapon('Dragon Slayer' , 5)

hero.weapon = weapon
hero.equip_weapon()

battle(zombie , titan)
hero_battle(hero , titan)
