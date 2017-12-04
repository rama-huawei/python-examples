number = int(input("enter the number"))
a = []

for i in range(2, number + 1):
    if (number % i == 0 ):
        break
print(i)
