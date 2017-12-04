filename = input("enter the file name")

counts = dict()

handle = open(filename, 'r')
print(handle)

for line in handle:
    words = line.split()
    for word in words:
        if word == "word" or word == '=' or word == "for" or word == "else" or word == "not" or word == "input('enter': 1, 'the': 1, 'file': 1, 'name')":
            continue
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts.get(word, 0) + 1

print(counts)
list = []
for value in sorted(counts.values()):
     print(value)    

BigName = None
BigCount = None

for name, count in counts.items():
    if BigCount is None or count > BigCount:
        BigName = name
        BigCount = count
print("==========================================")
print("Number of occuerencs of", BigName, "name is", BigCount)


