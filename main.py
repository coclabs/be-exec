import api
import sentry_sdk

from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

sentry_sdk.init(
    dsn="https://957e126643af407c94a99b32c263025d@o708708.ingest.sentry.io/5778759",
    traces_sample_rate=1.0
)


@api.init_routes
class App:
    """An application class for simple FastAPI application"""

    service = FastAPI()
    service.add_middleware(SentryAsgiMiddleware)

    def __new__(cls): pass

