#!/usr/bin/env python3
"""
Implementing a log filter that will obfuscate PII fields
"""


import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class

    Attributes:
    - REDACTION (str): The string used for redaction
    - FORMAT (str): The log message format
    - SEPARATOR (str): The field separator in log messages

    Methods:
    - __init__(self, fields: List[str]): Constructor method
    -format(self, record: logging.LogRecord) -> str: Formats records
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter

        Args:
        - fields (List[str]): A list of strings representing fields
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log records with redacted fields

        Args:
        - record (logging.LogRecord): The log record to format

        Returns:
        - str: The formatted log message
        """
        def filter_datum(fields, redaction, message, separator):
            return re.sub(
                    f'({separator.join(fields)}){separator}(.*?){separator}',
                    f'\\1{redaction}{separator}',
                    message
                )

        record.msg = filter_datum(
                self.fields,
                self.REDACTION,
                record.msg,
                self.SEPARATOR
            )
        return super(RedactingFormatter, self).format(record)


"""Define PII_FIELDS with the fields considered"""
PII_FIELDS = ('name', 'email', 'phone', 'address', 'credit_card')


def get_logger() -> logging.Logger:
    """
    Get a configured logging.Logger object

    Returns:
    - logging.Logger: Configured logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

    logger.proagate = False

    stream_handler = StreamHandler()
    redacting_formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(redacting_formatter)

    logger.addHandler(stream_handler)

    return logger


if __name__ == "__main__":
    logger = get_logger()

    with open('user_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            logger.info("User data: %s", row)
