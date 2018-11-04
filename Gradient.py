# Add your Python code here. E.g.
from microbit import *


while True:
    light = 9
    for x in range(5):
        light = 9 - x
        for y in range(5):
            #light = light - y
            display.set_pixel(x, y, light)

    
