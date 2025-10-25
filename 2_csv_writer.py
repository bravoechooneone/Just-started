import csv

data=[
['Name','Age','City'],
['Alice',25,'Wonderland'],
['Bob',30,'NewYork'],
['Charlie',28,'Oklahoma']
]
with open('example.csv', 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data)
print('CSV file created successfully')