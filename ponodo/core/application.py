from ponodo.core.facade import Facade
from ponodo.http.request import Request
from ponodo.http.response import Response
from ponodo.routing.controller_dispatcher import ControllerDispatcher
from ponodo.routing.route_collection import RouteCollection


class Container:
    """ """

    def __init__(self):
        # Binding abstract to concrete
        self.bindings = {}

        # Instance of class or plain object
        self.instances = {}

    def get(self, abstract):
        if abstract in self.instances:
            return self.instances[abstract]


class Application(Container):
    def __init__(self):
        super(Application, self).__init__()

    def set_werkzeug_request(self, request):
        self.instances["request"] = Request(app=self, werkzeug_request=request)
        return self

    def set_werkzeug_response(self, response):
        self.instances["response"] = Response(
            app=self, werkzeug_start_response=response
        )
        return self

    def handle(self):
        # Set application as class property of Facade class
        self.instances["routes"] = RouteCollection(app=self)
        Facade.app = self
        from app.routes.web import routes

        routes()

        return ControllerDispatcher(app=self).run()
