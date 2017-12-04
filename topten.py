temp = 0 
counts = {}
fhandler = open("temp.txt")
for line in fhandler:
    words = line.split()     
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


lst = []

for k,v in counts.items():
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val,key in lst[:5]:
    print(key,val)
