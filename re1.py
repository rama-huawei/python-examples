import re

count = 0
hand = open('temp.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)
        count = count + 1
print(count)
