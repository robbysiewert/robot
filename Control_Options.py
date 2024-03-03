# NOTES:
# Untested: Removal of sleep from dc motor move functions
#  sudo crontab -e

# Import Motor Classes
from MotorModule_High_Current import Motor
from MotorModule_DTLever_High_Current import Motor_DTLever
from Arm_Class import Arm_Class
from Arm_Class_js import Arm_Class_js
from Arm_Class_Auto import Arm_Class_Auto
# from Blue_Arm_Class import Arm_Class

global movement
# movement = 'Autonomous'
movement = 'JoyStick'

# Import Control Classes
import KeyPressModule as kp
if movement == 'JoyStick':
    import new_controller as js
#     import JoyStickModule as js
#     import JoyStickModule_boot as js

# Import Sensor Classes
from Pixy2_Camera import Pixy2_Camera
from Distance_sensor_01 import distance_sensor

# Import Libraries / Methods
from time import sleep
from os import environ # Check if still necessary with VNC
from os import system
import pygame
import RPi.GPIO as GPIO

# Variables for autonomy - camera
xmax = 315 # Max x value of camera
xcenter = xmax/2 # Center of camera x axis
x_cam_norm = 1/xcenter # Normalize x to 0 - 1
pixy_err = 5 # camera input error - dependent on testing
dt_speed = 1 # Standard forward driving speed for drivetrain 0-1
# global angle1 #, angle2, angle3, angle4, angle5
door_lever_sig = 1; door_handle_sig = 2; door_lip = 3 # color sig associated with objects

# Variables for autonomy - distances
approach_door_dist = 10
servo3_looking_up = 10; servo3_looking_down = 5
traversed_through_door = False
side_dist_buffer = 5; dt_approach_dist = 10; arm_approach_dist = 2
time_to_move_through_door = 10

# Initialization Angles for the Arm
init_angle = 50
# angle1 = init_angle; angle2 = init_angle; angle3 = init_angle; angle4 = init_angle; angle5 = init_angle; init_angle = init_angle
angle1 = 47; angle2 = 60; angle3 = 56; angle4 = 7.5; angle5 = 9.9;
shutdown_started = False
pin_button = 8

############################################################

def JoyStick_Control(motor, motor_DTLever, servo1_2, servo3, servo4, servo5, distL): #servo1_2, servo3
    global angle1, angle2, angle3, angle4, angle5, shutdown_started
    motor.move(-js.getJS()['axis2'],-js.getJS()['axis1']) #Negatives Adjust for direction
    motor_DTLever.move(js.getJS()['L2'],js.getJS()['R2'],js.getJS()['L1'],js.getJS()['R1'])
    angle1, angle2 = servo1_2.moveto( js.getJS()['axis3'],-js.getJS()['axis4'], angle1, angle2)
    angle3 = servo3.moveto(js.getJS()['x'],js.getJS()['o'],angle3)
    angle4 = servo4.moveto(js.getJS()['s'],js.getJS()['t'],angle4)
    angle5 = servo5.moveto(js.getJS()['L2'],js.getJS()['R2'],angle5)
    print(js.getJS())
#     print(distL.dist())
    if js.getJS()['L1'] == 1 and js.getJS()['L2'] == 1 and js.getJS()['R1'] == 1 and js.getJS()['R2'] == 1 and shutdown_started == False:
        shutdown_started = True
        system('shutdown now -h')


def Autonomous_Control(motor, motor_DTLever,servo1_2, servo3, servo4, servo5):
    pass
#     while not approach_interaction(door_lever_sig):
#         approach_interaction(door_lever_sig)
#     interact_lever()
#     while not approach_interaction(door_handle_sig):
#         approach_interaction(door_handle_sig)
#     interact_handle()
#     while not move_to_door(door_lip):
#         move_to_door(door_lip)
#     dt_forward(time_to_move_through_door)


#     print('Camera 1:', pixy2.sig(), 'Camera 2:', pixy2_rear.sig())


def Shutdown(channel):
    print('Shutting Down')
#     time.sleep(5)
#     os.system('sudo shutdown -h now')

def Initialize_Objects():

    pin1 = 13
    pin2 = 19
    pin3 = 26
    pin4 = 20
    pin5 = 21

    absminduty = 0
    absmaxduty = 100
    minduty_5v = 2.5
    maxduty_5v = 12.5
    freq_5v = 50
    freq_12v = 400
    claw_min_duty = 8.5
    claw_max_duty = 11.5

    GPIO.setup(pin_button,GPIO.IN,pull_up_down = GPIO.PUD_UP)

        # Check if these are still necessary with VNC
    environ['DISPLAY'] = ':0'
    pygame.display.init()

