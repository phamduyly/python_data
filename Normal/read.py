import csv

with open('Test3.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', )

with open('Test2.csv', encoding="utf8") as csv_file2:
    csv_reader = csv.reader(csv_file, delimiter=',', )


with open('update.csv', 'w') as outFile:
    for line in csv_file:
        if line not in csv_file2:
            outFile.write(line)