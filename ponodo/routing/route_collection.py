from app.http.controllers.project_controller import ProjectController

from .route import Route


class RouteCollection:
    def __init__(self, app):
        self.app = app
        self.routes = {
            "GET": {
                "/": Route(path="/", to="dashboard@index"),
                "/projects": Route(
                    path="/projects", controller=ProjectController, action="index"
                ),
            },
            "POST": [],
            "PUT": [],
            "PATCH": [],
            "DELETE": [],
        }
