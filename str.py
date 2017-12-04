def remove(string, n):  
      first = string[:n]
      print first
      last = string[n+1:]  
      print last
      return first + last

str = raw_input("enter the string")
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(str, n))


rama
0123
