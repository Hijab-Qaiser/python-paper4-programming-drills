class monster:
    def __init__(self, name, health, attack_power):
        self.name = name  # string variable
        self.health = health  # integer variable
        self.attack_power = attack_power  # integer variable

    @property
    def GetName(self):
        return self.name

    @property
    def GetHealth(self):
        return self.health

    @property
    def GetAttackPower(self):
        return self.attack_power

    def TakeDamage(self, amount):
        self.health -= amount

    def IsDefeated(self):
        if self.health <= 0:
            return True
        return False


def BattleRound(monster_object, player_damage):
    monster_object.TakeDamage(player_damage)
    print(
        f"Monster took {player_damage} damage! Health remaining: {monster_object.GetHealth}"
    )

    if monster_object.IsDefeated():
        print(f"Monster {monster_object.GetName} has been defeated! ")
    else:
        print(f"Monster attacks back for {monster_object.GetAttackPower} damage! ")

    return monster_object


Dragon = monster("Fire Dragon", 100, 25)
while Dragon.IsDefeated() == False:
    damage = int(input("Enter your attack damage: "))
    Dragon = BattleRound(Dragon, damage)
    print(f"\n")
