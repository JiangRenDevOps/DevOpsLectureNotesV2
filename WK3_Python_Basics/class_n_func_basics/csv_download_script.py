import csv

# Could you modify this file, help me retrieve all Adj Close price for all stocks that I saved?
# Tips: firstly, identify what data structure does each row have?

filename = '../csv_files/AAPL.csv'

with open(filename) as f:
    csv_file = csv.reader(f, delimiter=',')
    for row in csv_file:
        print(row)


