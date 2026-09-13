import math
#1
x = int(input("Type a good number:"))
print("Square root of that number is:", math.sqrt(x))

#2
y = int(input("Give me a good radius, I will calculate some stuff for you!"))
print("A circle with", y, "will have an area of", math.pi * y**2, "!")

#3
pii = round(math.pi, 3)
print("Here is pi, rounded to 3 decimal places:", pii)

#4
while True:
    try:
        x, y = map(int, input("Give me two numbers to find gcd of!").split())
        print("gcd of those numbers is:", math.gcd(x, y))
        break
    except ValueError:
        print("You didn't gave two good numbers:^ ")

#5
while True:
    try:
        x = int(input("Give me number to find factorial number of!"))
        print("factorial number of that number is:", math.factorial(x))
        break
    except ValueError:
        print("You didn't gave a good number:^ ")
