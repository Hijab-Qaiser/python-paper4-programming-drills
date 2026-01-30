class student:
    def __init__(self, name, roll_number, Class):
        self.__name = name  # Private string variable
        self.__roll_number = roll_number  # Private integer variable
        self.__Class = Class  # Private string variable

    @property
    def GetName(self):
        return self.__name

    @GetName.setter
    def GetName(self, name_value):
        self.__name = name_value

    @property
    def Getroll_number(self):
        return self.__roll_number

    @Getroll_number.setter
    def Getroll_number(self, roll_number_value):
        self.__roll_number = roll_number_value

    @property
    def GetClass(self):
        return self.__Class

    @GetClass.setter
    def GetClass(self, class_value):
        self.__Class = class_value

    def Display_info(self):

        self.GetName = input("Enter student name: ")
        self.Getroll_number = int(input("Enter roll number: "))
        self.GetClass = input("Enter class: ")

        print(f"\nStudent Info:")
        print(f"Name: {self.GetName}")
        print(f"Roll Number: {self.Getroll_number}")
        print(f"Class: {self.GetClass}")


S1 = student("", 0, "")


S1.Display_info()
