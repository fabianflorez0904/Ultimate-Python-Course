import csv


data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Chicago"]
]

with open("archivos/data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open("archivos/data.csv", "r") as file:
    reader = csv.reader(file)
    print(type(reader), reader)
    for row in reader:
        print(row)
