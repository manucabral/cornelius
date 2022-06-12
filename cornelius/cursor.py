from ctypes import windll, wintypes, byref, pointer, sizeof
from ctypes.wintypes import DWORD
from time import sleep

from .structs import MouseInput, Input, _INPUTunion
from .exceptions import InvalidButtonException

"""
    Cornelius cursor implementation for Windows.
    Based on the windows API and ctypes.
    Docstrings format is reStructuredText.
    Copyright (C) 2022 Manuel Cabral
    Licensed under the GNU General Public License v3.0
"""


class Cursor:

    __SendInput = windll.user32.SendInput
    __set = windll.user32.SetCursorPos
    __get = windll.user32.GetCursorPos
    __state = windll.user32.GetKeyState

    __dwFlags = {
        1: [0x2, 0x4],  # [Left down, Left up]
        2: [0x8, 0x10],  # [Right down, Right up]
    }

    LEFT_BUTTON = 0x0001
    RIGHT_BUTTON = 0x0002

    def __check_button(self, button) -> None:
        """
            Check if the button is valid.

            :param button: button to check
            :return: None
            :raises InvalidButtonException: if button is not int or not valid
        """
        if not isinstance(button, int):
            raise InvalidButtonException('button must be int')
        if not button in self.__dwFlags:
            raise InvalidButtonException(
                f'button must be one of {self.__dwFlags}')

    def is_pressed(self, button: int) -> bool:
        """
            Check if a button is pressed.

            :param button: button to check
            :return: True if pressed, False otherwise
            :raises InvalidButtonException: if button is not int or not valid
        """
        self.__check_button(button)
        return self.__state(self.__dwFlags[button][0]) & 0x8000

    def set(self, pos_x: int, pos_y: int) -> None:
        """
            Set the cursor position.

            :param pos_x: x position
            :param pos_y: y position
            :return: None
            :raises TypeError: if pos_x or pos_y is not int
        """
        if not isinstance(pos_x, int) or not isinstance(pos_y, int):
            raise TypeError("x and y must be int")
        self.__set(pos_x, pos_y)

    def get(self) -> (int, int):
        """
            Get the cursor position.

            :return: (x, y)
        """
        point = wintypes.POINT()
        if self.__get(byref(point)):
            return point.x, point.y, point
        return 0, 0

    def press(self, button: int) -> int:
        """
            Press a button.

            :param button: button to press
            :return: number of events sent
        """
        x, y, _ = self.get()
        extra_flags = pointer(DWORD(0))
        union = _INPUTunion()
        union.mi = MouseInput(
            x, y, button, self.__dwFlags[button][0], 0, extra_flags)
        input_ = Input(0, union)
        events = self.__SendInput(1, pointer(input_), sizeof(input_))
        return events

    def release(self, button: int) -> int:
        """
            Release a button.

            :param button: button to release
            :return: number of events sent
        """
        self.__check_button(button)
        x, y, _ = self.get()
        extra_flags = pointer(DWORD(0))
        union = _INPUTunion()
        union.mi = MouseInput(
            x, y, button, self.__dwFlags[button][1], 0, extra_flags)
        input_ = Input(0, union)
        events = self.__SendInput(1, pointer(input_), sizeof(input_))
        return events

    def left_click(self, delay: float = 0.1) -> None:
        """
            Send a left click.

            :param delay: delay between clicks
            :return: Nones
        """
        self.press(self.LEFT_BUTTON)
        sleep(delay)
        self.release(self.LEFT_BUTTON)

    def right_click(self, delay: float = 0.1) -> None:
        """
            Sends a right click.

            :param delay: delay between clicks
            :return: None
        """
        self.press(self.RIGHT_BUTTON)
        sleep(delay)
        self.release(self.RIGHT_BUTTON)
