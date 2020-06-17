import sys
import logging

# logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
# logFormatter = '%(asctime)s - %(user)s - %(levelname)s - %(message)s'
# logging.basicConfig(format=logFormatter, level=logging.WARNING)

logging.basicConfig()
logger = logging.getLogger(__name__)

handler = logging.FileHandler('myLogs.log')
handler.setLevel(logging.WARNING)
logger.addHandler(handler)


def capture_exception():
    return sys.exc_info()


def print_exception():
    try:
        1/0
    except:
        print(capture_exception())


def log_levels():
    logger.critical("this better be bad")
    logger.error("more serious problem")
    logger.warning("an unexpected event")
    logger.info("show user flow through program")
    logger.debug("used to track variables when coding")


def log_file():
    logger.warning('You can find this written in myLogs.log')


if __name__ == '__main__':
    print_exception()

    logger.critical('logging is easier than I was expecting')

    log_levels()

    logger.error('wrong purchase completed', extra={'user': 'Donald Trump'})

    log_file()
