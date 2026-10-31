from weapons.main_weapon import Weapon

class Sword(Weapon):
    def __init__(self, name, damage, weapon_type):
        super().__init__(name, damage, weapon_type)


class Bow(Weapon):
    def __init__(self, name, damage, weapon_type):
        super().__init__(name, damage, weapon_type)


class XBow(Weapon):
    def __init__(self, name, damage, weapon_type):
        super().__init__(name, damage, weapon_type)