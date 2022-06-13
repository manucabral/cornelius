from cornelius import Cursor
from time import time, sleep

"""
    A simple mouse recorder that records mouse movement.
    Note: This is a very simple implementation.
"""

mouse = Cursor()
positions = []

velocity = 0.1  # in seconds
record_time = 5  # in seconds

start = time()
elapsed = 0
print("Recording..")
while elapsed < record_time:
    position = mouse.get()
    positions.append(position)
    elapsed = time() - start
    sleep(velocity)

print('Recorded successfully!')
print('Executing recorded sequence')

for position in positions:
    x, y, _ = position  # _ is the pointer, we don't need it!
    mouse.set(x, y)
    sleep(velocity)
