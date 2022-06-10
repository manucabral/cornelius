from cornelius import Cursor
from time import sleep

cursor = Cursor()
cursor.set(300, 200)
sleep(1)
cursor.click(1)  # left button
sleep(1)
cursor.click(2)  # right button
