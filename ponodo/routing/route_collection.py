from .route import Route


class RouteCollection:
    def __init__(self, app):
        self.app = app
        self.routes = {
            "GET": {},
            "HEAD": {},
            "POST": {},
            "PUT": {},
            "PATCH": {},
            "DELETE": {},
        }

    def add_route(self, route: Route):
        self.routes[route.method][route.path] = route
