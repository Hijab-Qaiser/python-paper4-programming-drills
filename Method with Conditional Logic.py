class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Private string variable
        self.balance = balance  # Private float variable

    @property
    def GetAccountNumber(self):
        return self.account_number

    @GetAccountNumber.setter
    def GetAccountNummber(self, value):
        self.account_number = value

    @property
    def Getbalance(self):
        return self.balance

    @Getbalance.setter
    def Getbalance(self, value):
        self.balance = value

    def deposit(self, amount):
        while amount <= 0:
            float(input(f"Deposit must be positive, try again! "))
        self.balance += amount
        print(f"New balance: {self.Getbalance}")

    def withdraw(self, amount):
        while amount <= 0 or amount > self.balance:
            amount = float(input(f"Withdrawal not Successful, try again! "))
        self.balance -= amount
        print(f"Withdrawal Successful! ")
        print(f"New balance: {self.Getbalance}")


Account_1 = BankAccount("ACC001", 5000.00)


def system(acc):
    while True:
        print(
            f"Initial balance of Account Number {acc.GetAccountNumber} = {acc.Getbalance}"
        )
        choice = input(f"You want to Deposit or withdraw? ")
        if choice.lower() == "deposit":
            amount = float(input(f"Enter amount you want to deposit: "))
            acc.deposit(amount)
        else:
            amount = float(input(f"Enter amount you want to withdraw: "))
            acc.withdraw(amount)

        choice_2 = input(f"Do you want to continue: ")
        if choice_2.lower() == "no":
            break


system(Account_1)
