import inspect

from werkzeug.routing import Map

from ponodo.helpers import import_class
from ponodo.http import Request


class ControllerDispatcher:
    def __init__(self, app):
        self.app = app

    def run(self):
        request = self.app.instances["request"]

        # todo: configurable routing registration
        from app.routes.web import routes

        endpoint, args = Map(routes).bind_to_environ(request.environ).match()
        controller, action = endpoint.split("@")
        controller = import_class(controller)
        executor = getattr(controller(app=self), action)

        arg_spec = inspect.getfullargspec(executor)
        annotations = arg_spec.annotations
        kwargs = {}

        for annotation in annotations:

            if annotations[annotation] == Request:
                kwargs[annotation] = request

        # if 'request' in args:
        #     kwargs['request'] = request
        controller_result = executor(**kwargs)

        response = self.app.instances["response"]
        return response(controller_result)
