import time
from gfxhat import lcd

def clearScreen():
    lcd.clear()
    lcd.show()


#display object

def displayObject(obj,x,y):
    y1=0
    for i in obj:
        x1=0
        for j in i:                
            lcd.set_pixel(x+x1,y+y1,j)
            x1+=1
        y1+=1
    lcd.show()
    
#erase object

def eraseObject(obj,x,y):
    y1=0
    for i in obj:
        x1=0
        for j in i:                
            lcd.set_pixel(x+x1,y+y1,0)
            x1+=1
        y1+=1
    lcd.show()


#test 1
#while 1:
#    clearScreen(lcd)
#    displayObject(ball,15,20)
#    eraseObject(ball,15,20)
#    x+=1
#    Y+=1


#move Object
def moveObject(obj,x,y,vx,vy):
    for i in obj:
        a=i
    while x+vx<127-len(a) and y+vy<63-len(obj):
        displayObject(obj,x,y)
        time.sleep(0.05)
        eraseObject(obj,x,y)
        x=x+vx
        y=y+vy
        displayObject(obj,x,y)

#test 2

#moveObject(ball,77,5,1,1)


#check Collision
def checkCollision(obj,x=0,y=0,vx=0,vy=0,Sx=128,Sy=64):
        for i in obj:
        a=i
    while x+vx<127-len(a) and y+vy<63-len(obj):
        displayObject(obj,x,y)
        time.sleep(0.05)
        eraseObject(obj,x,y)
        x=x+vx
        y=y+vy
        displayObject(obj,x,y)
        if x+vx>=Sx-len(a):x=Sx-len(a)-vx
        if y+vy>=Sy-len(obj):y=Sy-len(obj)-vy
        if x<=0:x=0
        if y<=0:y=0





     

#test 3
checkCollision(ball,10,5,1,1,Sx=128,Sy=64)




# The new object
yh = [
[1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
[0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0],
[0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0],

]

#The program
#displayObject(yh,int(input("please enter the x(<64) of the coordinate ")),int(input("please enter the y(<32) of the coordinate ")))