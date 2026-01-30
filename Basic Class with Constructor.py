class Car:
    def __init__(self, CarModel, Year, Price):
        self.__CarModel = CarModel  # Private string variable
        self.__Year = Year  # Private integer variable
        self.__Price = Price  # Private float variable

    @property
    def GetCarModel(self):
        return self.__CarModel

    @property
    def GetYear(self):
        return self.__Year

    @property
    def GetPrice(self):
        return self.__Price


MyCar = Car("Toyota Corolla", 2023, 85000.0)

print(f"Car Model: {MyCar.GetCarModel}, Year: {MyCar.GetYear}, Price: {MyCar.GetPrice}")
