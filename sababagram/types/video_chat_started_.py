from dataclasses import dataclass

from .base import BaseTelegramType


@dataclass
class VideoChatStarted(BaseTelegramType):
    """
    This object represents a service message about a video chat started in the chat.
    Currently holds no information.

    Source: https://core.telegram.org/bots/api#videochatstarted
    """
