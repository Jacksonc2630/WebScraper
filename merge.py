import csv
data1 = []
data2 = []

with open("final.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data1.append(row)

with open("archive_dataset_sorted1.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data2.append(row)

headers1 = data1[0]
planet_data1 = data1[1:]

headers2 = data2[0]
planet_data2 = data2[1:]

headers = headers1 + headers2
planet_data  = []
for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("merge.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data) 

with open('merge.csv') as input, open('merge1.csv', 'w', newline='') as output:
     writer = csv.writer(output) 
     for row in csv.reader(input):
        if any(field.strip() for field in row):
             writer.writerow(row)