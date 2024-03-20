# custom_logger.py
import logging

class BinaryFilter(logging.Filter):
    def filter(self, record):
        # Check if the log message contains binary data
        if isinstance(record.msg, bytes):
            return False  # Skip logging binary data to the console
        return True  # Allow logging text data to the console

def get_logger(log_file: str, repo_url: str) -> logging.Logger:
    # Create a custom formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - {repo_url} - %(message)s'.format(
        repo_url=repo_url,
    ))

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.addFilter(BinaryFilter())

    # Create a logger and set the log level
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Add the console handler to the logger for debug and error levels
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    return logger
