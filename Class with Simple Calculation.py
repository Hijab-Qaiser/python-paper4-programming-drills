class circle:
    def __init__(self, radius):
        self.__radius = radius  # Private float variable

    @property
    def Getradius(self):
        return self.__radius

    def CalculateArea(self):
        r = self.Getradius  # float variable
        return 3.14 * r * r

    def CalculateCircumference(self):
        r = self.Getradius  # float variable
        return 2 * 3.14 * r


MyCircle = circle(7.0)

print(f"Area: {MyCircle.CalculateArea()}")
print(f"Circumference: {MyCircle.CalculateCircumference()}")
