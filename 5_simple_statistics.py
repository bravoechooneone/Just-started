import csv
import statistics

values=[]

with open('numbers.csv', 'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        values.append(float(row['value']))
print('Mean: ',statistics.mean(values))
print('Median: ',statistics.median(values))
print('Mode: ',statistics.mode(values))