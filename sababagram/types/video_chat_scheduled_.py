from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class VideoChatScheduled(BaseTelegramType):
    """
    This object represents a service message about a video chat scheduled in the chat.

    Source: https://core.telegram.org/bots/api#videochatscheduled
    """

    start_date: int
    """
    Point in time (Unix timestamp) when the video chat is supposed to be started by a chat 
    administrator
    """
