from dataclasses import dataclass
from typing import Optional, Union

from .base import BaseTelegramType
from .input_file_ import InputFile
from .mask_position_ import MaskPosition


@dataclass
class InputSticker(BaseTelegramType):
    """
    This object describes a sticker to be added to a sticker set.

    Source: https://core.telegram.org/bots/api#inputsticker
    """

    sticker: Union[InputFile, str]
    """
    The added sticker. 
    Pass a *file_id* as a String to send a file that already exists on the Telegram servers, 
    pass an HTTP URL as a String for Telegram to get a file from the Internet, 
    upload a new one using multipart/form-data, 
    or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under 
    <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. 
    `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_
    """
    format: str
    """
    Format of the added sticker, must be one of “static” for a **.WEBP** or **.PNG** image, 
    “animated” for a **.TGS** animation, “video” for a **WEBM** video
    """
    emoji_list: list[str]
    """
    List of 1-20 emoji associated with the sticker
    """
    mask_position: Optional[MaskPosition] = None
    """
    *Optional*. Position where the mask should be placed on faces. For “mask” stickers only.
    """
    keywords: Optional[list[str]] = None
    """
    *Optional*. 
    List of 0-20 search keywords for the sticker with total length of up to 64 characters. 
    For “regular” and “custom_emoji” stickers only.
    """
