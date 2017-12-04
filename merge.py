#The program takes two lists, merges them and sorts the merged list.

a = []
b = []

list1 = int(input("enter the number of elements in list1"))

list2 = int(input("enter the number of elementes in list2"))

for i in range(0, list1):
    number = int(input("enter the element"))
    a.append(number)

for i in range(0, list2):
    number = int(input("enter the element"))
    b.append(number)

merge = a + b

merge.sort()

print(merge)
