"""
Main models to DRY tests
"""
from dataclasses import dataclass
from typing import Literal
from django.db.models import Model

GET = 'get'
POST = 'post'


@dataclass(frozen=True)
class Request:
    """
    Main Request Model
    """
    url: str
    method: Literal[GET, POST] = GET
    data: dict = None


@dataclass(frozen=True)
class Response:
    """
    Main Excepted Response Model
    """
    status_code: int = 200
    redirect_url: str = None
    in_context: str = None
    context_values: dict = None
    content_value: str = None
    created: Model = None
    # db_data: callable = None
