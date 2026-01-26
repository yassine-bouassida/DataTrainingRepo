print("hello world")

my_number: int = 5
my_string: str = "This is a string"
my_string_number: float = "This is a string despite saying I expect a float"

print(type(my_number))
print(type(my_string))
print(type(my_string_number))
# The above line will not raise an error, but my_string_number will be of type str, not float.

#numeric datatypes are integers and floats
my_float: float = 5.99
print(type(my_float))
my_integer: int = 5

#string is the data type for text
my_string: str = "Hello World"
print(type(my_string))

#booleans can either be True or False
my_boolean: bool = True
print(type(my_boolean))
my_other_boolean: bool = False
print(type(my_other_boolean))
#notice the first letter is capitalized for boolean values

#None can be assigned as a type: useful for avoiding errors
my_none: None = None
print(type(my_none))

my_string_literal = 'This is also a string'
print(type(my_string_literal))

# You can concatenate strings using the + operator and add variables into string with interpolation

name: str = "Alice"
interpolated_greeting: str = "Hello, " + name + "!"

print(interpolated_greeting)
f_interpolated_greeting: str= f"Hello, {name}!"

#you can also use the .format() method to format your string
formatted_greeting: str = "Hello, {}!".format(name)









