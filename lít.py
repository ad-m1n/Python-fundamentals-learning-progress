#1 
chim1 = {"Estelle": "21", "Aion": "23", "Seraphin": "29"}
for key, value in chim1.items():
    print(f"{key} is {value} years old")

#2
chim2 = input("Type in a random word: ")
chim3 = {}
for letter in chim2:
    if letter in chim3:
        chim3[letter] += 1
    else:
        chim3[letter] = 1
print(chim3)

#3
chim4 = {"name": "anna", "age": 23}
chim5 = {"student": "bobby", "born in": 2009}
chim6 = chim4 | chim5
print(chim6)

#4
chim7 = {"apple": 90, "iphonekupi": 1900, ",applemeomeo": 3}
chim8 = max(chim7, key=chim7.get)
print(chim8)

#5

chim9 = {}
while True:
    print("--Interactive Phonebook Menu--")
    print("1. Add new contact")
    print("2. Search")
    print("3. Delete contact")
    print("4. Quit")

    chim10 = input("Chose an option: ")

    if chim10 == '1':
        chim10 = input("New contact phone number: ")
        chim11 = input("Contact name:")
        chim9[chim11] = chim10
        print(f"{chim11} has been added to the phonebook!\n")

    elif chim10 == '2':
        chim12 = input("Contact name:")
        if chim12 in chim9:
            print(f"{chim12} is in the phonebook!(Phone number: {chim9[chim12]})\n")
        else:
            print(f"Contact {chim12} has not been saved. \n")

    elif chim10 == '3':
        chim13 = input("Type in contact name to delete: ")
        if chim13 in chim9:
            chim9.pop(chim13)
            print(f"{chim13} has successfully been deleted!\n")
        else:
            print(f"{chim13} does not exist in phonebook.\n")

    elif chim10 == '4':
        print("Goodbye!\n")
        break

    else: 
        print("Invallid option. Please try again")


