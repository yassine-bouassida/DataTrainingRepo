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
    
my_instance = MyNewClass(25, "Will")
print(my_instance.my_new_class_function())