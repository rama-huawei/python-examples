class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
s.party() # Sally party count 1

j = PartyAnimal("Jim")
j.party() # Jim party count 1
s.party() # Sally party count 2
j.party() # Jim party count 2
