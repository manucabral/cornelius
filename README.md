# cornelius
Cornelius allows you to control mouse and keyboard inputs in a simple way.

Currently only supports **Windows**.

## Usage
Clone the repository
```bash
git clone https://github.com/manucabral/cornelius.git
```

## Example
Using cursor module
```py
from cornelius import Cursor

mouse = Cursor()
mouse.set(500, 500)
mouse.press(1) # left click
```
Using keyboard module
```py
from cornelius import Keyboard

keyboard = Keyboard()
keyboard.press('a')
keyboard.release('a')
```

You can see more examples [here](https://github.com/manucabral/cornelius/tree/main/examples)

## Planned features
- Mouse scrolling
- Detect multiple clicks
- Wait for a key/mouse input
- Rewrite modules using SendInput function

## Limitations
Currently cornelius uses the win32 events functions so does not work in some applications or video games.
