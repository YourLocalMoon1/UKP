## client.py ##

# UKP's client file #
# !DO NOT TOUCH ANYTHING THERE, UNLESS YOU KNOW WHAT YOU'RE DOING! #

import eel
import SS
Enc = SS.Encryption()
eel.init("web")  

@eel.expose
def testPy():
    print("Button CLICk")
    return 'yoyo, the button has been clicked'

eel.start("index.html")
