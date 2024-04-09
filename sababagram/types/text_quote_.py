from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .message_entity_ import MessageEntity


@dataclass
class TextQuote(BaseTelegramType):
    """
    This object contains information about the quoted part of a message that is replied to by the
    given message.

    Source: https://core.telegram.org/bots/api#textquote
    """

    text: str
    """
    Text of the quoted part of a message that is replied to by the given message
    """
    position: int
    """
    Approximate quote position in the original message in UTF-16 code units as specified by the sender
    """
    entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. Special entities that appear in the quote. Currently, only *bold*, *italic*, 
    *underline*, *strikethrough*, *spoiler*, and *custom_emoji* entities are kept in quotes.
    """
    is_manual: Optional[bool] = None
    """
    *Optional*. True, if the quote was chosen manually by the message sender. Otherwise, 
    the quote was added automatically by the server.
    """
