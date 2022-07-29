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
        if path in route_collection.routes[method]:
            route = route_collection.routes[method][path]
            executor = getattr(route.controller(app=self), route.action)
            # arg_spec = inspect.getfullargspec(executor)
            # args = arg_spec.args
            # annotations = arg_spec.annotations
            controller_result = executor()

            # response = Response()
            response = self.app.instances["response"]
            return response(controller_result)
            # self.response("200 OK", [("Content-Type", "text/plain")])
            # return [controller_result.encode("utf-8")]
