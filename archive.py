import csv
data = []
with open("archive_dataset.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
headers = data[0]
planet_data = data[1:]
for data_point in planet_data:
    data_point[2] = data_point[2].lower()
planet_data.sort(key = lambda planet_data:planet_data[2])
with open("archive_dataset_sorted.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data) 
with open('archive_dataset_sorted.csv') as input, open('archive_dataset_sorted1.csv', 'w', newline='') as output:
     writer = csv.writer(output) 
     for row in csv.reader(input):
        if any(field.strip() for field in row):
             writer.writerow(row)
