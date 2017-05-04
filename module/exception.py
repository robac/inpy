class InpyError(Exception):
    pass

class ConfigurationError(InpyError):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg