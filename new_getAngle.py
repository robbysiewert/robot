
def getAngle(button1,button2,button3,button4,y,z):

     l1 = 11
     l2 = 15
     increment = 0.5
     minangle = -100.0
     maxangle = 100.0

     if button3 == 1:
        if button1 == 1 and button2 == 1:
            y+=0.0
        elif button1== 1 and button2 == 0:
            y+=increment
#             if angle >= maxangle:
#                 angle = maxangle
#             elif angle <= minangle:
#                 angle = minangle
        elif button1 == 0 and button2 == 1:
            y-= increment
#             if angle >= maxangle:
#                 angle = maxangle
#             elif angle <= minangle:
#                 angle = minangle
     elif button4 == 1:
        if button1 == 1 and button2 == 1:
            z+=0.0
        elif button1== 1 and button2 == 0:
            z+=increment
#             if angle >= maxangle:
#                 angle = maxangle
#             elif angle <= minangle:
#                 angle = minangle
        elif button1 == 0 and button2 == 1:
            z-= increment
     gamma = math.acos((l1**2+l2**2-y**2-z**2)/(2*l1*l2))
     # print(gamma)
     theta1 = math.pi-gamma
     # print((l2*math.sin(gamma))/math.sqrt(y**2+z**2))
     delta = math.asin((l2*math.sin(gamma))/math.sqrt(y**2+z**2))
     alpha = math.pi-(math.atan(z/y)+delta)
     theta2 = math.pi/2-alpha
     theta2 = theta2*180.0/math.pi
     theta1 = -theta1*180.0/math.pi
     # print(theta1)
     # print(theta2)
     #     print(angle)
     return theta1, theta2