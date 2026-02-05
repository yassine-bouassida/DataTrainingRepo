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

# #let's try writing a csv
# file = open('airport_codes2.csv','w')
# csv_writer = csv.writer(file)
# rows_no_header= rows[1:]
# for row in rows_no_header:
#     csv_writer.writerow(row)
# file.close()

#we could write all the rows at once
file = open('airport_codes2.csv','w')
csv_writer = csv.writer(file)
rows_no_header= rows[1:]
csv_writer.writerows(rows_no_header)
file.close()