#         Establish Motor Objects (Pins)
    motor = Motor(17,27,22,10)
    motor_DTLever = Motor_DTLever(9,11)

    inc = 0.5; inc_5v = 0.1
    increment1 = inc; increment2 = inc; increment3 = inc; increment4 = inc_5v; increment5 = inc_5v;
    servo1_2 = Arm_Class_js(pin1,pin2,freq_12v,absminduty, absmaxduty,50,100,increment1,increment2)
    servo3 = Arm_Class(pin3,freq_12v,absminduty,absmaxduty,increment3)
    servo4 = Arm_Class(pin4,freq_5v,minduty_5v,maxduty_5v,increment4)
    servo5 = Arm_Class(pin5,freq_5v,claw_min_duty,claw_max_duty,increment5)

#     servo1_2.moveto(0.1,0.1, angle1, angle2)
#     servo3.moveto(0,1,angle3)
#     servo4.moveto(0,1,angle4)
#     servo5.moveto(0,1,angle5)

#       #Establish camera object
#     serial_port_00 = '/dev/ttyUSB0'
#     serial_port_01 = '/dev/ttyUSB1'
#     pixy2 = Pixy2_Camera(serial_port_00)
#     pixy2_rear = Pixy2_Camera(serial_port_01)

#       #Establish distance sensor objects Set trigger and echo pins
    trig1 = 0; echo1 = 0; trigL = 1; echoL = 7; trigR = 5; echoR = 6
#         dist1 = distance_sensor(trig1,echo1)
    distL = distance_sensor(trigL,echoL)
#         distR = distance_sensor(trigR,echoR)


    return motor, motor_DTLever,servo1_2, servo3, servo4, servo5, distL #, pixy2, pixy2_rear#, dist1, distL, distR



def control_method():
    global movement
    return movement

def KeyBoard_Control(motor):

    if kp.getKey('UP'):
        motor.move(0.6,0); print('Key UP was pressed')
    elif kp.getKey('DOWN'):
        motor.move(-0.6,0); print('Key DOWN was pressed')
    elif kp.getKey('LEFT'):
        motor.move(0.5,0.3); print('Key LEFT was pressed')
    elif kp.getKey('RIGHT'):
        motor.move(0.5,-0.3); print('Key RIGHT was pressed')
    else:
        motor.stop(0.1)

def JoyStick_boot_Control(motor, motor_DTLever, servo1_2, servo3, servo4, servo5): #servo1_2, servo3
    global angle1, angle2, angle3, angle4, angle5
    motor.move(js.getJS()['axis2'],-js.getJS()['axis1']) #Negatives Adjust for direction
    motor_DTLever.move(js.getJS()['x'],js.getJS()['o'],0.3)
#     angle1, angle2 = servo1_2.moveto( js.getJS()['axis3'],-js.getJS()['axis4'], angle1, angle2)
#     angle3 = servo3.moveto(js.getJS()['x'],js.getJS()['o'],angle3)
#     angle4 = servo4.moveto(js.getJS()['s'],js.getJS()['t'],angle4)
#     angle5 = servo5.moveto(js.getJS()['share'],js.getJS()['options'],angle5)

    print(js.getJS())


def approach_interaction(object):
#     if left and right distances are larger than side distance buffer
    if distL.dist() > side_dist_buffer and distR.dist() > side_dist_buffer:
#         if color sig detected
        if pixy2.x_coord() != -1:
#             if color sig == door_lever
            if pixy2.sig() == object:
#                if front distance is larger than approach distance
                if dist1.dist() > dt_approach_dist:
#                 move drivetrain towards color
                    motor.move(dt_speed, ((xcenter - pixy2.x_coord())*x_cam_norm)) # DC motors move to center object
                else:
#                     if front distance is larger than interact distance
                    if dist1.dist() > arm_approach_dist:
#                         move arm towards color
                        angle1 = servo1.moveto(angle1 + ((pixy2.x_coord() - xcenter)*x_cam_norm))
                        angle2 = servo2.moveto(angle2 + ((dist1.dist() - arm_approach_dist)/dist1.dist()))
                    else:
                        return True # Manip is ready to open lever
            else:
#                 look for color sig
                attempt = 0; sig_found = False
                while sig_found == False:
                    sig_found, angle1, angle3, attempt = look_for_sig(sig_found, angle1, angle3, attempt)
        else:
#             look for color sig
            attempt = 0; sig_found = False
            while sig_found == False:
                sig_found, angle1, angle3, attempt = look_for_sig(sig_found, angle1, angle3, attempt)


#     elif left dist is smaller than buffer
    elif distL < side_dist_buffer:
