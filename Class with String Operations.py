class password:
    def __init__(self, user_password):
        self.__user_password = user_password  # Private string variable

    @property
    def GetPassword(self):
        return self.__user_password

    @GetPassword.setter
    def GetPassword(self, value):
        self.__user_password = value

    def GetLenght(self):
        lenght = len(self.__user_password)
        return lenght

    def IsStrong(self):
        if self.GetLenght() >= 8:
            return f"Strong Password "
        return f"Weak Password "


Pass1 = password("")
Pass1.GetPassword = input(f"Enter your Password: ")
print(Pass1.IsStrong())
