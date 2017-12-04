class HelloWorld1:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def display(self):
        print("rama")
        return "The first name is {} last name is {} and the pay is {}".format(self.first, self.last, self.pay)

obj1 = HelloWorld1("Dakshit", "Reddy", 9000000)
print(obj1.display())
obj2 = HelloWorld1("Saritha", "Reddy", 9000000)
print(obj2.display())

