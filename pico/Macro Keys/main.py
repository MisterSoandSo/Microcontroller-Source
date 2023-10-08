import time
import usb_hid
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Define button pins
btn1_pin = board.GP9
btn2_pin = board.GP8
btn3_pin = board.GP7
btn4_pin = board.GP19
btn5_pin = board.GP20
btn6_pin = board.GP21

# Function to initialize button input
def initialize_button(pin):
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    return btn

# Initialize buttons
btn1 = initialize_button(btn1_pin)
btn2 = initialize_button(btn2_pin)
btn3 = initialize_button(btn3_pin)
btn4 = initialize_button(btn4_pin)
btn5 = initialize_button(btn5_pin)
btn6 = initialize_button(btn6_pin)

# Initialize the USB HID keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

while True:
    if btn1.value:
        layout.write('git push\n')
        time.sleep(0.1)
    if btn2.value:
        layout.write('git pull\n')
        time.sleep(0.1)
    if btn3.value:
        layout.write('git log\n')
        time.sleep(0.1)
    if btn4.value:
        layout.write('git status\n')
        time.sleep(0.1)
    if btn5.value:
        layout.write('git add')
        time.sleep(0.1)
    if btn6.value:
        layout.write('git commit -m ""')
        time.sleep(0.1)
    time.sleep(0.1)