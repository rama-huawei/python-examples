class A():
    def __init__(self,name):
        self.name=name

a = A('mary')
b=a
del b
print a.name 