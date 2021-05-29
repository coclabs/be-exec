from typing import Callable
from ktypes import Typing
from models import CodeExecResult

from .controllers import send_pong, execute_code

GET = Typing.SupportedHTTPMethod.GET
POST = Typing.SupportedHTTPMethod.POST


class Router:
    routes = {
        '/': {
            GET: send_pong
        },
        '/api': {
            GET: lambda: None,
        },
        '/api/codes': {
            POST: execute_code,
            'args': {
                'response_model': CodeExecResult
            }
        }
    }

    def __new__(cls): pass

    @staticmethod
    def register_route(service: Typing.App.service, route: Typing.Route, callback: Callable,
                       method: Typing.SupportedHTTPMethod = Typing.SupportedHTTPMethod.GET.value,
                       *args, **kwargs):
        getattr(service, method.value)(route, *args, **kwargs)(callback)


