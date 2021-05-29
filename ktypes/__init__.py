from typing import *
from enum import Enum
from fastapi import FastAPI


class Typing:
    Route: Final = Dict[str, Dict[str, Callable]]

    class App:
        service = FastAPI

    class SupportedHTTPMethod(Enum):
        GET = 'get'
        POST = 'post'
        PUT = 'put'
        PATCH = 'patch'
        DELETE = 'delete'
