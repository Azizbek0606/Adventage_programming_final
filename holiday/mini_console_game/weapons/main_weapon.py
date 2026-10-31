class Weapon:
    def __init__(self, name, damage, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type

    @property
    def get_damage(self):
        return self.damage
    @property
    def get_weapon_type(self):
        return self.weapon_type
    def get_name(self):
        return self.name