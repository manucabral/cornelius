from cornelius import Cursor
from time import sleep

cursor = Cursor()
cursor.move(x=300, y=200)
sleep(1)
cursor.click(button=1)
sleep(1)
cursor.click(button=2)
