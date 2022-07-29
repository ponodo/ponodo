import inspect

from ponodo.core import Facade
from ponodo.http import Request


class ControllerDispatcher:
    def __init__(self, app):
        self.app = app

    def run(self):
        # Request
        request = self.app.instances["request"]
        method = request.method
        # scheme = request.scheme
        # server = request.server[0]
        # port = request.server[1]
        # query = request.query_string
        path = request.path
        # headers = request.headers

        # Route request to specific Controller
        route_collection = self.app.instances["routes"]
        response = self.app.instances["response"]

        if path in route_collection.routes[method]:
            route = route_collection.routes[method][path]
            executor = getattr(route.controller(app=self), route.action)
            arg_spec = inspect.getfullargspec(executor)
            # args = arg_spec.args
            annotations = arg_spec.annotations
            kwargs = {}

            for annotation in annotations:

                if annotations[annotation] == Request:
                    kwargs[annotation] = request

            # if 'request' in args:
            #     kwargs['request'] = request
            controller_result = executor(**kwargs)

            # response = Response()
            return response(controller_result)
            # self.response("200 OK", [("Content-Type", "text/plain")])
            # return [controller_result.encode("utf-8")]

        return response("404", status=404)


class Route:
    def __init__(
        self, path, method="GET", to=None, controller=None, action=None, alias=None
    ):
        self.path = path
        self.to = to
        self.controller = controller
        self.action = action
        self.alias = alias
        self.method = method

    @classmethod
    def get(cls, path, **kwargs):
        app = Facade.app
        routes = app.get("routes")
        routes.add_route(cls(path, method="GET", **kwargs))
        routes.add_route(cls(path, method="HEAD", **kwargs))

    @classmethod
    def post(cls, path, **kwargs):
        app = Facade.app
        routes = app.get("routes")
        routes.add_route(cls(path, method="POST", **kwargs))


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
