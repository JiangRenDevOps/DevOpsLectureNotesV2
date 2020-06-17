import csv
from WK3_Python_Basics.class_n_func_basics.utils import logger


class CsvDownloader:
    def __init__(self, filename: str):
        self.logger = logger.Logger('WARNING', self.__class__.__name__).get_logger()
        self.filename = filename
        self.data = {}
        self.csv_reader_read_file()

    def csv_reader_read_file(self):
        with open(self.filename) as f:
            csv_file = csv.reader(f, delimiter=',')
            for row in csv_file:
                self.data[row[0]] = {}
                self.data[row[0]]['adj_close'] = row[-2]
                self.data[row[0]]['volume'] = row[-1]
                self.logger.warning(f'{self.data[row[0]], self.data[row[0]]["adj_close"], self.data[row[0]]["volume"]}')

    def adj_close_by_date(self, date: str):
        return self.data[date]


if __name__ == '__main__':
    aapl_csv = CsvDownloader('../csv_files/AAPL.csv')
    print(aapl_csv.adj_close_by_date('2019-06-19'))

