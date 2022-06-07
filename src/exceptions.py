class CorneliusException(Exception):
    def __init__(self, message: str = None):
        message = 'An fatal error has occurred' if message is None else message
        super().__init__(message)

class PythonVersionException(CorneliusException):
    def __init__(self, message: str = None):
        message = 'Python version is not supported' if message is None else message
        super().__init__(message)

class SystemNotSupported(CorneliusException):
    def __init__(self, message: str = None):
        message = 'The system is not supported' if message is None else message
        super().__init__(message)

class NoSuchFile(CorneliusException):
    def __init__(self, filename: str):
        super().__init__(f"File '{filename}' not found")

class InvalidMouseButton(CorneliusException):
    def __init__(self, button: int):
        super().__init__(f"Invalid mouse button: {button}")

class InvalidKey(CorneliusException):
    def __init__(self, key: str):
        super().__init__(f"Invalid key: {key}")