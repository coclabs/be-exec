import api

from fastapi import FastAPI


@api.init_routes
class App:
    """An application class for simple FastAPI application"""

    service = FastAPI()

    def __new__(cls): pass

