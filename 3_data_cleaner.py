import csv

cleaned_rows=[]
with open('raw_data.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        if any(row):
            cleaned_rows.append([cell.strip()for cell in row])

with open('cleaned_data.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(cleaned_rows)

print('cleaned data saved to cleaned_data.csv')