from ktypes import Typing


def init_routes(app: Typing.App, /):
    from api.v1 import routes

    router = routes.Router
    for k, v in router.routes.items():
        keys = iter(v.keys())
        values = iter(v.values())
        route = k
        method = next(keys)
        callback = next(values)
        args = {}
        try:
            args = next(values)
        except StopIteration:
            pass
        router.register_route(app.service, route, method=method, callback=callback, **args)

    return app
