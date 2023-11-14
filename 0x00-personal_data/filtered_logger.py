#!/usr/bin/env python3
"""Implementing a log filter that will obfuscate PII fields"""

import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Function that logs obfuscated data

    Args:
        fields: list of strings
        redaction: string of obfuscated fields
        message: string representing the log line
        separator: string representing char separating fields

    Returns:
        log message
    """
    return re.sub(
            f'({separator.join(fields)}){separator}(.*?){separator}',
            f'\\i{redaction}{separator}',
            message
        )


if __name__ == "__main__":
    pass
