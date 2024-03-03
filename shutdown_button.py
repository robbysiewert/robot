# restart program execution https://stackoverflow.com/questions/48129942/python-restart-program
#  button hold https://raspberrypi.stackexchange.com/questions/63512/how-can-i-detect-how-long-a-button-is-pressed
# Event detected https://raspberrypi.stackexchange.com/questions/119152/my-gpio-event-detected-code-is-unreliable

# Simple script for shutting down the Raspberry Pi at the press of a button.
import RPi.GPIO as GPIO
import time
import os

# movement = 'Joystick'
pin_button = 26
num_press = 0
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Setup the pin with internal pullups enabled and pin in reading mode.
GPIO.setmode(GPIO.BCM)

# GPIO.add_event_detect(pin_button, GPIO.FALLING, callback=change_modes, bouncetime=2000)
# Our function on what to do when the button is pressed
def Shutdown(channel):

    print("Shutting Down")
#     time.sleep(1)
#     os.system("sudo shutdown -h now")

# Add our function to execute whe#     movement = 'Autonomous'n the button pressed event happens

def ChangeModes(channel):

    global num_press
    num_press+=1
    print(num_press)

#     if num_press % 2 == 0:
#         print('Code Block 1')
#     else:
#         print('Code Block 2')
#     print(num_press)

#     global num_press
#     if channel != 0:
#         num_press+=1
#     if num_press % 2 == 0:
#         print('Code Block 1')
#     else:
#         print('Code Block 2')
#     print(movement)
#     print(num_press)
#     print('Running')
#     time.sleep(1)


def main(movement):
    print(movement)
    time.sleep(.001)




# GPIO.add_event_detect(pin_button, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

# Now wait!

# while 1:

#     time.sleep(1)
# GPIO.add_event_detect(pin_button, GPIO.FALLING, callback=main, bouncetime=2000)
# GPIO.add_event_detect(pin_button, GPIO.FALLING, callback=ChangeModes, bouncetime=2000)
# GPIO.add_event_detect(pin_button, GPIO.RISING)


if __name__ == '__main__':
    GPIO.add_event_detect(pin_button, GPIO.FALLING, callback=ChangeModes, bouncetime=500)
    try:
        while True:
            if num_press % 2:
                main('Joystick')
            else:
                main('Autonomous')

    except KeyboardInterrupt:
        print('Execution Aborted By User')
        GPIO.cleanup()

