class Dog:
    species = "Canis familiaris"

    def __init__(self,name):
        self.name=name
        self._tricks=[] #"protected" (by convention)
        self.__mood= "happy" #name-mangled private variable

    #public method
    def add_trick(self, trick):
        self._tricks.append(trick)

    #controlled access to private data
    def get_tricks(self):
        return list(self._tricks) #return a copy (encapsulation)
    
    def get_mood(self):
        return self.__mood
    

d = Dog("Fido")
e = Dog("Buddy")

d.add_trick("roll over")
d.add_trick("play dead")

print(d._tricks) # single underscore is just a "convention", means "this is internal, don't touch directly
#" but is still accessible if you insist

#print(d.__mood) #attribute error, because mood is private

print(d.get_mood())

#don't do this in actual code
print(d._Dog__mood) #Name mangling prevents accidental access, not malicious access

# some useful methods 

print(hasattr(d, "name"))
print(hasattr(d, "_tricks"))

print(getattr(d,"name"))
print(getattr(d,"age","unknown")) #give default or throws error if doens't exist

setattr(d,"age",5)
print(d.age)

print(dir(d)) #shows instance attributes, methods, inherited attributes, mangled private attributes

print(vars(d)) #shows what belongs to the instance, the namespace