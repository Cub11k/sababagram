from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .location_ import Location
from .user_ import User


@dataclass
class ChosenInlineResult(BaseTelegramType):
    """
    Represents a `result <https://core.telegram.org/bots/api#inlinequeryresult>`_ of an inline query
    that was chosen by the user and sent to their chat partner.**Note:** It is necessary to enable
    `inline feedback <https://core.telegram.org/bots/inline#collecting-feedback>`_ via  in order to
    receive these objects in updates.

    Source: https://core.telegram.org/bots/api#choseninlineresult
    """

    result_id: str
    """
    The unique identifier for the result that was chosen
    """
    from_user: User
    """
    The user that chose the result
    """
    query: str
    """
    The query that was used to obtain the result
    """
    location: Optional[Location] = None
    """
    *Optional*. Sender location, only for bots that require user location
    """
    inline_message_id: Optional[str] = None
    """
    *Optional*. Identifier of the sent inline message. 
    Available only if there is an `inline keyboard 
    <https://core.telegram.org/bots/api#inlinekeyboardmarkup>`_ attached to the message. 
    Will be also received in `callback queries <https://core.telegram.org/bots/api#callbackquery>`_ 
    and can be used to `edit <https://core.telegram.org/bots/api#updating-messages>`_ the message.
    """
