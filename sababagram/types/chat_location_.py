from dataclasses import dataclass

from .base import BaseTelegramType
from .location_ import Location


@dataclass
class ChatLocation(BaseTelegramType):
    """
    Represents a location to which a chat is connected.

    Source: https://core.telegram.org/bots/api#chatlocation
    """

    location: Location
    """
    The location to which the supergroup is connected. Can't be a live location.
    """
    address: str
    """
    Location address; 1-64 characters, as defined by the chat owner
    """
