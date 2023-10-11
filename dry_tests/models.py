from dataclasses import dataclass
from typing import Literal

GET = 'get'
POST = 'post'


@dataclass(frozen=True)
class Request:
    url: str
    method: Literal[GET, POST] = GET


@dataclass(frozen=True)
class Response:
    status_code: int = 200
    redirect_url: str = None
    in_context: str = None
    context_values: dict = None
    content_value: str = None
