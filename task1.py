import csv

with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        rows = row['Images']
        if len(rows.split(',')) > 3:
            data.append(row)

with open('task_1.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Id", "Images", "Title", "Description", "Price"], delimiter=",",
                            lineterminator="\r")
    writer.writerows(data)