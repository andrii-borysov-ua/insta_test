import logging
import os
import sys

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler('test.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger