class Service:
    service_attr: int


class ServiceWithCallable:
    def __init__(self):
        self.foo = CallableDict({"bar": lambda: 10})
        self.method_with_args = lambda x, y: x + y
        self.method_with_kwargs = lambda **kwargs: kwargs


class CallableDict(dict):
    def __init__(self, data):
        super().__init__(data)
        self.process = lambda *args, **kwargs: {"args": args, "kwargs": kwargs}
