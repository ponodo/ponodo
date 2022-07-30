def import_class(cls: str):
    import importlib

    module_path = ".".join(cls.split(".")[:-1])
    klass = cls.split(".")[-1:][0]
    module = importlib.import_module(module_path)
    return getattr(module, klass)
