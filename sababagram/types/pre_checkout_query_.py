from dataclasses import dataclass
from typing import Optional

from .base import BaseTelegramType
from .order_info_ import OrderInfo
from .user_ import User


@dataclass
class PreCheckoutQuery(BaseTelegramType):
    """
    This object contains information about an incoming pre-checkout query.

    Source: https://core.telegram.org/bots/api#precheckoutquery
    """

    id: str
    """
    Unique query identifier
    """
    from_user: User
    """
    User who sent the query
    """
    currency: str
    """
    Three-letter ISO 4217 `currency <https://core.telegram.org/bots/payments#supported-currencies>`_ 
    code
    """
    total_amount: int
    """
    Total price in the *smallest units* of the currency (integer, **not** float/double). For example, 
    for a price of :code:`US$ 1.45` pass :code:`amount = 145`. 
    See the *exp* parameter in `currencies.json 
    <https://core.telegram.org/bots/payments/currencies.json>`_, 
    it shows the number of digits past the decimal point for each currency (2 for the majority of 
    currencies).
    """
    invoice_payload: str
    """
    Bot specified invoice payload
    """
    shipping_option_id: Optional[str] = None
    """
    *Optional*. Identifier of the shipping option chosen by the user
    """
    order_info: Optional[OrderInfo] = None
    """
    *Optional*. Order information provided by the user
    """
