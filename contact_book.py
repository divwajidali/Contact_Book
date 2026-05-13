#ATM machine sysstem
class Contactbook:
    def __init__(self):
        self.dict = {}

    def add_contact(self, name, contact):
        self.name = name
        self.contact = contact
        self.dict.update({self.name : self.contact})


    def show_contact(self):
        print(self.dict)


    def search_contact(self, name):
        if name in self.dict:
            self.name = name
            num = self.dict[name]
            print(num)
        else:
            print("You enter incorrect name.\nPlease enter correct name again :")

    def delete_contact(self, name):
        if name in self.dict:
            self.name = name
            self.dict.pop(name)
        else:
            print("You enter incorrect name.\nPlease enter correct name again :")


c1 = Contactbook()

while True:
    choice = input("Select one option.\n1. Add Contact\n2. Show Contact\n3. Search Contact\n4. Delete Contact\n5. Exit\nEnter option :")


    if (choice == "1"):
        name = input("Enter name :")
        contact = input("Enter contact :")
        c1.add_contact(name, contact)

    elif (choice == "2"):
        c1.show_contact()

    elif (choice == "3"):
        name = input("Enter name :")
        c1.search_contact(name)

    elif (choice == "4"):
        name = input("Enter name :")
        c1.delete_contact(name)

    elif (choice == "5"):
        print("Exit")
        break

    else:
        print("You entered an invalid option. Please entered valid option.")