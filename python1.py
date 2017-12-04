dunder methods:
def __init__()
def __str__()
def __repr__()
int.__add__(1,2)
str.__add__(a,b)
print('test'.__len__())

property decorator methods:
@property is specified for a method then we call that method as a attribute instead of a method.
@fullname.setter  is specified for a setter method then we call that setter method as a attribute instead of a method. 
@fullname.deleter  is specified for a deleter method then we call that deleter method as a attribute instead of a method and assign first and last attributes to None. 


regular instance methods
class methods
static methods 

Inheritance:
inherting all the properties from parent class to child class is nothing but inheritance

in inheritance we have isinstance and issubclass methods to check whether the insance belongs to this class or not.
is subclass is used to check whether the given class is belongs to subclass or not of a parent class.

