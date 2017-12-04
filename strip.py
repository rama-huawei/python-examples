# baby name
var = "     dakshitreddy    "

#find functionallity
find = var.find("reddy")

print(find)

#strip functionallity

print("before", var)
rvar = var.rstrip()
print("after rstrip", rvar)
lvar = var.lstrip()
print("after lstrip", lvar)
stripVar = var.strip()
print("after strip", stripVar)

#uppercase

upperCase = stripVar.upper()

print(upperCase)

#lowercase

lowerCase = stripVar.lower()
print(lowerCase)


#startswith
flag = var.startswith("    ")
print(flag)

#notstartswith
flag = var.startswith("Hit")
print(flag)
