class InpyError(Exception):
    pass

class ConfigurationError(InpyError):
    def __init__(self, message, detail):
        self.message = message
        self.detail = detail