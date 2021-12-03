import csv
import pandas
rc = []
rb = []

f = open("test.csv", 'r')
with f:
    reader = csv.reader(f)
    print("reader: ", reader)
    for row in reader:
        rc.append(row)
        
# print("rc: ", rc)

with open('../../runner/data/runner.csv', 'r', encoding='gbk') as f:
    reader = csv.DictReader(f)
    print("reader: ", reader)
    for row in reader:
        rb.append(row)
       
print("rb: ", rb)
