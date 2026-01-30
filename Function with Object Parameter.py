class player:
    def __init__(self, name, score, lives):
        self.name = name  # string variable
        self.score = score  # integer variable
        self.lives = lives  # integer variable

    @property
    def GetName(self):
        return self.name

    @property
    def GetScore(self):
        return self.score

    @property
    def GetLives(self):
        return self.lives

    def AddScore(self, point):
        self.score += 10

    def LoseLife(self):
        self.lives -= 1


def PlayRound(player_object):
    answer = input(f"Did you win this round: ").lower()
    if answer == "yes":
        player_object.AddScore(10)

    else:
        player_object.LoseLife()
    return player_object


Player_1 = player("Ahmed", 0, 0)
for count in range(3):
    Player_1 = PlayRound(Player_1)
print(f"\n")
print(f"Final score = {Player_1.GetScore} and final lives = {Player_1.GetLives}")
