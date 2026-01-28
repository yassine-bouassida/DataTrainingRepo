
#bad_math = 5/0 # this will raise a ZeroDivisionError

#placing the code above inside a try/except block gives us a chance to handle the exception
# try:
#     bad_math = 5/0
# except ZeroDivisionError:
#     print("You cannot divide by zero!")

# you can have multiple except blocks with need to go from specific to general
try:
    5/"0"  
except ZeroDivisionError: # this only triggers if the try code causes a ZeroDivisionError
    print("You cannot divide by zero!")
except TypeError: # this only triggers if the try code causes a TypeError  
    print("You cannot divide by a string!")
except Exception: # this will trigger for any exception not caught by the above except blocks
    print("An unknown error occurred.")

#you can create your own custom exception
class MyException(Exception):
    def __init__(self, message): # you want the message parameter so you can include a custom message when you raise the exception
        self.message = message

try:
    raise MyException("This is my custom exception message!") # this tells the app that it  needs to handle our custom exception we created
#the sting in () is the message that will be passed to the MyException class
except MyException as e: # e is the identifier for the exception object that was raised
    print(f"Caught my custom exception: {e.message}") # we can access the message attribute of the exception object to get the custom message