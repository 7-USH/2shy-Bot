import pyautogui as pt
from time import sleep


def cursor():
    sleep(3)
    position = pt.locateOnScreen("smiley_image.png",confidence = 0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+120,y-70,duration=0.5)
    position = pt.locateOnScreen("arrow.png",confidence = 0.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x+35,y,duration=0.5)
    pt.click()
    sleep(0.1)
    reply_position = pt.locateOnScreen("reply.png",confidence = 0.7)
    a = reply_position[0]
    b = reply_position[1]
    pt.moveTo(a,b,duration=0.5)
    pt.click()
    pt.typewrite("hello",interval=0.05)

cursor()