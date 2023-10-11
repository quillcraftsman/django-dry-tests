"""
Main models to DRY tests
"""
from dataclasses import dataclass
from typing import Literal
from django.db.models import Model

GET = 'get'
POST = 'post'


@dataclass(frozen=True)
class Url:
    """
    Url for Request with args and params
    """
    url: str
    args: list = None
    params: dict = None

    def make_url(self):
        """
        Make url with params and kwargs
        :param request:
        :return:
        """
        url = self.url
        # url_args
        url_args_list = self.args
        if url_args_list:
            url_args = '/'.join(url_args_list)
            url = f'{url}{url_args}/'
        # url_params
        url_params_dict = self.params
        if url_params_dict:
            url_params_list = []
            for key, value in url_params_dict.items():
                pair = f'{key}={value}'
                url_params_list.append(pair)
            url_params_str = '&'.join(url_params_list)
            url = f'{url}?{url_params_str}'
        return url


@dataclass(frozen=True)
class Request:
    """
    Main Request Model
    """
    url: str | Url
    # url_args: list = None
    # url_params: dict = None
    method: Literal[GET, POST] = GET
    data: dict = None

    # def make_url(self):
    #     """
    #     Make url with params and kwargs
    #     :param request:
    #     :return:
    #     """
    #     url = self.url
    #     # url_args
    #     url_args_list = self.url_args
    #     if url_args_list:
    #         url_args = '/'.join(url_args_list)
    #         url = f'{url}{url_args}/'
    #     # url_params
    #     url_params_dict = self.url_params
    #     if url_params_dict:
    #         url_params_list = []
    #         for key, value in url_params_dict.items():
    #             pair = f'{key}={value}'
    #             url_params_list.append(pair)
    #         url_params_str = '&'.join(url_params_list)
    #         url = f'{url}?{url_params_str}'
    #     return url

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


@dataclass(frozen=True)
class ContentValue:
    """
    Content Value Dataclass
    """
    value: str
    count: int = None


@dataclass(frozen=True)
class ExpectedResponse:
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
