from ponodo.core.facade import Facade


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
