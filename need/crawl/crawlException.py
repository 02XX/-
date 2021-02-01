class ServerConnectFailed(Exception):
    def __init__(self, s) -> None:
        self.message = s
class ParameterError(Exception):
    def __init__(self, s) -> None:
        self.message = s
class NoSuchQuestion(Exception):
    def __init__(self, s) -> None:
        self.message = s




