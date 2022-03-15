from ktypes import Typing


def init_routes(app: Typing.App, /):
    from api.v1 import routes

    router = routes.Router
    for route, route_attr in router.routes.items():
        for method, method_attr in route_attr.get('methods').items():
            callback, args = method_attr.get('callback'), method_attr.get('args', {})
            router.register_route(app.service, route, method=method, callback=callback, **args)

    return app
