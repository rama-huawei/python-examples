counts = dict()
line = input("enter the numbers which needs to be counted")
names = line.split() 
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

for i in counts:
    print("key is: ", i, "and value is: ", counts[i])

print(list(counts))

print(counts.keys())

print(counts.values())

print(counts.items())

print(counts)
