from cornelius import Keyboard
from time import sleep

kb = Keyboard()
text = 'hello'

for c in text:
    kb.press(c)
    sleep(0.1)
