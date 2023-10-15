"""
Response models
"""
from dataclasses import dataclass
from django.db.models import Model
from .content import ContentValue
from .context import Context
from .urls import Url, get_url


@dataclass(frozen=True)
class TrueResponse:
    """
    Main Excepted Response Model
    """
    status_code: int = None
    redirect_url: str | Url = None
    content_values: list = None
    context: Context = None
    created: Model = None

    def get_content_values(self):
        """
        Convert content values to ContentValue
        :return:
        """
        return [
            content_value
            if isinstance(content_value, ContentValue)
            else ContentValue(value=content_value)
            for content_value in self.content_values
        ]

    def get_redirect_url(self):
        """
        Get result url from self url
        :return: str url
        """
        return get_url(self.redirect_url)
