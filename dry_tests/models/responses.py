"""
Response models
"""
from dataclasses import dataclass
from django.db.models import Model
from .content import ContentValue


@dataclass(frozen=True)
class TrueResponse:
    """
    Main Excepted Response Model
    """
    status_code: int = 200
    redirect_url: str = None
    in_context: str = None
    context_values: dict = None
    content_values: list = None
    created: Model = None
    # db_data: callable = None

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
