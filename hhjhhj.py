#1
a = [4, 6, 8, 10, 11, 13]
print("Sum:", sum(a))
print("Average:", sum(a) / len(a))

#2
chim2 = []
for i in range(5):
    chim1 = input(f"Type in the fruit {i+1}: ")
    chim2.append(chim1)
chim2.sort()
print("This is the list of fruits, sorted", chim2)

#3
chim3 = [1,2,2,3,4,4,5]
chim4 = list(dict.fromkeys(chim3))
print("List:", chim4)

#4
def chim5(chim6):
    return[l for l in chim6 if l % 2 == 0]
print("Even numbers:", chim5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#5
chim6 = [chim ** 2 for chim in [1, 2, 3, 4, 5]]
print("Square numbers:", chim6)



