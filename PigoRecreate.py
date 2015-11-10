#__author__ = 'siskovica'
from gopigo import *
import time

class Pigo:

######
######BASIC STATUS AND METHODS
######

    STOP_DIST = 50

    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'rightspeed':175, 'dist': 100}
    isMoving = False
    servoPos = 90

    def __init__(self):
        print "I'm a little robot car. beep beep."
        self.status['dist'] = us_dist(15)

#named after the GoPiGo version of stop()
    def stop(self):
        self.status["isMoving"] = False
        print "STOP get jiggy with it"
        for x in range(3):
            stop()

    def fwd(self):
        self.status["isMoving"] = True
        print "I'm on a rolllll"
        for x in range(3):
            fwd()

#Check if conditions are safe for Pigo to continue
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle withtin stop distance"
            return False
        elif volt() > 14 or volt() < 6:
            print "Voltage Outside of Safe Range: " + str(volt())
            return False
        else:
            return True

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something" + str(self.status['dist']) + "mm away."

######
######ADVANCED METHODS
######
    #def self.spin(degree)

    def dance(self):
        print "I just want to DANCE!"
        self.spin()
        self.shuffle()
        self.shakeServo()
        self.rturn()
        self.lturn()
        self.blink()
######
######MAIN APP STARTS HERE
######
tina = Pigo()

while tina.keepGoing():
    tina.checkDist()
    tina = Pigo()
    tina.fwd()
    if tina.keepGoing() == False:
        break
    time.sleep(2)
    tina.stop()

tina.stop()
