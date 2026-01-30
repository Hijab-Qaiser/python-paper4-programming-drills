class Phone:
    def __init__(self, brand, model):
        self.__brand = brand  # Private string variable
        self.__model = model  # Private string variable
        self.__battery_level = 100  # Private integer variable

    @property
    def Getbrand(self):
        return self.__brand

    @property
    def Getbattery_level(self):
        return self.__battery_level

    @Getbattery_level.setter
    def Getbattery_level(self,value):
        self.__battery_level = value


MyPhone = Phone("Samsung", "Galaxy S24")


print(f"Initial Battery Level: {MyPhone.Getbattery_level}")
MyPhone.Getbattery_level = 45 
print(f"New Battery Level: {MyPhone.Getbattery_level}")
