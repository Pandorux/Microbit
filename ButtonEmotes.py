# Add your Python code here. E.g.
from microbit import *


while True:
    if button_b.is_pressed() and button_a.is_pressed():
        display.show(Image.CONFUSED)
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.ANGRY)
    else:
        display.show(Image.SAD)
        
display.clear()

    
