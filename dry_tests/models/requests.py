"""
Requests Models
"""
from dataclasses import dataclass
from typing import Literal
from .urls import Url

GET = 'get'
POST = 'post'


@dataclass(frozen=True)
class Request:
    """
    Main Request Model
    """
    # true_response: TrueResponse
    url: str | Url
    method: Literal[GET, POST] = GET
    data: dict = None

    def get_url_response(self, client):
        """
        get response with test client
        :param client: Request client
        :return: client response
        """
        requests = {
            GET: client.get,
            POST: client.post
        }

        url = self.url.make_url() if isinstance(self.url, Url) else self.url
        url_response = requests[self.method](url, data=self.data)

        return url_response
