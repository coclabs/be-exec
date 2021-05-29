from ktypes import Typing


def init_routes(app: Typing.App, /):
    from api.v1 import routes

    router = routes.Router
    for route, route_attr in router.routes.items():
        for method, method_attr in route_attr.get('methods'):
            router.register_route(app.service, route, method=method, **method_attr)

    return app
