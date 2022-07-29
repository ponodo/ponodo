import collections.abc
import json

from werkzeug.wrappers.response import Response as WerkzeugResponse


class Response:
    def __init__(self, app, werkzeug_start_response):
        self.app = app
        self.werkzeug_start_response = werkzeug_start_response

    def __call__(self, *args, **kwargs):
        content, content_type = self.format_content(args[0])
        response = WerkzeugResponse(content, content_type=content_type)
        return response(
            self.app.instances["request"].environ, self.werkzeug_start_response
        )

    def format_content(self, content):
        if isinstance(content, str):
            return content, "text/plain; charset=utf-8"
        if isinstance(content, (dict, collections.abc.Sequence)):
            return json.dumps(content), "application/json; charset=utf-8"

        return content, "text/plain; charset=utf-8"
