from datetime import datetime, timezone
from dateutil import parser


"""
Copied content from abalage/whatsthedamage/src/whatsthedamage/utils/date_converter.py
"""


class DateConverter:
    @staticmethod
    def convert_from_epoch(epoch: float, date_format: str) -> str:
        """
        Convert an epoch time to a date string.

        :param epoch: The epoch time to convert.
        :param date_format: The format to convert the epoch time to (e.g., '%Y.%m.%d').
        :return: The formatted date string, or None if conversion fails.
        :raises ValueError: If the epoch value is invalid.
        """
        if epoch:
            try:
                date_obj = datetime.fromtimestamp(epoch, tz=timezone.utc)
                return date_obj.strftime(date_format)
            except (ValueError, OverflowError, OSError):
                raise ValueError(f"Invalid epoch value '{epoch}'")
        raise ValueError("Epoch value cannot be None or empty")


    @staticmethod
    def convert_date_format(date_str: str, date_format: str) -> str:
        """
        Convert a date string to the specified format.

        :param date_str: The date string to convert.
        :param date_format: The format to convert the date string to (e.g., '%Y-%m-%d').
        :return: The formatted date string.
        :raises ValueError: If the date format is not recognized.
        """
        try:
            date_obj: datetime = parser.parse(date_str)
            return date_obj.strftime(date_format)
        except ValueError:
            raise ValueError(f"Date format for '{date_str}' not recognized.")
