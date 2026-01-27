# print("hello world")

my_number: int = 5
my_string: str = "This is a string"
my_string_number: float = "This is a string despite saying I expect a float"

# print(type(my_number))
# print(type(my_string))
# print(type(my_string_number))
# The above line will not raise an error, but my_string_number will be of type str, not float.

#numeric datatypes are integers and floats
my_float: float = 5.99
# print(type(my_float))
my_integer: int = 5

#string is the data type for text
my_string: str = "Hello World"
# print(type(my_string))

#booleans can either be True or False
my_boolean: bool = True
# print(type(my_boolean))
my_other_boolean: bool = False
# print(type(my_other_boolean))
#notice the first letter is capitalized for boolean values

#None can be assigned as a type: useful for avoiding errors
""" my_none: None = None
print(type(my_none))

my_string_literal = 'This is also a string'
print(type(my_string_literal)) """

# You can concatenate strings using the + operator and add variables into string with interpolation

name: str = "Alice"
interpolated_greeting: str = "Hello, " + name + "!"

# print(interpolated_greeting)
f_interpolated_greeting: str= f"Hello, {name}!"

#you can also use the .format() method to format your string
formatted_greeting: str = "Hello, {}!".format(name)

my_string = "Hello Will"
just_hello = my_string[0:5]  # Slicing to get "Hello"
print(just_hello)

my_string2 = my_string[::]  # Copying the entire string


reversed_string = my_string[::-1]  # Reversing the string

every_second_character = my_string[::2]  # Getting every second character

every_second_character = my_string[::-2]  # Getting every second character in reverse
print(every_second_character)

# use a negative number to work backwards through a string (-1 is the last character, -2 is the second to last, etc.)
using_negative_indexing = my_string[-5:]  # Getting the last 5 characters
print(using_negative_indexing)

# or if you want to leave of the last five characters
leaving_off_last_five = my_string[:-5]  # Leaving off the last 5 characters
print(leaving_off_last_five)

def basic_function() -> None:
    """This is a basic function that prints a greeting."""
    print("Hello from the basic function!")

basic_function()

def basic_function_with_params(name):
    """This function takes a name as a parameter and prints a personalized greeting."""
    print(f"Hello, {name}!")

basic_function_with_params ("Bob")

def plus_or_concat(obj1, obj2):
    return obj1 + obj2

print(plus_or_concat(5, 10))          # Outputs: 15
print(plus_or_concat("Hello, ", "World!"))  # Outputs: Hello, World!

this_is_a_tuple = (1, "apple", 3.14, True)
#you can add a variable to the end of the parameters called a variable arguemtn, which allows you to pass in any number of arguments
def variable_args_function(*args):
    for element in args:
        print(element)
variable_args_function("apple", 1, "cherry")
variable_args_function(this_is_a_tuple)

def keyword_args_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

keyword_args_function(name="Alice", age=30, city="New York")



