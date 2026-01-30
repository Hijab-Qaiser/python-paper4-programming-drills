class contact:
    def __init__(self, name, phone_nuber, email):
        self.__name = name  # Private string variable
        self.__phone_nuber = phone_nuber  # Private string variable
        self.__email = email  # Private string variable

    @property
    def GetName(self):
        return self.__name

    @property
    def GetPhoneNumber(self):
        return self.__phone_nuber

    @property
    def GetEmail(self):
        return self.__email

    def DisplayContact(self):
        print(f"Name: {self.__name}")
        print(f"Phone: {self.__phone_nuber}")
        print(f"Email: {self.__email}")


def SearchContact(phonebook, search_name):
    for i in range(len(phonebook)):
        if phonebook[i].GetName.lower() == search_name.lower():
            phonebook[i].DisplayContact()
            return True

    print("Contact not found")
    return False


PhoneBook = []  # empty string array
for i in range(5):
    print(f"\nContact {i+1}:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact_obj = contact(name, phone, email)
    PhoneBook.append(contact_obj)

while True:
    print("\nSearch Session")
    search_name = input("Enter name to search: ")
    SearchContact(PhoneBook, search_name)

    again = input("Search again? (yes/no): ")
    if again.lower() != "yes":
        break
