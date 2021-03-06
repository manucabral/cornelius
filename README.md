# cornelius

Cornelius allows you to control mouse and keyboard inputs in a simple way.

Currently only supports **Windows**.

See full documentation [here](https://github.com/manucabral/cornelius/wiki)
## Usage

Install the [PyPI package](https://pypi.org/project/cornelius/)

```bash
pip install cornelius
```

or clone the repository

```bash
git clone https://github.com/manucabral/cornelius.git
```

## Example

Using cursor module

```py
from cornelius import Cursor

mouse = Cursor()
mouse.set(500, 500)
mouse.left_click()
```

Using keyboard module

```py
from cornelius import Keyboard

keyboard = Keyboard()
keyboard.send('a')
```

You can see more examples [here](https://github.com/manucabral/cornelius/tree/main/examples)

## Planned features

-   Mouse scrolling
-   Detect multiple clicks
-   Wait for a key/mouse input
-   Keyboard hotkeys
