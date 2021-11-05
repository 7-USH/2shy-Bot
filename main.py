import pyautogui as pt
from time import sleep
import pyperclip


sleep(2)

postion_one = pt.locateOnScreen("smiley_image.png",confidence=.6)
x = postion_one[0]
y = postion_one[1]

def get_message():
    global x,y
    postion = pt.locateOnScreen("smiley_image.png",confidence=.6)
    x = postion[0]
    y = postion[1]
    pt.moveTo(x,y,duration=.5)
    pt.moveTo(x+120,y-70,duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(10,-150)
    pt.click()
    return pyperclip.paste()

def response(message):
    # global x,y
    # postion = pt.locateOnScreen("smiley_image.png",confidence=.6)
    # x = postion[0]
    # y = postion[1]
    # pt.moveTo(x+200,y+20,duration=.5)
    # pt.click()
    # pt.typewrite(message=message,interval=0.01)
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
    pt.typewrite(message=message,interval=0.05)
    pt.typewrite("\n",interval=0.01)
    

def process_respone(message):
    

    if "?" in str(message).lower():
        return "I don't know the answer to this question - 2shy Bot"
    elif "@2SH"in str(message):
        return "Sorry sir/madam Tushar is busy right now - 2shy Bot"
    elif "tutorial" in str(message).lower():
        return "All the Best Everyone - 2shy Bot"
    elif "assignment" in str(message).lower():
        return "Mera baki hai karna - 2shy Bot"
    elif "thanks" in str(message).lower(): 
        return "Welcome - 2shki Bot"
    elif "himanshuchan" in str(message):
        return "Himanshu-Chan kawai :3 - 2shy Bot"
    elif "delhi" in str(message).lower():
        return "Nitboi chutiya - 2shy Bot"
    elif "gandu" in str(message).lower():
        return "bruh - 2shy Bot"
    elif "lodi" in str(message) :
        return "bsdk - 2shy Bot"
    elif "Hey this is 2shy Bot" in str(message):
        return "Hey don't copy me  Bsdk - 2shy Bot"       
    else:
        return "Hey this is 2shy Bot"        

def check_newmessage():
    pt.moveTo(x+120,y-50)
    while True :
        try:
            postion = pt.locateOnScreen("noti_image.png",confidence=.7)

            if postion is not None:
                pt.moveTo(postion)
                pt.moveRel(-100,0)
                pt.click()
                pt.sleep(.5)
        
        except(Exception):
            print("no new messages from other user located")
        if pt.pixelMatchesColor(int(x+120),int(y-50),(38,45,49),tolerance=10):
            print("new message")
            processed_message = process_respone(get_message())
            response(processed_message)
        else:
            print("no new messages")
        sleep(5)      

check_newmessage()