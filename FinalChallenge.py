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

class Pigo:

    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 100, 'rightspeed' : 100, 'dist' : 100}
    isMoving = False
    servoPos = 90
    MIN_DIST = 30		#Distance from obstacle where the GoPiGo should stop
    vision = [None] * 180

    def __init__(self):
            print "I'm a little robot car. beep beep."

    def stop(self):
            self.status["isMoving"] = False
            for x in range(8):
                stop()
            print "Stop"

    def fwd(self):
            self.status["isMoving"] = True
            for x in range(3):
                fwd()
            print "Forward"

    def bwd(self):
            self.status["isMoving"] = True
            for x in range(3):
                bwd()
            print "Back it up"

    def rightrot(self):
            self.status["isMoving"] = True
            for x in range(3):
                right_rot()
            print "rotating right"

    ######
    ##COMPLEX METHODS
    ######
    def servoSweep(self):
        print "Checking for obstacles!"
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.1)
            self.vision[ang] = us_dist(15)

    def turnAround(self):
        self.rightrot()
        time.sleep(1.5)
        self.stop()

    #returns true if there's any 20 degree slice
    def checkSpan(self):
        counter = 0
        for ang in range(20, 160, 2):
            if self.vision[ang] > self.MIN_DIST:
                counter += 1
                print "Looking for a clear path."
            else:
                counter = 0
                print "Looking for a clear path."
            if counter >= 10:
                print "checkSpan found at least one option available"
                return True
        print "checkSpan says no options exist"
        return False

    def turnTo(self):
        ang = 90
        answer = None
        counter = 0
        option = [0] * 20
        optindex = 0
        for ang in range(20, 160, 2):
            if self.vision[ang] > self.MIN_DIST:
                counter += 1
                print "Looking for a clear path."
            else:
                counter = 0
                print "Looking for a clear path."
            if counter >= 10:
                option[optindex] = ang - 10
                answer = option[optindex]
                optindex += 1
                counter = 0
        if answer:
            ang = answer
            print ang
            print answer
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

    def checkDist(self):
        servo(90)
        self.status['dist'] = us_dist(15)
        print "I see something" + str(self.status['dist']) + "mm away."
        if self.status['dist'] < self.MIN_DIST:
            self.stop()
            return False
        else:
            return True

    def safeDrive(self):
        self.fwd()
        while self.checkDist():
            time.sleep(2)
        self.stop()

    def avoider(self):
        if self.status['dist'] < self.MIN_DIST:
            self.bwd()
            self.stop()
            time.sleep(.5)
            self.servoSweep()
            self.checkSpan()
            self.turnTo()
            self.safeDrive()
        else:
            self.safeDrive()

#Main APP starts here
tina = Pigo()

while True:
    if tina.checkDist() == True:
        tina.safeDrive()
    else:
      tina.avoider()

