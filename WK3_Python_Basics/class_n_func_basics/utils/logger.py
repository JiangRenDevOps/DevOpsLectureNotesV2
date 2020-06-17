import logging


class Logger:

    def __init__(self, severity: str, name: str):
        # Gets or creates a logger
        self.logger = logging.getLogger(name)

        # set log level
        if severity == 'WARNING':
            self.logger.setLevel(logging.WARNING)

        # define file handler and set formatter
        self.file_handler = logging.FileHandler('logfile.log')
        self.formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        self.file_handler.setFormatter(self.formatter)

        # add file handler to logger
        self.logger.addHandler(self.file_handler)

    def get_logger(self):
        return self.logger

