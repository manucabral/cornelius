from ctypes import windll
from .exceptions import InvalidKeyException

"""
    Cornelius keyboard implementation for Windows.
    Based on the windows API and ctypes.
    Docstrings format is reStructuredText.
    Copyright (C) 2022 Manuel Cabral
    Licensed under the GNU General Public License v3.0
"""


class Keyboard:
    __event = windll.user32.keybd_event
    __state = windll.user32.GetKeyState

    __dwFlags = {
        1: 0,       # Event key down
        2: 0x0002,  # Event key up
    }

    def __check_key(self, key) -> None:
        """
            Check if the key is valid.

            :param key: key to check
            :return: None
            :raises InvalidKeyException: if key is not str or int
        """
        if not isinstance(key, (str, int)):
            raise InvalidKeyException('key must be str or int')

    def __to_int(self, key: str) -> int:
        """
            Convert a key to its integer representation.

            :param key: key to convert
            :return: integer representation of the key
            :raises TypeError: if key is not str
        """
        if not isinstance(key, str):
            raise TypeError("key must be str")
        return ord(key.upper())

    def is_pressed(self, key) -> bool:
        """
            Check if a key is pressed.

            :param key: key to check
            :return: True if pressed, False otherwise
            :raises TypeError: if key is not str or int
        """
        self.__check_key(key)
        if isinstance(key, str):
            key = self.__to_int(key)
        return self.__state(key) & 0x80 == 0x80

    def press(self, key) -> None:
        """
            Press a key.

            :param key: key to press
            :return: None
            :raises InvalidKeyException: if key is not str or int
        """
        self.__check_key(key)
        if isinstance(key, str):
            key = self.__to_int(key)
        self.__event(key, 0, self.__dwFlags[1], 0)

    def release(self, key) -> None:
        """
            Release a key.

            :param key: key to release
            :return: None
            :raises InvalidKeyException: if key is not str or int
        """
        self.__check_key(key)
        if isinstance(key, str):
            key = self.__to_int(key)
        self.__event(key, 0, self.__dwFlags[2], 0)
