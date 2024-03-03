import math
import xarm

l1 = 11
l2 = 15
arm = xarm.Controller('USB')


servo1 = xarm.Servo(1)
servo2 = xarm.Servo(2)
servo3 = xarm.Servo(3)
servo4 = xarm.Servo(4)
servo5 = xarm.Servo(5)
servo6 = xarm.Servo(6)
arm.setPosition([[3,40.0],[4,30.0],[5,30.0]], 100, wait=True)
# y=11*math.cos(math.pi/2-arm.getPosition(5,True)*math.pi/180.0)+15*math.cos(math.pi/2-arm.getPosition(5,True)*math.pi/180-arm.getPosition(4,True)*math.pi/180.0)
# z=11*math.sin(math.pi/2-arm.getPosition(5,True)*math.pi/180.0)+15*math.sin(math.pi/2-arm.getPosition(5,True)*math.pi/180-arm.getPosition(4,True)*math.pi/180.0)
# gamma = math.acos((l1**2+l2**2-y**2-z**2)/(2*l1*l2))
# print((l1**2+l2**2-y**2-z**2)/(2*l1*l2))
for i in range(3,17):
     y = 10
     z = 20-i
     gamma = math.acos((l1**2+l2**2-y**2-z**2)/(2*l1*l2))
     theta2 = math.pi-gamma
     delta = math.asin((l2*math.sin(gamma))/math.sqrt(y**2+z**2))
     theta1 = math.pi/2-math.atan(z/y)-delta
     theta1 = theta1*180.0/math.pi
     theta2 = theta2*180.0/math.pi
     theta3 = -(math.atan(z/y)+ delta+ gamma - math.pi)*180.0/math.pi+12.0
     print("theta1 is", theta1)
     print("theta2 is", theta2)
     arm.setPosition([[3,theta3],[4,theta2],[5,theta1]], 100, wait=True)
# print(theta1)
# print(theta2)

# print(arm.getPosition(5,True))
# print(arm.getPosition(4,True))
# y=11*math.cos(math.pi/2-arm.getPosition(5,True)*math.pi/180)+15*math.cos(math.pi/2-arm.getPosition(5,True)*math.pi/180-arm.getPosition(4,True)*math.pi/180)
# z=11*math.sin(math.pi/2-arm.getPosition(5,True)*math.pi/180)+15*math.sin(math.pi/2-arm.getPosition(5,True)*math.pi/180-arm.getPosition(4,True)*math.pi/180)
# print(y)
# print(z)