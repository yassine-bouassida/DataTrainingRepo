from abc import ABC, abstractmethod

#from yesteryday with functions

# you can even add functions as arguments in your functions
def called_function():
    return "this is called by the outter function"

def calls_outer_function(func1):
    return func1()

print(calls_outer_function(called_function))
#leave off the parentheses when passing in the function as an argument

# basic class syntax if the class keyword, ClassName:, init under method (add instance variables here), then associated function

class MyNewClass:
    #this sets up he constructor for the class. There can only be one
    #notice you can set default values for the parameteres by declaring them within the ()
    def __init__(self, age = 0, name ="default name"):
        self.name = name 
        self.age = age 

    def my_new_class_function(self): # first parameter is always a reference to self, doesn't have to be called self
        return f"My name is {self.name} and I am {self.age} years old."
    #note we should use self instead of jeeves, but this is just to illustrate the point

    # the __str__ method allows you to define what happens when you print an instance of the class
    def __str__(self):
        return f"MyNewClass(name={self.name}, age={self.age} from the to string method)"
    
    # the __repr__ method allows you to create a clone of the class. I could create a new variables and call this method to create a clone of the object
    def __repr__(self):
        return f"MyNewClass(self, {self.age},{self.name})"

# the self parameter is included because Python, under the hood, is actually using the class to call the function,
# and the particular object you want to use is being passed  as the first parameter

my_instance = MyNewClass(25, "Will")
print(my_instance.my_new_class_function())

my_class = MyNewClass()
print(my_class.__str__())
print(MyNewClass.__str__(my_class))  # equivalent to the above line
print(my_class)  # implicitly calls __str__()

#Python supports abstract classes. You make a class abstract by adding ABC inside the parentheses
class MyAbstractClass(ABC):

    #this is a class variable, accessed by calling the class itself, not an instantiated object
    class_count: int = 0

    #class methods take in the class as an implicity first argument,  can interact with and change the state of the class
    @classmethod
    def print_class_count(cls) -> int: 
        return cls.class_count
    #class methods take in the class as an implicity first argument,  can interact with and change the state of the class

    #static methods don't take in an implicit first argument, they behave like regular functions but belong to the class's namespace
    #static methods do not receive the class or an instance of the class as an implicit argument. You can add it,
    #but you might as well use a class method at that point
    @staticmethod
    def static_method_example():
        return "This is a static method example"
    
    #abstract methods have no body: they need to be defined in their child class
    @abstractmethod
    def abstract_method(self):
        pass


print(MyAbstractClass.class_count)
print(MyAbstractClass.print_class_count())
print(MyAbstractClass.static_method_example())

class MyInheritsTheAbstractClass(MyAbstractClass):
    def __init__(self):
        print("I inherited from the abstract class")
        MyAbstractClass.class_count +=1

    #you can now define what the abstract method does within the child class
    def abstract_method(self):
        return "This is the implementation of the abstract method"

class AlsoInheritsAbstractClass(MyAbstractClass):
    def __init__(self):
        print("I also inherited from the abstract class")
        MyAbstractClass.class_count +=1

    def abstract_method(self):
        return "This is another implementation of the abstract method"
    
my_abstract_instance = MyInheritsTheAbstractClass()
print(my_abstract_instance.print_class_count())
another_abstract_instance = AlsoInheritsAbstractClass()
print(another_abstract_instance.print_class_count())

print(my_abstract_instance.abstract_method())
print(another_abstract_instance.abstract_method())

class OuterClass:
    def __init__(self, number, word, inner_class="my inner class"):
        self.number = number
        self.word = word
        self.create_inner_class(inner_class)

    class InnerClass:
        def __init__(self, name):
            self.name = name
            print("the inner class has been created")
        
    def create_inner_class(self, name):
        self.inner_class = self.InnerClass(name)

    def __str__(self):
        return f"my number is {self.number}, my word is {self.word}, and my inner class name is {self.inner_class.name}"
    

outer_instance = OuterClass(10, "hello", "inner instance")
print(outer_instance)

class InheritedConstructor:
    def __init__(self,name):
        self.name = name
        print("the parent constructor was called")

class InheritsConstructor(InheritedConstructor):
    def __init__(self, age, name):
        super().__init__(name) #calls the parent constructor
        self.age = age
        print("the child constructor was called")


inherited_instance = InheritsConstructor(30, "Will")
#print(f"name: {inherited_instance.name}, age: {inherited_instance.age}")

######################################################################
# this is global, it can actually be referenced in other modules if you import it
# and it is available inside methods within this module
name="Will"

def local_and_enclosed():
    name="Sam" # this is local, it is available insde the function but not outside
    def enclosed(): #a function within a function is an enclosed namespace: same lifecycle as its parent function
        #and access to its variables
        return name # will return Sam, since the enclosed function has access to the paren function's local block
        #you will get an error if you try and just return name without defining it in the local block before the enclosing block
    print(enclosed()) # this prints sam
    name="Luke"
    return name #this now returns Luke, since it is the local assignment to the variable

