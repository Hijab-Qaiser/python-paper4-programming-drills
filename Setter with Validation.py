class employee:
    def __init__(self, name, age, salary):
        self.name = name  # string variable
        self.age = age  # integer variable
        self.salary = salary  # float variable

    @property
    def GetName(self):
        return self.name

    @property
    def GetAge(self):
        return self.age

    @GetAge.setter
    def GetAge(self, value):
        self.age = value

    def SetAge(self, value):
        if value >= 18 and value <= 65:
            self.GetAge = value
            return True
        return False

    @property
    def GetSalary(self):
        return self.salary


Emp1 = employee("Ali Khan", 30, 50000.00)
value = int(input(f"Enter age "))
if Emp1.SetAge(value) == True:
    print(f"Age updated to", Emp1.GetAge)
else:
    print(f"Invalid age, Try again! ")
