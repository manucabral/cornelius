from ctypes import windll, pointer, sizeof
from ctypes.wintypes import DWORD, ULONG
from time import sleep

from .structs import Input, KeyboardInput, _INPUTunion
from .exceptions import InvalidKeyException

"""
    Cornelius keyboard implementation for Windows.
    Based on the windows API and ctypes.
    Docstrings format is reStructuredText.
    Copyright (C) 2022 Manuel Cabral
    Licensed under the GNU General Public License v3.0
"""


class Keyboard:
    __SendInput = windll.user32.SendInput
    __state = windll.user32.GetKeyState

    """
        Key map for char keys, some keys are not implemented yet.
        http://www.flint.jp/misc/?q=dik&lang=en
    """

    KEY_MAP = {
        'a': {'vk': 0x41, 'scan': 0x1E},
        'b': {'vk': 0x42, 'scan': 0x30},
        'c': {'vk': 0x43, 'scan': 0x2E},
        'd': {'vk': 0x44, 'scan': 0x20},
        'e': {'vk': 0x45, 'scan': 0x12},
        'f': {'vk': 0x46, 'scan': 0x21},
        'g': {'vk': 0x47, 'scan': 0x22},
        'h': {'vk': 0x48, 'scan': 0x23},
        'i': {'vk': 0x49, 'scan': 0x17},
        'j': {'vk': 0x4A, 'scan': 0x24},
        'k': {'vk': 0x4B, 'scan': 0x25},
        'l': {'vk': 0x4C, 'scan': 0x26},
        'm': {'vk': 0x4D, 'scan': 0x32},
        'n': {'vk': 0x4E, 'scan': 0x31},
        'o': {'vk': 0x4F, 'scan': 0x18},
        'p': {'vk': 0x50, 'scan': 0x19},
        'q': {'vk': 0x51, 'scan': 0x10},
        'r': {'vk': 0x52, 'scan': 0x13},
        's': {'vk': 0x53, 'scan': 0x1F},
        't': {'vk': 0x54, 'scan': 0x14},
        'u': {'vk': 0x55, 'scan': 0x16},
        'v': {'vk': 0x56, 'scan': 0x2F},
        'w': {'vk': 0x57, 'scan': 0x11},
        'x': {'vk': 0x58, 'scan': 0x2D},
        'y': {'vk': 0x59, 'scan': 0x15},
        'z': {'vk': 0x5A, 'scan': 0x2C},
        '0': {'vk': 0x30, 'scan': 0x0B},
        '1': {'vk': 0x31, 'scan': 0x02},
        '2': {'vk': 0x32, 'scan': 0x03},
        '3': {'vk': 0x33, 'scan': 0x04},
        '4': {'vk': 0x34, 'scan': 0x05},
        '5': {'vk': 0x35, 'scan': 0x06},
        '6': {'vk': 0x36, 'scan': 0x07},
        '7': {'vk': 0x37, 'scan': 0x08},
        '8': {'vk': 0x38, 'scan': 0x09},
        '9': {'vk': 0x39, 'scan': 0x0A},
        'ctrl': {'vk': 0x11, 'scan': 0x1D},
        'shift': {'vk': 0x10, 'scan': 0x2A},
        'alt': {'vk': 0x12, 'scan': 0x38},
        'caps': {'vk': 0x14, 'scan': 0x3A},
        'esc': {'vk': 0x1B, 'scan': 0x01},
        'tab': {'vk': 0x09, 'scan': 0x0F},
        'f1': {'vk': 0x70, 'scan': 0x3B},
        'f2': {'vk': 0x71, 'scan': 0x3C},
        'f3': {'vk': 0x72, 'scan': 0x3D},
        'f4': {'vk': 0x73, 'scan': 0x3E},
        'f5': {'vk': 0x74, 'scan': 0x3F},
        'f6': {'vk': 0x75, 'scan': 0x40},
        'f7': {'vk': 0x76, 'scan': 0x41},
        'f8': {'vk': 0x77, 'scan': 0x42},
        'f9': {'vk': 0x78, 'scan': 0x43},
        'f10': {'vk': 0x79, 'scan': 0x44},
        'f11': {'vk': 0x7A, 'scan': 0x57},
        'f12': {'vk': 0x7B, 'scan': 0x58}
    }

    def __convert_key(self, key: str, outformat: str) -> int:
        """
            Convert a char key to a virtual or scan code.

            :param key: The key to convert.
            :param outformat: The output format.
            :return: The converted key.
            :raises InvalidKeyException: if the key is not a valid key.
        """
        if key in self.KEY_MAP:
            return self.KEY_MAP[key][outformat]
        raise InvalidKeyException(f'"{key}" is not a valid key.')

    def press(self, key) -> int:
        """
            Press a keystroke.

            :param key: The key to press.
            :param format: The format of the keystroke.
            :return: The number of events sent.
            :raises InvalidKeyException: if the key is not a valid key.
        """
        key = self.__convert_key(key, 'scan')
        extra_flags = pointer(DWORD(0))
        union = _INPUTunion()
        union.ki = KeyboardInput(0, key, 0x0008, 0, extra_flags)
        input_ = Input(ULONG(1), union)
        events = self.__SendInput(1, pointer(input_), sizeof(input_))
        return events

    def release(self, key) -> int:
        """
            Release a keystroke.

            :param key: The key to release.
            :return: The number of events sent.
            :raises InvalidKeyException: if the key is not a valid key.
        """
        key = self.__convert_key(key, 'scan')
        extra_flags = pointer(DWORD(0))
        union = _INPUTunion()
        union.ki = KeyboardInput(0, key, 0x0008 | 0x0002, 0, extra_flags)
        input_ = Input(ULONG(1), union)
        events = self.__SendInput(1, pointer(input_), sizeof(input_))
        return events

    def send(self, key, delay: float = 0.0) -> int:
        """
            Send a keystroke.

            :param key: The key to send.
            :param delay: The delay in seconds.
            :return: The number of events sent.
            :raises InvalidKeyException: if the key is not a valid key.
        """
        key = self.__convert_key(key, 'scan')
        events = 0 + self.press(key)
        if delay > 0.0:
            sleep(delay)
        events += self.release(key)
        return events

    def is_pressed(self, key) -> bool:
        """
            Check if a key is pressed.

            :param key: The key to check.
            :return: True if the key is pressed, False otherwise.
            :raises InvalidKeyException: if the key is not a valid key.
        """
        key = self.__convert_key(key, 'vk')
        return self.__state(key) & 0x80 == 0x80
