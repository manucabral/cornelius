"""
    Cornelius keyboard module.
    This module contains the Keyboard class.
"""

import win32api as api

from .exceptions import InvalidKey
from .constants import KeyboardEvent

class Keyboard:
    def __init__(self):
        pass

    def press(self, key: str) -> None:
        """
            Press a key
 
            Params:
                key (str): Key to press
 
            Returns:
                None
 
            Raises:
                None
        """
        if not key:
            return
        api.keybd_event(KeyboardEvent.KEY[key], 0, 0, 0)
        api.keybd_event(KeyboardEvent.KEY[key], 0, KeyboardEvent.KEYUP, 0) 

    def delete(self) -> None:
        """
            Delete a key
 
            Params:
                None
 
            Returns:
                None
 
            Raises:
                None
        """
        api.keybd_event(0x08, 0, 0, 0)
        api.keybd_event(0x08, 0, KeyboardEvent.KEYUP, 0)
    
    def type(self, text: str) -> None:
        """
            Type text
 
            Params:
                text (str): Text to type
 
            Returns:
                None
 
            Raises:
                InvalidKey (Exception): If the key is not valid
        """
        if not text:
            return
        for char in text:
            char = char.upper()
            if not char in KeyboardEvent.KEY:
                raise InvalidKey(char)
            api.keybd_event(KeyboardEvent.KEY[char], 0, 0, 0)
            api.keybd_event(KeyboardEvent.KEY[char], 0, KeyboardEvent.KEYUP, 0)
    
    def key_state(self, **kwargs) -> bool:
        """
            Get the state of a key
 
            Params:
                key (str): Key to check
                exclude (list): Keys to exclude when checking
 
            Returns:
                bool: True if the key is pressed, False otherwise
 
            Raises:
                None
        """
        key = kwargs.get('key', None)
        exclude = kwargs.get('exclude', None)
        if not key:
            return False
        keyid = KeyboardEvent.KEY[key.upper()]
        return api.GetAsyncKeyState(keyid) & 0x8000
