from utility.calculate_critic_e import calculate_critic_e
from weapons.main_weapon import Weapon


class MainEntity:
    def __init__(self, name, hp, entity_type, weapon: Weapon, default_damage):
        self.name = name
        self.hp = hp
        self.entity_type= entity_type
        self.weapon = weapon
        self.default_damage = default_damage

    def calculate_damage(self):
        critic = calculate_critic_e(self, self.weapon)
        damage = self.default_damage * self.weapon.get_damage
        return damage + ((damage / 100) * critic)

    @property
    def get_entity_type(self):
        return self.entity_type

    def take_damage(self, amount):
        if amount < 0:
            return
        self.hp = max(0, self.hp - amount)

    @property
    def get_hp(self):
        return self.hp

    @property
    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp += amount
