---
title: 'class: Cursor'
---

# Cursor
In this section will you see _Cursor_ class information.

Cursor class contains methods for controlling the mouse.

## `get()`
Gets the current cursor position.

**Parameters:**
- x _(int)_: The vertical position in pixels.
- y _(int)_: The horizontal position in pixels.
- point _(POINT)_

**Returns:**
- `tuple` with the next items.
  
**Example:**
```python{15}
from cornelius import Cursor
from time import time, sleep

mouse = Cursor()
positions = []

velocity = 0.1 # in seconds
record_time = 5 # in seconds

start = time()
elapsed = 0
print("Recording...")

while elapsed < record_time:
  position = mouse.get()
  position.append(positions)
  elapsed = time() - start
  sleep(velocity)
    
for position in positions:
  x, y, _ = position # _ is the pointer, we don't need it :)
  mouse.set(x, y)
```

## `set()`
Sets the cursor position in pixels.

**Parameters:**
- x _(int)_: The vertical position in pixels.
- y _(int)_: The horizontal position in pixels.

**Returns:** -> `None`

**Example:**
```python{5}
from cornelius import Cursor
from time import sleep

cursor = Cursor()
cursor.set(300, 200) # Setting the cursor position
cursor.press(1)
sleep(1)
cursor.release(1)
```

## `press()`
Press a mouse button.

**Parameters:**
- button _(int)_: The button **id** to press (1: left | 2: right).

**Raises:**
- InvalidButtonException _(CorneliusException)_: If the button isn't valid.

**Returns:** -> `None`

**Example:**
```python{4}
from cornelius import Cursor

cursor = Cursor()
cursor.press(2) # Pressing the right button.
cursor.release(1)
```

## `release()`
Release a mouse button.

**Parameters:**
- button _(int)_: The button **id** to release (1: left | 2: right).

**Raises:**
- InvalidButtonException _(CorneliusException)_: If the button isn't valid.

**Returns:** -> `None`

**Example:**
```python{5}
from cornelius import Cursor

cursor = Cursor()
cursor.press(1)
cursor.release(2) # Release button
```

## `left_click()`
Send a left click.

**Parameters:**
- delay _(float)_: Delay between clicks in seconds.

**Returns:** -> `None`

**Example:**
:::danger Error 🚨
No examples was founded.
:::

## `right_click()`
Send a right click.

**Parameters:**
- delay _(float)_: Delay between clicks in seconds.

**Returns:** -> `None`

**Example:**
:::danger Error 🚨
No examples was founded.
:::

## `is_pressed()`
**Parameters:**
- button _(int)_: Button **id** to check. (1: left | 2: right).

**Raises:**
- InvalidButtonException _(CorneliusException)_: If the button isn't valid.

**Returns:** -> `boolean`: _True_ if pressed, _False_ otherwise.

**Example:**
:::danger Error 🚨
No examples was founded.
:::

## Constants
- class _cornelius.Cursor.**LEFT_BUTTON**_
- class _cornelius.Cursor.**RIGHT_BUTTON**_