class Enemy:

    #Default constructor
    # def __init__(self):
    #     pass

    def __init__(self , type_of_enemy , hp , att_damage ):
        self.type_of_enemy = type_of_enemy
        self.health = hp
        self.damage = att_damage

    def get_type_of_enemy(self):
        return self.type_of_enemy

    def special_attack(self):
        print("Enemy has no special attack")

    def talk(self):
        print(f"I am a {self.get_type_of_enemy()}!")
    def walk(self):
        print(f"{self.get_type_of_enemy()} is walking towards you!")
    def attack(self):
        print(f"{self.get_type_of_enemy()} is attacking! Damage: {self.damage}")
        return self.damage
