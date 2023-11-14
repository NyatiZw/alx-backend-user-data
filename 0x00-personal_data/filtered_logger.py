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


if __name__ == "__main__":
    pass
