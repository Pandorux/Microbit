# Add your Python code here. E.g.
from microbit import *

brightness = 9

while True:

    for x in range(5):
        light = brightness - x
        for y in range(5):
            light = light - 1
            
            if light < 0:
                light = 9
            
            display.set_pixel(x, y, light)
            
    brightness = brightness - 1
    if brightness < 0:
        brightness = 9
    
    sleep(100)
    
