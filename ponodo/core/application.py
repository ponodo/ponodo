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


class Application(Container):
    def __init__(self):
        super(Application, self).__init__()

        self.instances["routes"] = RouteCollection(app=self)

    def set_werkzeug_request(self, request):
        self.instances["request"] = Request(app=self, werkzeug_request=request)
        return self

    def set_werkzeug_response(self, response):
        self.instances["response"] = Response(
            app=self, werkzeug_start_response=response
        )
        return self

    def handle(self):

        return ControllerDispatcher(app=self).run()
