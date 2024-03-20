# custom_logger.py
import logging

class BinaryFilter(logging.Filter):
    def filter(self, record):
        # Check if the log message contains binary data
        if isinstance(record.msg, bytes):
            return False  # Skip logging binary data
        elif "STREAM" in record.msg:
            return False  # Skip logging binary data to the console
        return True  # Allow logging text data

def get_logger(log_file: str, repo_url: str) -> logging.Logger:
    # Create a custom formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - {repo_url} - %(message)s'.format(
        repo_url=repo_url,
    ))

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    # Create an instance of BinaryFilter for the file handler
    file_binary_filter = BinaryFilter()
    # Add the BinaryFilter to the file handler
    file_handler.addFilter(file_binary_filter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_binary_filter = BinaryFilter()  # Create an instance of the filter for console
    console_handler.addFilter(console_binary_filter)  # Add the filter to the console handler

    # Create a logger and set the log level
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Add the console handler to the logger for debug and error levels
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    return logger
