counts = dict()
filename = input("enter file name")
handle = open(filename)
for line in handle:
    words = line.split()
    for word in words:
            counts[word]  = counts.get(word, 0) + 1

print(counts)

bigword = None
bigcount = None

for word,count in counts.items():
   if bigcount is None or count > bigcount:
       bigword = word
       bigcount = count

print(bigword, bigcount)
