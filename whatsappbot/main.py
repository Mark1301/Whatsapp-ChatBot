import pyautogui as pt
from time import sleep
import pyperclip
import random
import math

sleep(2)

position1 = pt.locateOnScreen("C:/Users/HP/Pictures/Screenshots/Screenshot.png", confidence=.6)
x = position1[0]
y = position1[1]


def get_message():
    global x, y

    position = pt.locateOnScreen("C:/Users/HP/Pictures/Screenshots/Screenshot.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 70, y - 70, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Received: "+ whatsapp_message)
    return whatsapp_message


def post_response(message):
    global x, y

    position = pt.locateOnScreen("C:/Users/HP/Pictures/Screenshots/Screenshot.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Master will reply soon..."
    else:
        return "Master Will reply as soon as possible.Thank-you."


processed_message = process_response(get_message())

post_response(processed_message)
