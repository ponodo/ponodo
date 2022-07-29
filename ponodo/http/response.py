import collections.abc
import json

from werkzeug.wrappers.response import Response as WerkzeugResponse


class Response:
    def __init__(self, app, werkzeug_start_response):
        self.app = app
        self.werkzeug_start_response = werkzeug_start_response

    def __call__(self, *args, **kwargs):
        content, content_type = self._get_content_metadata(args[0])
        response = WerkzeugResponse(content, content_type=content_type, **kwargs)
        return response(
            self.app.instances["request"].environ, self.werkzeug_start_response
        )

    @staticmethod
    def _get_content_metadata(content):
        if isinstance(content, str):
            return content, "text/plain; charset=utf-8"
        if isinstance(content, (dict, collections.abc.Sequence)):
            return json.dumps(content), "application/json; charset=utf-8"

        return content, "text/plain; charset=utf-8"
