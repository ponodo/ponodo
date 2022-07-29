class Route:
    def __init__(self, path, to=None, controller=None, action=None, alias=None):
        self.path = path
        self.to = to
        self.controller = controller
        self.action = action
        self.alias = alias
