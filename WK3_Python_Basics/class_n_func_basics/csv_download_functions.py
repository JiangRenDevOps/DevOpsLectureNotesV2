import csv


def csv_reader_read_file(filename: str):
    with open(filename) as f:
        csv_file = csv.reader(f, delimiter=',')
        for row in csv_file:
            print(row)

            
if __name__ == '__main__':
    csv_reader_read_file('../csv_files/AAPL.csv')
    csv_reader_read_file('../csv_files/TEAM.csv')
