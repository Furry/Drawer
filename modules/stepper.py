import time
import RPi.GPIO as GPIO

class Stepper_28BYJ_48:
    def __init__(self, _port1, _port2, _port3, _port4):
        self.port1 = _port1
        self.port2 = _port2
        self.port3 = _port3
        self.port4 = _port4
        self.totalSteps = 0
        self.stepIndex = 0
        self.steps = [
            [1, 0, 0, 0],
            [1, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]
        ]

        GPIO.setmode(GPIO.BCM)
        for pin in self.pins():
            GPIO.setup(pin, GPIO.OUT)
        #END
    #END

    def pins(self):
        return [self.port1, self.port2, self.port3, self.port4]
    #END

    def clockwise(self):
        self.totalSteps += 1
        if 7 < self.stepIndex + 1:
            self.stepIndex = 0
        else:
            self.stepIndex = self.stepIndex + 1
        #END

        GPIO.output(self.pins(), self.steps[self.stepIndex])
        time.sleep(0.001)
    #END

    def counterclockwise(self):
        self.totalSteps -= 1
        if 0 > self.stepIndex - 1:
            self.stepIndex = 7
        else:
            self.stepIndex = self.stepIndex - 1
        # END

        GPIO.output(self.pins(), self.steps[self.stepIndex])
        time.sleep(0.001)
    #END

    def stepTo(self, stepCount):
        while self.totalSteps != stepCount:
            if self.totalSteps > stepCount:
                self.counterclockwise()
            else:
                self.clockwise()
            #END
            print(self.totalSteps)
        #END
    #END
#END