#         move to the right using left dc motor
        motor.move('Right')
#     elif right dist is smaller than buffer
    elif distR < side_dist_buffer:
#         move to the left using left dc motor
        motor.move('Left')
    else:
        motor.stop() # If both sides are too close to obstacle then stop dc motors
    return False

def interact_lever(): # Psuedo Autonomous Code with predefined servo movements
    angle2 = servo2.moveto(angle2 + 0.5) # move forward against door below lever
    # Change if using 12v servos - use servo4
    angle3 = servo3.moveto(angle3 + 3) # move up partially opening lever
    angle2 = servo2.moveto(angle2 + 0.5) # move forward to adjust manips contact with lever
    angle1 = servo1.moveto(angle1 + 4) # move arm right to fully open lever
    reset_arm()  # reset arm


def interact_handle(): # Psuedo Autonomous Code with predefined servo movements
    angle5 = servo5.moveto() # Open Claw
    angle2 = servo2.moveto(angle2 + 1) # Move forward to get handle within grasp
    angle5 = servo5.moveto(getattr(servo5,'minduty')) # Close Claw
    for open_door in range(100): # 100 is arbitrary num of loops to open door
        angle5 = servo5.moveto(getattr(servo5,'minduty')) # Close Claw
        motor.move(-0.3,0) # Move backward
        angle1 = servo1.moveto(angle1 + -0.1) # Move Arm left to aid in opening door
        angle1 = servo1.moveto(angle1 + 4) # move arm right to fully open lever
    for move_away in range(20): # 20 is arbitrary num loops to move away
        motor.move(-0.3,0)
    reset_arm()  # reset arm

def move_to_door(object):
#     if left and right distances are larger than side distance buffer
    if distL.dist() > side_dist_buffer and distR.dist() > side_dist_buffer:
#         if color sig detected
        if pixy2.x_coord() != -1:
#             if color sig == door_lever
            if pixy2.sig() == object:
#                if front distance is larger than approach distance
                if dist1.dist() > dt_approach_dist:
#                 move drivetrain towards color
                    motor.move(dt_speed, ((xcenter - pixy2.x_coord())*x_cam_norm)) # DC motors move to center object
                else:
                    return True
            else:
#                 look for color sig
                attempt = 0; sig_found = False
                while sig_found == False:
                    sig_found, angle1, angle3, attempt = look_for_sig(sig_found, angle1, angle3, attempt)
        else:
#             look for color sig
            attempt = 0; sig_found = False
            while sig_found == False:
                sig_found, angle1, angle3, attempt = look_for_sig(sig_found, angle1, angle3, attempt)


#     elif left dist is smaller than buffer
    elif distL < side_dist_buffer:
#         move to the right using left dc motor
        motor.move('Right')
#     elif right dist is smaller than buffer
    elif distR < side_dist_buffer:
#         move to the left using left dc motor
        motor.move('Left')
    else:
        motor.stop() # If both sides are too close to obstacle then stop dc motors
    return False


def dt_forward(time):
    motor.move(1,0)
    sleep(time)





def reset_arm():
    servo1.moveto(init_angle); servo2.moveto(init_angle); servo3.moveto(init_angle);servo4.moveto(init_angle); servo5.moveto(init_angle);


def look_for_sig(sig_found, angle1, angle3, attempt):
    increment = 0.1

    # Sweep Left to Right
    if attempt == 0:
        angle1 = 0; angle3 = init_angle
    elif attempt > 0 and attempt < 10/increment: # 10 is duty 2.5 to 12.5
        angle1 = angle1 + increment; angle3 = init_angle

    # Sweep Down to Up
    elif attempt == 10/increment:
        angle1 = init_angle; angle3 = 0
    elif attempt > 10/increment and attempt < 20/increment:
        angle1 = init_angle; angle3 = angle2 + increment

    # Sweep Left to Right Looking Up
    elif attempt == 20/increment:
        angle1 = 0; angle3 = servo3_looking_up
    elif attempt > 20/increment and attempt <= 30/increment:
        angle1 = angle1 + increment; angle3 = servo3_looking_up

    # Sweep Left to Right Looking Down
    elif attempt == 20/increment:
        angle1 = 0; angle3 = servo3_looking_down
    elif attempt > 20/increment and attempt <= 30/increment:
        angle1 = angle1 + increment; angle3 = servo3_looking_down

    angle1 = servo1.moveto(angle1)
    angle3 = servo3.moveto(angle3)

    attempt += 1

    if pixy2.x_coord() != -1:
        sig_found = True
    else:
        sig_found = False

    return sig_found, angle1, angle3, attempt