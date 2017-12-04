import re
x = 'My 2 favorite numbers are 19 and 42'

y = re.findall('[s]', x)
s = x.find('s')
print(y, s)
