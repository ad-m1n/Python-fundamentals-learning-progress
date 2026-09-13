#1
def is_even(n):
    return n % 2 == 0

#2
def square(n):
    return n ** 2

#3
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return "is leap year"
    elif year % 400 == 0:
        return "is leap year"
    else:
        return "is not leap year"

#4
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

#5
def chimto(vai):
    chimbe = 1
    for chim in range (1, vai + 1):
        chimbe *= chim
    return chimbe
        
        

#6
def get_valid_number():
    while True:
        try:
            chim1 = int(input("Send me a number:"))
            return chim1
        except ValueError:
            print("not valid")