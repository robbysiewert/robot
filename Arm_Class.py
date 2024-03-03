import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Arm_Class():
    def __init__(self,pin,freq,minduty,maxduty, increment):
        self.pin = pin
        self.pulse_in_Hz = freq # 50 for 5v and 400 for 12v
        GPIO.setup(self.pin,GPIO.OUT)
        self.servo1 = GPIO.PWM(self.pin,self.pulse_in_Hz) # Note: 50 = 50Hz pulse
        self.servo1.start(0)
        self.minduty = minduty
        self.maxduty = maxduty
        self.increment = increment

    def moveto(self,button1,button2,angle):


#         increment = 0.25
        if button1 == 1 and button2 == 1:
            angle+=0
        elif button1 == 1 and button2 == 0:
            if angle >= self.maxduty - self.increment:
                angle = self.maxduty
            else:
                angle+= self.increment
            self.servo1.ChangeDutyCycle(round(angle,3))
            print(angle)
        elif button1 == 0 and button2 == 1:
            if angle <= self.minduty + self.increment:
                angle = self.minduty
            else:
                angle-= self.increment
            self.servo1.ChangeDutyCycle(round(angle,3))
            print(angle)
        else:
            self.servo1.ChangeDutyCycle(0)


        sleep(0.01)
        return angle

    def stop(self):
        self.servo1.stop()
        sleep(0.1)