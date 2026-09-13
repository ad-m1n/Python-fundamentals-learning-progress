#1
while True:
    try:
        chim1 = int(input("Send me a number:"))
        if chim1 > 0:
            print("positive")
        elif chim1 < 0:
            print("negative")
        else:
            print("zero")
        break
    except ValueError:
        print("Try using a proper number!")

#2
while True:
    try:
        chim2 = int(input("Send me an age number:"))
        if 0 < chim2 < 13:
            print("child")
        elif 13 <= chim2 < 18:
            print("teen")
        elif 18 <= chim2 < 65:
            print("adult")
        elif chim2 >= 65:
            print("senior")
        else:
            print("Not born yet:/")
        break
    except ValueError:
        print("Try using a proper number of age!")

#3
while True:
    try:
        chim3 = int(input("Give me a year:"))
        if chim3 % 4 == 0 and chim3 % 100 != 0:
            print(chim3, "is a leap year!")
        elif chim3 % 400 == 0:
            print(chim3, "is a leap year")
        else:
            print()
        break
    except ValueError:
        print("Try again with a valid year number:)")

#4
chim4tru_usr = "chimto"
chim4tru_pwd = "chimkhongto"

chim4_usr = input("Username:")
chim4_pwd = input("Password:")

if chim4_usr == chim4tru_usr and chim4_pwd == chim4tru_pwd:
    print("Access Granted")
else:
    print("Denied")

#5
while True:
    try:
        a, b, c = map(int, input("Give me 3 numbers to sort:").split())
        if a >= b and a >= c:
            if b >= c:
                print(a, b, c)
            else:
                print(a, c, b)
        elif b >= a and b >= c:
            if a >= c:
                print(b, a, c)
            else:
                print(b, c, a)
        elif c >= a and c >= b:
            if b >= a:
                print(c, b, a)
            else:
                print(c, a, b)
        break
    except ValueError:
        print("try again with correct numbers")




