# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True: # Loop forever

    time.sleep(0.5) # Short delay

    if button1.value() == 1: #If button 1 is pressed

        print("Button 1 pressed")

        red.toggle() # Toggle Red LED on/off

    elif button2.value() == 1: # If buttone 2 is pressed
        print("button 2 pressed")

        amber.toggle() # Toggle Amber on/off

    elif button3.value() == 1: # if button 3 is pressed
        print("Button 3 pressed")

        green.toggle() # Toggle Green on/off
