#1
a = int(input("Enter the first one:"))
b = int(input("Enter the second one:"))
print ("The sum is:", a + b)

#2
name = str(input("Name?:"))
age = int(input("Age?:"))
print(name, "is", age, "years old.")

#3
while True:
    try:
        number = input("Type a good number!")
        number = int(number)
        print("good number!")
        break
    except ValueError:
        print("bad number:(")

#4
while True:
    try:
            a, b, c = input("Enter 3 numbers, I will pick out the largest for you:").split()
            a = int(a)
            b = int(b)
            c = int(c)
            print("The largest number is:", max(a, b, c))
            break
    except ValueError:
       print("nuh:( ")
