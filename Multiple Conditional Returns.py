class temperature:
    def __init__(self, city, celsius):
        self.city = city  # string variable
        self.celsius = celsius  # float variable

    @property
    def Getcity(self):
        return self.city

    @Getcity.setter
    def Getcity(self, value):
        self.city = value

    @property
    def Getcelsius(self):
        return self.celsius

    @Getcelsius.setter
    def Getcelsius(self, value):
        self.celsius = value

    def ConvertToFahrenheit(self):
        fahrenheit = (self.Getcelsius * 9 / 5) + (32)
        return fahrenheit

    def GetWeatherCondition(self):
        if self.Getcelsius > 35:
            return f"Very Hot "
        elif self.Getcelsius >= 25 or self.Getcelsius <= 35:
            return f"Hot "
        elif self.Getcelsius >= 15 or self.Getcelsius <= 24:
            return f"Warm "
        elif self.Getcelsius >= 5 or self.Getcelsius <= 14:
            return f"Cool "
        else:
            return "Cold "


karachi = temperature("Karachi", 32.5)
print(
    f"{karachi.Getcity}'s temperature = {karachi.Getcelsius} Temperature in Fahrenheit = {karachi.ConvertToFahrenheit()}"
)
print(f"It is {karachi.GetWeatherCondition()}today")
