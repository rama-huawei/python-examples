#find a number which occurs in list

#take the list of elements in a list

#enter a number which should be counted

#take  a loop check the index aganist the given number

#increase the count and print it and lets do that

n = int(input("enter a number of elements to be stored in the list"))
a = []
for i in range(0,n):
     element = int(input("enter the element"))
     a.append(element)

count = int(input("enter the element which needs to be counted"))
num = 0
for j in a:
    if count == j:
        num = num + 1

print num
