class Employee:
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee("rama","subbareddy",500000)
emp2 = Employee("saritha", "reddy",500000)

print emp1.fullname()
