import csv 
import os
from collections.abc import Iterable
print(os.getcwd())
file = open('airport_codes.csv','r')
#print(type(file))
csv_reader = csv.reader(file)
#print(type(csv_reader))

rows = list(csv_reader)
#or below works
#rows = [row for row in csv_reader]

#print(rows)

airports_full_names= [airport for code,airport in rows]
print(airports_full_names)

airports_codes= [code for code,airport in rows]
print(airports_codes)

airports_codes_cleaned=airports_codes[1:]

file.close()

# TODO: make 
file = open('airport_codes.csv','r')
reader = csv.DictReader(file)

# print(reader)
# for row in reader:
#         print(row['Airport Code'], row['Airport Name'])

print("as a dictionary")
airports = {row['Airport Code']: row['Airport Name'] for row in reader}   
print(airports)     




def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
    
#print(is_iterable(csv_reader))
#or check this way

#print(isinstance(csv_reader,Iterable))









# In Python, the open() function has several modes that determine how a file is opened. Here are the most common modes:

# 'r': Read (default mode). Opens a file for reading. The file must exist.

# 'w': Write. Opens a file for writing, truncating the file first. If the file does not exist, it creates a new file.

# 'a': Append. Opens a file for writing, appending to the end of the file if it exists. Creates a new file if it does not exist.

# 'b': Binary mode. This can be added to other modes (e.g., 'rb' or 'wb') to read or write binary files.

# 't': Text mode (default). This can be added to other modes (e.g., 'rt' or 'wt') to read or write text files.

# 'x': Exclusive creation. Opens a file for writing, failing if the file already exists.

# 'r+': Read and write. Opens a file for both reading and writing. The file must exist.

# 'w+': Write and read. Opens a file for both writing and reading, truncating the file first. Creates a new file if it does not exist.

# 'a+': Append and read. Opens a file for both appending and reading. Creates a new file if it does not exist.