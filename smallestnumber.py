smallest = None

for i in [8,9,67,5,4,3,2]:
    if smallest == None:
        smallest = i
    elif i < smallest:
        smallest = i
print(smallest)
