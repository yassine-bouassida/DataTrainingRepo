import csv, json

#just need a dictionary so I can test our the DictWriter
file = open('airport_codes.csv','r')
reader = csv.DictReader(file)
print("as a dictionary")
airports = {row['Airport Code']: row['Airport Name'] for row in reader}  
print(airports)
file.close()


with open('airport_codes_from_dict.csv','w') as file:
    csv_writer = csv.DictWriter(file,fieldnames=['Airport Codes','Airport Name'])
    rows = [{'Airport Codes': code, 'Airport Name': name} for code, name in airports.items()]
    csv_writer.writerows(rows)

with open('airport_codes_from_dict.json','w') as f:
  json.dump(airports, f)