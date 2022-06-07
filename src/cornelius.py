import sys

from .exceptions import SystemNotSupported, PythonVersionException

if sys.platform != 'win32':
    raise SystemNotSupported('Cornelius is only supported on Windows')

if sys.version_info[0] < 3:
    raise PythonVersionException('Python 3.x is required to run Cornelius')