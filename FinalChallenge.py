__author__ = 'Owner'
#!/usr/bin/env python
########################################################################
# This script uses an Ultrasonic sensor to detect a collision and turn right
#
########################################################################
#
# ! Attach Ultrasonic sensor to A1 Port.
#
########################################################################
from gopigo import *
import time

class pigo:

    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 100, 'rightspeed' : 100, 'dist' : 100}
    isMoving = False
    servoPos = 90

    def __init__(self):
            print "I'm a little robot car. beep beep."

    def stop(self):
            self.status["isMoving"] = False
            for x in range(8):
                stop()

    def fwd(self):
            self.status["isMoving"] = True
            for x in range(3):
                fwd()

    def bwd(self):
            self.status["isMoving"] = True
            for x in range(3):
                bwd()

    vision = []

    def servoSweep(self):
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.1)
            vision[ang] = us_dist(15)
            print "Checking for obstacles!"

    def turnTo(self):
        if ang < 30 and ang > 0:
            right_rot()
            time.sleep(1)
            self.stop()
        if ang < 60 and ang > 31:
            right_rot()
            time.sleep(.5)
            self.stop()
        if ang < 90 and ang > 61:
            right_rot()
            time.sleep(.2)
            self.stop()
        if ang > 90 and  ang < 120:
            left_rot()
            time.sleep(.2)
            self.stop()
        if ang > 121 and ang < 150:
            left_rot()
            time.sleep(.5)
            self.stop()
        if ang > 151 and ang < 180:
            left_rot()
            time.sleep(.1)
            self.stop()
        else:
            print "Uhhhhh this isn't working."

    def checkSpan(self):
        counter = 0
        for ang in range(20, 160, 2):
            if vision[ang] > SAFE_DISTANCE:
                counter += 1
                print "Looking for a clear path."
            else:
                counter = 0
                print "Looking for a clear path."
            if counter == 20:
                print "Let's Go!"
                self.turnTo()
                return ang

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something" + str(self.status['dist']) + "mm away."

    def safeDrive(self):
        self.fwd()
        while self.fwd():
            self.checkDist()
            if 'dist' < 30:
                self.stop()



    distance_to_stop = 30		#Distance from obstacle where the GoPiGo should stop

    def findPathRight(dist):
        self.safeDrive()
        if dist < distance_to_stop:
            self.bwd()
            self.stop()
            time.sleep(.5)
            self.servoSweep()
            self.checkSpan()
            self.fwd()
        else:
            self.SafeDrive()

tina = Pigo()
tina.findPathRight()
