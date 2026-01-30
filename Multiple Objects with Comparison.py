class runner:
    def __init__(self, name, time):
        self.name = name  # string variable
        self.time = time  # float variable

    @property
    def GetName(self):
        return self.name

    @property
    def GetTime(self):
        return self.time

    def IsFasterThan(self, other_runner):
        if self.time < other_runner.time:
            return True
        return False


Runner_1 = runner("Usain Bhai", 9.58)
Runner_2 = runner("Tyson Bhai", 9.69)
if Runner_1.IsFasterThan(Runner_2):
    print(f"{Runner_1.GetName} is faster than {Runner_2.GetName}")
else:
    print(f"{Runner_2.GetName} is faster than {Runner_1.GetName}")
