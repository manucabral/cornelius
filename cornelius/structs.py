from ctypes import pointer, sizeof, Union, Structure
from ctypes.wintypes import WORD, DWORD, LONG, ULONG, PULONG, LPDWORD

"""
    Cornelius C windows structures implementation.
    Based on the windows API and ctypes.
    Copyright (C) 2022 Manuel Cabral
    Licensed under the GNU General Public License v3.0
"""


class KeyboardInput(Structure):
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-keybdinput
    _fields_ = (
        ('wVk', WORD),
        ('wScan', WORD),
        ('dwFlags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', PULONG)
    )


class MouseInput(Structure):
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput
    _fields_ = (
        ('dx', LONG),
        ('dy', LONG),
        ('mouseData', DWORD),
        ('dwFlags', DWORD),
        ('time', DWORD),
        ('dwExtraInfo', PULONG)
    )


class HardwareInput(Structure):
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-hardwareinput
    _fields_ = (
        ('uMsg', DWORD),
        ('wParamL', WORD),
        ('wParamH', WORD)
    )


class _INPUTunion(Union):
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input
    _fields_ = (
        ('mi', MouseInput),
        ('ki', KeyboardInput),
        ('hi', HardwareInput)
    )


class Input(Structure):
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input
    _fields_ = (
        ('type', DWORD),
        ('union', _INPUTunion)
    )
