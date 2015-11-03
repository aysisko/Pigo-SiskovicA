__author__ = 'siskovica'
from GoPiGo import *
import time

class Pigo:

######
######BASIC STATUS AND METHODS
######


    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'rightspeed' : 175}
    isMoving = False
    servoPos = 90

    def __init__(self):
        print "I'm a little robot car. beep beep."

#named after the GoPiGo version of stop()
    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "Whoops, sorry boss."

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "Can't do the vroom vroom."


######
######COMPLEX METHODS
######

######
######MAIN APP STARTS HERE
######

tina = Pigo()
tina.fwd()
time.sleep(2)
tina.stop()
