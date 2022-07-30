from werkzeug.routing import Rule


class Route:
    # def __init__(
    #         self, path, method="GET", to=None, controller=None, action=None, alias=None
    # ):
    #     self.path = path
    #     self.to = to
    #     self.controller = controller
    #     self.action = action
    #     self.alias = alias
    #     self.method = method

    def _new_rule(self, path, **kwargs):
        rule_kwargs = {
            "endpoint": self._make_endpoint(**kwargs),
            "methods": self._make_methods(**kwargs),
        }

        return Rule(path, **rule_kwargs)

    @staticmethod
    def _make_methods(**kwargs):
        methods = kwargs["methods"]
        if isinstance(methods, str):
            return [methods]
        return methods

    @staticmethod
    def _make_endpoint(**kwargs):
        controllers_location = "app.http.controllers"

        if "to" in kwargs:
            # Transform `foo@bar` into full path of the controller location,
            # and it's action. For example the sample above will transform into
            # `app.http.controllers.foo_controller.FooController@bar`

            to = kwargs["to"]

            # if "." in to:
            #     # It will transform `foo.bar@baz` into
            #     # `app.http.controllers.foo.bar_controller.BarController@baz`
            #
            #     modules = to.split(".")
            #
            #     return f"{controllers_location}.{modules[0]}"
            # debug()
            # from IPython import embed
            # embed()

            controller_candidate, action = to.split("@")
            controller_module_name = f"{controller_candidate}_controller"
            class_name = controller_module_name.title().replace("_", "")

            return (
                f"{controllers_location}.{controller_module_name}.{class_name}@{action}"
            )

        if "controller" in kwargs:
            module = kwargs["controller"].__module__
            class_name = kwargs["controller"].__name__
            endpoint = f"{module}.{class_name}"

            if "action" in kwargs:
                action = kwargs["action"]
                return f"{endpoint}@{action}"

            return endpoint

    def get(self, path, **kwargs):
        return self._new_rule(path, methods="GET", **kwargs)

    def post(self, path, **kwargs):
        return self._new_rule(path, methods="POST", **kwargs)

    def put(self, path, **kwargs):
        return self._new_rule(path, methods="PUT", **kwargs)

    def patch(self, path, **kwargs):
        return self._new_rule(path, methods="PATCH", **kwargs)

    def delete(self, path, **kwargs):
        return self._new_rule(path, methods="DELETE", **kwargs)


def get(*args, **kwargs):
    return Route().get(*args, **kwargs)


def post(*args, **kwargs):
    return Route().post(*args, **kwargs)


def put(*args, **kwargs):
    return Route().put(*args, **kwargs)


def patch(*args, **kwargs):
    return Route().patch(*args, **kwargs)


def delete(*args, **kwargs):
    return Route().delete(*args, **kwargs)
