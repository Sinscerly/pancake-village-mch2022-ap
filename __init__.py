import display
import buttons
import urequests
import wifi
import time
import mch22
import sys

url = "https://pv.sirminion.nl/pancakes"

a1 = "pancakes.png"

APP_PATH = "/".join(__file__.split("/")[:-1])
sys.path.append(APP_PATH)

def connectToWifi(print):
    if not wifi.status():
        wifi.connect()
        if print:
          displayPancakes("Connecting to wifi...")
        if not wifi.wait():
          return 0
        return 1

def loadPancakes(print):
  state = connectToWifi(print)
  if state:
    pancakes = urequests.get(url).text
    displayPancakes("Pancakes made: " + pancakes)
  elif print:
    displayPancakes("Failed, press A")

def displayPancakes(message):
    display.drawFill(display.BLACK)
    display.drawText(20, 10, "Pancake village pancakes", display.WHITE, "roboto_regular22")    
    display.setDefaultFont("roboto_regular18")

    display.drawText(40, 50, message, display.WHITE)

    display.drawPng(80, 80, "%s/%s" % (APP_PATH, a1))

    display.drawText(20, 170, "Free pancakes from 17:00-19:00", display.WHITE)
    display.drawText(20, 190, "Come to Pancake village", display.WHITE)
    display.flush()

def on_action_btn(pressed):
  if pressed:
    while True:
      loadPancakes(False)
      time.sleep(30)

def on_home_btn(pressed):
  if pressed:
    mch22.exit_python()

buttons.attach(buttons.BTN_A, on_action_btn)
buttons.attach(buttons.BTN_B, on_home_btn)
buttons.attach(buttons.BTN_HOME, on_home_btn)

loadPancakes(True)
