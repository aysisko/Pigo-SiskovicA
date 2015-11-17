#__author__ = 'siskovica'
from gopigo import *
import time
STOP_DIST = 200


class Pigo:

######
######BASIC STATUS AND METHODS
######



    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'rightspeed':175, 'dist': 100}
    isMoving = False
    servoPos = 90

    def __init__(self):
        print "I'm a little robot car. beep beep."
        self.checkDist()

#named after the GoPiGo version of stop()
    def stop(self):
        self.status["isMoving"] = False
        print "STOP get jiggy with it"
        for x in range(8):
            stop()

    def fwd(self):
        self.status["isMoving"] = True
        print "I'm on a rolllll"
        for x in range(3):
            fwd()

    def bwd(self):
        self.status["isMoving"] = True
        print "Back it up!"
        for x in range(3):
            bwd()

#Check if conditions are safe for Pigo to continue
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle within stop distance"
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
    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
            if 'dist' < 200:
                self.stop()
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160, 5):
            if ang % 15 == 0:
                servo(ang)
                time.sleep(.1)

    def spin(self):
        for x in range(3):
            right_rot()
        time.sleep(2)
        self.stop()

    def shuffle(self):
        for x in range(5):
            self.fwd()
            time.sleep(.5)
            self.bwd()
            time.sleep(.5)
        self.stop()

    def shakeServo(self):
        for x in range(3):
            self.servoSweep()
            print "Do the sprinkler"
            time.sleep(1)

    def dance(self):
        print "I just want to DANCE!"
        self.spin()
        self.shuffle()
        self.shakeServo()
        #self.rturn()
        #self.lturn()
        #self.blink()
######
######MAIN APP STARTS HERE
######
tina = Pigo()
tina.dance()
tina.stop()
