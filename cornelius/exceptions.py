class CorneliusException(Exception):
    def __init__(self, message: str = None):
        message = 'An fatal error has occurred' if message is None else message
        super().__init__(message)


class InvalidButtonException(CorneliusException):
    def __init__(self, message: str = None):
        message = 'The button is not valid' if message is None else message
        super().__init__(message)


class InvalidKeyException(CorneliusException):
    def __init__(self, message: str = None):
        message = 'The key is not valid' if message is None else message
        super().__init__(message)
