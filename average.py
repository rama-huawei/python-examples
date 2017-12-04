#Python Program to Calculate the Average of Numbers in a Given List

numbers = int(input("enter the list of numbers to be inserted"))
a = []

for i in range(numbers):
    number = int(input())
    a.append(number)

average = sum(a)//numbers
print("The average of given list of elments is ", average)

