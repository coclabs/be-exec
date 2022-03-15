from typing import Callable
from ktypes import Typing, Union
from models import CodeExecResult, ErrorMixin

from .controllers import send_pong, execute_code

GET = Typing.SupportedHTTPMethod.GET
POST = Typing.SupportedHTTPMethod.POST
PUT = Typing.SupportedHTTPMethod.PUT
PATCH = Typing.SupportedHTTPMethod.PATCH
DELETE = Typing.SupportedHTTPMethod.DELETE


class Router:
    routes = {
        '/': {
            'methods': {
                GET: {
                    'callback': send_pong,
                },
                POST: {
                    'callback': send_pong,
                },
                PUT: {
                    'callback': send_pong,
                },
                PATCH: {
                    'callback': send_pong,
                },
                DELETE: {
                    'callback': send_pong,
                },
            }
        },
        '/api': {
            'methods': {
                GET: {
                    'callback': lambda: None,
                }
            }
        },
        '/api/codes': {
            'methods': {
                POST: {
                    'callback': execute_code,
                    'args': {
                        'response_model': Union[CodeExecResult, ErrorMixin],
                    }
                },
            },
        }
    }

    def __new__(cls): pass

    @staticmethod
    def register_route(service: Typing.App.service, route: Typing.Route, callback: Callable,
                       method: Typing.SupportedHTTPMethod = Typing.SupportedHTTPMethod.GET.value,
                       *args, **kwargs):
        getattr(service, method.value)(route, *args, **kwargs)(callback)


