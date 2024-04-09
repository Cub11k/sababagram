from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class BusinessOpeningHoursInterval(BaseTelegramType):
    """


    Source: https://core.telegram.org/bots/api#businessopeninghoursinterval
    """

    opening_minute: int
    """
    The minute's sequence number in a week, starting on Monday, 
    marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60
    """
    closing_minute: int
    """
    The minute's sequence number in a week, starting on Monday, 
    marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60
    """
