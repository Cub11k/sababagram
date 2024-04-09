from dataclasses import dataclass, field
from typing import Optional, Union

from .input_file_ import InputFile
from .input_media_ import InputMedia
from .message_entity_ import MessageEntity


@dataclass
class InputMediaDocument(InputMedia):
    """
    Represents a general file to be sent.

    Source: https://core.telegram.org/bots/api#inputmediadocument
    """

    type: str = field(default="document", init=False)
    """
    Type of the result, must be *document*
    """
    media: str
    """
    File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), 
    pass an HTTP URL for Telegram to get a file from the Internet, 
    or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under 
    <file_attach_name> name. 
    `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_
    """
    thumbnail: Optional[Union[InputFile, str]] = None
    """
    *Optional*. Thumbnail of the file sent; 
    can be ignored if thumbnail generation for the file is supported server-side. 
    The thumbnail should be in JPEG format and less than 200 kB in size. 
    A thumbnail's width and height should not exceed 320. 
    Ignored if the file is not uploaded using multipart/form-data. 
    Thumbnails can't be reused and can be only uploaded as a new file, 
    so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using 
    multipart/form-data under <file_attach_name>. 
    `More information on Sending Files » <https://core.telegram.org/bots/api#sending-files>`_
    """
    caption: Optional[str] = None
    """
    *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing
    """
    parse_mode: Optional[str] = None
    """
    *Optional*. Mode for parsing entities in the document caption. 
    See `formatting options <https://core.telegram.org/bots/api#formatting-options>`_ for more details.
    """
    caption_entities: Optional[list[MessageEntity]] = None
    """
    *Optional*. List of special entities that appear in the caption, 
    which can be specified instead of *parse_mode*
    """
    disable_content_type_detection: Optional[bool] = None
    """
    *Optional*. 
    Disables automatic server-side content type detection for files uploaded using 
    multipart/form-data. Always *True*, if the document is sent as part of an album.
    """
