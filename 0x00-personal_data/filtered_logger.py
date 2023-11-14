#!/usr/bin/env python3
"""Implementing a log filter that will obfuscate PII fields"""


import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields


    def format(self, record: logging.LogRecord) -> str:
        def filter_datum(fields, redaction, message, separator):
            return re.sub(
                    f'({separator.join(fields)}){separator}(.*?){separator}',
                    f'\\1{redaction}{separator}',
                    message
                )

        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


if __name__ == "__main__":
    pass
