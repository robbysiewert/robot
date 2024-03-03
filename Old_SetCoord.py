def SetCoord():
    if button3 == 1 and button4 == 0:
        if button1 == 1 and button2 == 1:
            pass
        elif button1 == 1 and button2 == 0:
            if l1**2 < (y+increment)**2 + z**2 < (l1+l2)**2 and y > 0:
                y+=increment
            else:
                print('Out of Range y+')
            print('y is ',y)
        elif button1 == 0 and button2 == 1:
            if l1**2 < (y-increment)**2 + z**2 < (l1+l2)**2 and y > increment:
                y-=increment
            else:
                print('Out of Range y-')
            print('y is ',y)
    elif button3 == 0 and button4 == 1:
        if button1 == 1 and button2 == 1:
            pass
        elif button1 == 1 and button2 == 0:
            if l1**2 < (y)**2 + (z+increment)**2 < (l1+l2)**2:
                z+=increment
            else:
                print('Out of Range z+')
            print('z is ',z)
        elif button1 == 0 and button2 == 1:
            if l1**2 < (y)**2 + (z-increment)**2 < (l1+l2)**2:
                z-=increment
            else:
                print('Out of Range z-')
            print('z is ',z)