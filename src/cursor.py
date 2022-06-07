"""
    Cornelius cursor module.
    This module contains the Cursor class.
"""

import win32api as api

from .constants import MouseEvent
from .exceptions import InvalidMouseButton

class Cursor:

    def __init__(self, **kwargs):
        if not kwargs:
            self.__refresh()
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)

    def __refresh(self) -> None:
        """
            Refresh the cursor position
            
            Params:
                None

            Returns:
                None

            Raises:
                None
        """
        self.x, self.y = api.GetCursorPos()
    
    def click(self, button: int = 1) -> None:
        """
            Click the mouse

            Params:
                button (int): Mouse button to click
                    1: Left
                    2: Right
                    3: Middle

            Returns:
                None

            Raises:
                InvalidMouseButton (Exception): If the button is not valid
        """
        if not button:
            return
        if not button in MouseEvent.CLICK:
            raise InvalidMouseButton(button)
        api.mouse_event(MouseEvent.CLICK[button][0], 0, 0)
        api.mouse_event(MouseEvent.CLICK[button][1], 0, 0)

    def move(self, **kwargs) -> None:
        """
            Move the cursor to the specified position

            Params:
                x (int): X coordinate
                y (int): Y coordinate

            Returns:
                None

            Raises:
                None
        """
        if not kwargs:
            return
        position = kwargs.get('x', self.x), kwargs.get('y', self.y)
        api.SetCursorPos(position)
