# 📒 Contact Book Management System

A beginner-friendly Python Contact Book project built using **Object-Oriented Programming (OOP)**.

This project allows users to:

- ✅ Add Contacts
- ✅ Show All Contacts
- ✅ Search Contacts
- ✅ Delete Contacts
- ✅ Exit Program

This project is great for practicing:

- Classes & Objects
- Dictionaries
- Methods
- Loops
- Conditional Statements
- User Input Handling

---

# 📌 Features

- Add new contacts
- Store contact names and numbers
- Display all saved contacts
- Search contacts by name
- Delete contacts
- Simple menu-driven interface

---

# ▶️ How To Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

## 2️⃣ Open Project Folder

```bash
cd your-repository-name
```

## 3️⃣ Run Program

```bash
python main.py
```

---

# 💻 Project Code

```python
class Contactbook:

    def __init__(self):
        self.dict = {}

    def add_contact(self, name, contact):
        self.name = name
        self.contact = contact

        self.dict.update({
            self.name: self.contact
        })

    def show_contact(self):
        print(self.dict)

    def search_contact(self, name):

        if name in self.dict:
            self.name = name
            num = self.dict[name]

            print(num)

        else:
            print("You entered incorrect name.")
            print("Please enter correct name again.")

    def delete_contact(self, name):

        if name in self.dict:
            self.name = name
            self.dict.pop(name)

        else:
            print("You entered incorrect name.")
            print("Please enter correct name again.")


c1 = Contactbook()

while True:

    choice = input(
        "Select one option.\n"
        "1. Add Contact\n"
        "2. Show Contact\n"
        "3. Search Contact\n"
        "4. Delete Contact\n"
        "5. Exit\n"
        "Enter option : "
    )

    if (choice == "1"):

        name = input("Enter name : ")
        contact = input("Enter contact : ")

        c1.add_contact(name, contact)

    elif (choice == "2"):

        c1.show_contact()

    elif (choice == "3"):

        name = input("Enter name : ")
        c1.search_contact(name)

    elif (choice == "4"):

        name = input("Enter name : ")
        c1.delete_contact(name)

    elif (choice == "5"):

        print("Exit")
        break

    else:
        print("You entered an invalid option.")
        print("Please enter valid option.")
```

---

# 🧪 Example Output

```bash
Select one option.
1. Add Contact
2. Show Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter option : 1

Enter name : Ali
Enter contact : 03001234567

Select one option.
1. Add Contact
2. Show Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter option : 2

{'Ali': '03001234567'}
```

---

# 📚 Concepts Used

| Concept | Description |
|---|---|
| Class | Creates Contact Book blueprint |
| Object | Creates Contact Book instance |
| Dictionary | Stores contacts |
| Methods | Performs operations |
| while loop | Runs menu repeatedly |
| if-elif-else | Handles conditions |

---

# 🚀 Future Improvements

You can improve this project by adding:

- File Handling
- Contact Update Feature
- Contact Validation
- Search by Number
- GUI using Tkinter
- Database Integration
- Favorite Contacts
- Multiple Users

---

# 👨‍💻 Author

**Wajid Ali**

Python Beginner Developer 🚀

---