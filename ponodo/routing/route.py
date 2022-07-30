from werkzeug.routing import Rule


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
        return cls._generate_rule("GET", path, **kwargs)

    @classmethod
    def _generate_rule(cls, methods, path, **kwargs):
        rule_kwargs = {}

        # Endpoint
        if "to" in kwargs:
            rule_kwargs["endpoint"] = kwargs["to"]
        elif "controller" in kwargs:
            module = kwargs["controller"].__module__
            class_name = kwargs["controller"].__name__
            endpoint = f"{module}.{class_name}"
            if "action" in kwargs:
                action = kwargs["action"]
                rule_kwargs["endpoint"] = f"{endpoint}@{action}"
            else:
                rule_kwargs["endpoint"] = endpoint

        # methods
        if isinstance(methods, str):
            methods = [methods]
        rule_kwargs["methods"] = methods

        return Rule(path, **rule_kwargs)

    @classmethod
    def post(cls, path, **kwargs):
        return Rule(path, methods="POST", endpoint=kwargs["to"])

    @classmethod
    def put(cls, path, **kwargs):
        return Rule(path, methods="PUT", endpoint=kwargs["to"])

    @classmethod
    def patch(cls, path, **kwargs):
        return Rule(path, methods="PATCH", endpoint=kwargs["to"])

    @classmethod
    def delete(cls, path, **kwargs):
        return Rule(path, methods="DELETE", endpoint=kwargs["to"])

    # @classmethod
    # def _get_routes(cls):
    #     app = Facade.app
    #     return app.make("routes")


def get(*args, **kwargs):
    return Route.get(*args, **kwargs)


def post(*args, **kwargs):
    return Route.post(*args, **kwargs)


def put(*args, **kwargs):
    return Route.put(*args, **kwargs)


def patch(*args, **kwargs):
    return Route.patch(*args, **kwargs)


def delete(*args, **kwargs):
    return Route.delete(*args, **kwargs)