print(name) #prints Will
print(local_and_enclosed()) #prints Sam first because of the enclosed() method, then it prints Luke because of the local assignment

########################
class Num:
    def __init__(self,number):
        self.number = number

    def __add__(self, other):
        return self.number + other*100

num: Num = Num(10)
print(num.number)

x:int = num.__add__(5)  # returns 15
print(x)

print(num + 5)  # also returns 15 because of operator overloading 

##############################################################################
l:list = [1, 2, "three", 4, 5, 2]
s:set = {1,2,3,4,5}  # sets automatically remove duplicates
t:tuple = (1, "two", 3.0, True, 1)  # tuples are immutable lists
d:dict = {"one": 1, "two": 2, "three": 3, "threee": 3}  # dictionaries store key-value pairs

#LISTS

l.append(6)
print(l)
appended_list = l + [7, 8, 9]  # creates a new list
print(appended_list)
appended_list.append([10,11,12])
print(appended_list)

final_numbers = [5,6,7,8]
appended_list.extend(final_numbers)  # extends the list with another list
print(appended_list)


appended_list.insert(0, "start")  # inserts at index 0
print(appended_list)

#list.pop([index]) removes and returns the item at the given index. If no index is specified, it removes and returns the last item
print(appended_list.pop())  # removes and returns the last item
print(appended_list)

#list.remove(value) removes the first occurrence of the value. Raises ValueError if the value is not found
appended_list.remove(5)
print(appended_list)

#list.clear() removes all items from the list
app_list= appended_list.copy()
#app_list= appended_list
app_list.clear()
print("app_list")
print(app_list)
print("appended_list")
print(appended_list)

#list.index(value, [start, [end]]) returns the index of the first occurrence of the value. Raises ValueError if the value is not found
index_of_two = appended_list.index(2)

#list.count(value) returns the number of occurrences of the value
print(appended_list.count(7))

print("sorting example")
to_sort_numbers= [5,3,8,1,2,7,4,6]
print(to_sort_numbers)
to_sort_numbers.sort()  # sorts the list in place
print(to_sort_numbers)

sort_using_key=[(1,"c"), (2,"a"), (3,"b")]
def my_key(element):
    return element[1] #takes the second element of the tuple for sorting

sort_using_key.sort(key=my_key)
print(sort_using_key)

print(to_sort_numbers[::-1])  # prints the list in reverse order without modifying the original list
print(to_sort_numbers)  # original list remains unchanged

print("using reverse method")

to_sort_numbers.reverse()  # reverses the list in place
print(to_sort_numbers)

###Sets 

well:str = "well"
lets = "let's"
see= "see"

my_set={1}
my_set.add(2)
my_set.add(lets)
my_set.add(well)
my_set.add(see)
print(my_set)

my_set.add(2)  # adding a duplicate does nothing
print(my_set)

new_list=[1,6,5,4,2,0,1,7,8,3,2,9,1]
y:list = list(set(new_list))
print(y)

#set.pop() removes and returns an arbitrary element from the set. Raises KeyError if the set is empty
popped_element = my_set.pop()
print(f"popped element: {popped_element}")
popped_element2 = my_set.pop()
print(f"popped element: {popped_element2}")
print(my_set)

#set.remove(value) removes the specified value from the set. Raises KeyError if the value is not found
#set.discard(value) removes the specified value from the set. Does nothing if the value is not found
my_set.remove(well)
print(my_set)
my_set.discard("nonexistent")  # does nothing

#set.update(other_set) adds all elements from other_set to the set
another_set={3,4,5}
my_set.update(another_set)
print(my_set)

###TUPLES
print(appended_list)
appended_list[3]= "changed value"
print(appended_list)

tuple_example=(1,2,3,"four",5,1,2)
print('should print tuple example')
print(tuple_example)
#tuple_example[2]= "changed value"  # this will raise an error because tuples are immutable

tuple_example_count= tuple_example.count(1)
print(tuple_example_count)

#tuple.index(value) returns the index of the first occurrence of the value. Raises ValueError if the value is not found
tuple_example_index= tuple_example.index(2)
print(tuple_example_index)

#dictionaries

def inside_the_dictionary():
    return "function key"

my_dictionary = {
    "key": "value",
    100: 1000,
    "string key": 5,
    10: "string value",
    None: "this still works",
    "can also do this": None,
    "function": inside_the_dictionary(),
    inside_the_dictionary(): "does this work"
}

print(my_dictionary)
print(my_dictionary["key"])

my_dictionary["new key"]= "new value"
print(my_dictionary)

print(my_dictionary.items()) # returns a view object that displays a list of a dictionary's key-value tuple pairs

#dic.setdefault(key, default=None) returns the value of the key if it is in the dictionary. If not, it inserts the key with the default value   
print(my_dictionary.setdefault("key", "default value"))  # returns "value"
print(my_dictionary.setdefault("nonexistent", "default value"))  # returns "default value" and adds the key-value pair to the dictionary
print(my_dictionary)