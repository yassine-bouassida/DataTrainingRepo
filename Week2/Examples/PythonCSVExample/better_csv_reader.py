import csv 
import os
print(os.getcwd())

with open('airport_codes.csv','r') as file:
    #print(type(file))
    csv_reader = csv.reader(file)
    #print(type(csv_reader))
    rows = list(csv_reader)
    print(rows)

#below would still work since with automatically closes the resource
file = open('airport_codes.csv','r')
csv_reader = csv.reader(file)
rows = list(csv_reader)
print("still works")
print(rows)
file.close()

