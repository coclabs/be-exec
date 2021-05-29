import api
import sentry_sdk

from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

# sentry_sdk.init(
#     dsn='https://12369f77d5474acdb6908dbeb8daddaf@o525207.ingest.sentry.io/5778800',
#     traces_sample_rate=1.0,
#     environment='develop'
# )


@api.init_routes
class App:
    """An application class for simple FastAPI application"""

    service = FastAPI()
    # service.add_middleware(SentryAsgiMiddleware)

    def __new__(cls): pass

