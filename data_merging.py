import pandas as pd
import csv

csv_1= "star_data.csv"
csv_2= "dwarf_stars.csv"

data_1=[]
data_2=[]

with open(csv_1, "r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        data_1.append(i)

with open(csv_2, "r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        data_2.append(i)

h1= data_1[0]
h2= data_2[0]

d1= data_1[1:]
d2= data_2[1:]

header= h1+h2
data=[]

for i in d1:
    data.append(i)
for i in d2:
    data.append(i)

with open("merged_data.csv", "w") as f:
    csv_writer= csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(data)