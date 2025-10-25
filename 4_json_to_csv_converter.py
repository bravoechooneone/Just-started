import json
import csv

with open("data.json", "r") as jf:
    data = json.load(jf)
    
with open("converted.csv", "w", newline="") as cf:
    writer = csv.DictWriter(cf,fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("JSON converted to CSV successfully!")