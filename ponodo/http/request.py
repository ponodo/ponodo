class Request:
    def __init__(self, app, werkzeug_request):
        self.app = app
        self.werkzeug_request = werkzeug_request

    def __getattr__(self, item):
        if hasattr(self.werkzeug_request, item):
            return getattr(self.werkzeug_request, item)
