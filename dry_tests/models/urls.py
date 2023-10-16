"""
Urls models
"""
from dataclasses import dataclass


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
                if not isinstance(value, (str, tuple)):
                    error_text = (f'Wrong url parameter "{key}" value. '
                                  f'Expected "str" or "tuple", got {type(value)}')
                    raise ValueError(error_text)
                if isinstance(value, tuple):
                    for one_value in value:
                        pair = f'{key}={one_value}'
                        url_params_list.append(pair)
                else:
                    pair = f'{key}={value}'
                    url_params_list.append(pair)
            url_params_str = '&'.join(url_params_list)
            url = f'{url}?{url_params_str}'
        return url


def get_url(url: str | Url):
    """
    Get url from str or Url
    :param url: input urls
    :return: result url
    """
    return url.make_url() if isinstance(url, Url) else url
