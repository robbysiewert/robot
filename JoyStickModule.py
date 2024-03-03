# In Pi Terminal
###########################

#sudo apt-get -y install jd
#Install Ds4:
#sudo pip3 install ds4drv
#sudo wget https://raw.githubusercontent.com//chrippa/ds4drv/master/udev/50-ds4drv.rules -O /etc/udev/rules.d/50-ds4drv.rules
#sudo udevadm control --reload-rules
#sudo udevadm trigger
#sudo nano /etc/rc.local
# add next line after # By default this script does nothing
#/usr/local/bin/ds4drv &
# control o control x
# then connect via bluetooth

###########################

import pygame
from time import sleep
from os import environ

pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()
buttons = {'x':0.,'o':0.,'t':0.,'s':0.,
           'L1':0.,'R1':0.,'L2':0.,'R2':0.,
	   'share':0.,'options':0.,
           'axis1':0.,'axis2':0.,'axis3':0.,'axis4':0.}

axiss = [0.,0.,0.,0.,0.,0.]

environ['DISPLAY'] = ':0'
pygame.display.init()

def getJS(name=''):

    global buttons
    #retrieve any events
    use_joystick = False
    for event in pygame.event.get():                                 # Analog Sticks
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(event.value,2)
        elif event.type == pygame.JOYBUTTONDOWN:                     # When Button pressed
#             print(event.dict,event.joy,event.button,'PRESSED')
            for x,(key,val) in enumerate(buttons.items()):
                if x < 10:
                    if controller.get_button(x): buttons[key] = 1
        elif event.type == pygame.JOYBUTTONUP:                       # When Button released
#             print(event.dict,event.joy,event.button,'RELEASED')
            for x,(key,val) in enumerate(buttons.items()):
                if x < 10:
                    if event.button == x: buttons[key] = 0

    # to remove element 2 since axis numbers are 0 1 3 4
    buttons['axis1'], buttons['axis2'], buttons['axis3'], buttons['axis4'] = [axiss[0],axiss[1],axiss[3],axiss[4]]

    if name == '':
        return buttons
    else:
        return buttons[name]

def main():
    print(getJS())
    sleep(0.1)

if __name__ == '__main__':
    while True:
        main()