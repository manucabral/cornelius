from cornelius import Cursor
from time import sleep

cursor = Cursor()
cursor.set(300, 200)  # Setting the cursor position
cursor.press(1)  # Pressing the left button
sleep(1)
cursor.release(1)  # Releasing the left button 1 second later
