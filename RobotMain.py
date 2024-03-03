import RPi.GPIO as GPIO
from time import sleep
from os import system

import Control_Options as ctl

motor, motor_DTLever,servo1_2, servo3, servo4, servo5, distL = ctl.Initialize_Objects()

############################################################

def main(movement):

#     Input all objects into functions
    if movement == 'JoyStick':
        ctl.JoyStick_Control(motor, motor_DTLever,servo1_2, servo3, servo4, servo5,distL)
    elif movement == 'Autonomous':
        ctl.Autonomous_Control(motor, motor_DTLever,servo1_2, servo3, servo4, servo5)
    else:
        print('Set Type of Control')



def ChangeModes(channel):
    print('Button Pressed')
    shutdown_button_hold = 5
    sleep(shutdown_button_hold)
    if GPIO.input(channel) == 0:
        print('Shutdown Initiated')
        system('shutdown now -h')
        sleep(1)
    else:
        global num_press
        num_press+=1


if __name__ == '__main__':
    control_button = 18; num_press = 0
    GPIO.setup(control_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(control_button, GPIO.FALLING, callback=ChangeModes, bouncetime=1000)

    try:
        while True:
            if num_press % 2 == 0:
                movement = 'JoyStick'
            else:
                movement = 'Autonomous'
            main(movement)

    except KeyboardInterrupt:
        print('Execution Aborted By User')

#         servo1_2.stop()
#         servo3.stop()
#         servo4.stop()
#         servo5.stop()
#         print('Servos Stopped')
        GPIO.cleanup()
        print('Clean')
    GPIO.cleanup()