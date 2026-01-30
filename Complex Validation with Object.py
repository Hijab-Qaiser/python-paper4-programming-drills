class movieticket:
    def __init__(self, movie_name, seat_number):
        self.movie_name = movie_name  # string variable
        self.seat_number = seat_number  # string variable
        self.price = 0.0  # float variable

    @property
    def GetMovieName(self):
        return self.movie_name

    @GetMovieName.setter
    def GetMovieName(self, value):
        self.movie_name = value

    @property
    def GetSeatNumber(self):
        return self.seat_number

    @property
    def GetPrice(self):
        return self.price

    def SetPrice(self, seat_type):
        if seat_type == "E":
            self.price = 500
            return True
        elif seat_type == "S":
            self.price = 800
            return True
        elif seat_type == "P":
            self.price = 1200
            return True
        else:
            return False

    def ApplyDiscount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)


ticket1 = movieticket(input("Enter movie name: "), input("Enter seat number: "))

while True:
    seat_type = input(f"Enter a valid seat type: ")
    if ticket1.SetPrice(seat_type):
        is_student = input(f"Are you a student: ").lower()
        if is_student == "yes":
            ticket1.ApplyDiscount(20)
        break
print(f"Final tickert price = {ticket1.GetPrice}")
