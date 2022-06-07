from cornelius import Keyboard
from time import sleep

kb = Keyboard()
kb.press(key='a')
kb.delete()
sleep(1)
kb.type(text='Hello World')
