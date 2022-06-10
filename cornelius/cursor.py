from ctypes import windll, wintypes, byref
from .exceptions import InvalidButtonException

"""
    Cornelius cursor implementation for Windows.
    Based on the windows API and ctypes.
    Docstrings format is reStructuredText.
    Copyright (C) 2022 Manuel Cabral
    Licensed under the GNU General Public License v3.0
"""


class Cursor:
    __set = windll.user32.SetCursorPos
    __get = windll.user32.GetCursorPos
    __event = windll.user32.mouse_event
    __state = windll.user32.GetKeyState

    __dwFlags = {
        1: [0x2, 0x4],  # [Left down, Left up]
        2: [0x8, 0x10],  # [Right down, Right up]
    }

    RIGHT_BUTTON = 0x1
    LEFT_BUTTON = 0x2

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

    def press(self, button: int, **kwargs) -> None:
        """
            Press a button.

            :param button: button to press
            :param kwargs:
                - repeat: number of times to press
            :return: None
            :raises InvalidButtonException: if button is not int or not valid
        """
        self.__check_button(button)
        repeat = kwargs.get("repeat", 1)
        for _ in range(repeat):
            self.__event(self.__dwFlags[button][0], 0, 0, 0, 0)
            self.__event(self.__dwFlags[button][1], 0, 0, 0, 0)

    def is_pressed(self, button: int) -> bool:
        """
            Check if a button is pressed.

            :param button: button to check
            :return: True if pressed, False otherwise
            :raises InvalidButtonException: if button is not int or not valid
        """
        self.__check_button(button)
        return self.__state(button) & 0x80 == 0x80
