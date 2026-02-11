from OpenGL.GL import *    
from OpenGL.GLUT import *  
from OpenGL.GLU import *   
import random


Dspeed = 0.3
x0 = random.choice([40,45,110,210,310,389,420,465])
colors = [(1.0,0.0,0.0),(1.0,0.5,0.0),(1.0,0.85,0.0),(0.0,0.75,0.75),(0.9,0.0,0.6)]
r,g,b = random.choice(colors)
cr,cg,cb = 1.0, 1.0, 1.0
y0 = 700
prev_y0 = y0
gameOver = False
cx0 = 200
cy0 = 25
catcherSpeed = 6
score = 0
autoPlayFlag = False
autoPlaySpeed  = 0.001 
diamondBox = []
catcherBox = []
bstScore = -1
playPauseFlag = True


def dxdyFinder(start,end):
     x0,y0 = start
     x1,y1 = end
     dx = x1-x0
     dy = y1-y0
     return dx,dy



def findZone(start,end):
     dx,dy = dxdyFinder(start,end)
     if (dx == 0 and dy == 0 ) or (dx == 0 or dy == 0):
               return 0
     if dx>0 and dy>0 :
          if abs(dx)>abs(dy):
               return 0
          else:
               return 1 
     elif dx<0 and dy>0 :
          if abs(dy)>abs(dx):
               return 2
          else:
               return 3 
     elif dx<0 and dy<0 :
          if abs(dx)>abs(dy):
               return 4
          else :
               return 5
     elif dx>0 and dy<0 :
          if abs(dy)>abs(dx):
               return 6
          else :
               return 7
 
 
          
def convertZone0(start, end, zone):
    x0, y0 = start
    x1, y1 = end
    if zone == 0 or zone is None:
        return start, end    
    if zone == 1:
        nStart = (y0, x0)
        nEnd   = (y1, x1)
    elif zone == 2:
        nStart = (y0, -x0)
        nEnd   = (y1, -x1)
    elif zone == 3:
        nStart = (-x0, y0)
        nEnd   = (-x1, y1)
    elif zone == 4:
        nStart = (-x0, -y0)
        nEnd   = (-x1, -y1)
    elif zone == 5:
        nStart = (-y0, -x0)
        nEnd   = (-y1, -x1)
    elif zone == 6:
        nStart = (-y0, x0)
        nEnd   = (-y1, x1)
    elif zone == 7:
        nStart = (x0, -y0)
        nEnd   = (x1, -y1)
    return nStart, nEnd  


 
def MPL(start,end):
    dx,dy = dxdyFinder(start,end)
    D= 2*dy - dx
    NE = 2*(dy-dx)
    E = 2*dy 
    x,y = start
    x1,y1 = end 
    listPixels = [[x,y]]
    if dx == 0 :
       while y<y1 :
          y+=1
          listPixels.append([x,y])  
             
    while x<x1 : 
       x+=1 
       if D>0 :
          y += 1
          D+=NE
       else:
          D += E   
       listPixels.append([x,y])  
    return listPixels       



def convertToOriginal(lst , zone ):
     newList = [] 
     for i in lst :
          x, y = i[0], i[1] 
          if zone == 1: 
               newList.append([y, x])
          elif zone == 2: 
               newList.append([-y, x])    
          elif zone == 3: 
               newList.append([-x, y])                          
          elif zone == 4: 
               newList.append([-x, -y])
          elif zone == 5: 
               newList.append([-y, -x])               
          elif zone == 6: 
               newList.append([y, -x])               
          elif zone == 7: 
               newList.append([x, -y])                             
     return  newList 



def design(lst,r,g,b):
     for i in lst:      
         start = i[0]
         end = i[1]
         zone = findZone(start,end)
         glColor3f(r, g, b)
         if zone!=0:
              NewStart,NewEnd = convertZone0(start,end,zone)
              listPixel = MPL(NewStart,NewEnd)
              listUpPixel = convertToOriginal(listPixel,zone)
              drawPixel(listUpPixel)
         else :
              listPixel = MPL(start,end)  
              drawPixel(listPixel)


               
def drawPixel(lst):
     for i in lst: 
         glPointSize(1) 
         glBegin(GL_POINTS) 
         x, y = i[0], i[1] 
         glVertex2f(x, y)
         glEnd()   
         
         
                                                     
def diamond():
    global x0 ,y0  ,r,g,b , diamondBox
    x = x0-7
    y = y0-30
    diamondBox=[x,y,14,30]
    x1 = x0+7
    y2 = y1 = y0-15
    x2 = x0-7
    x3 = x0
    y3 = y0-30
    cordinatelst = [[(x0,y0),(x1,y1)],[(x0,y0),(x2,y2)],[(x2,y2),(x3,y3)],[(x1,y1),(x3,y3)]] 
    design(cordinatelst,r,g,b)    
    
    
    
def catcher():
     global cx0,cy0,catcherSpeed,catcherBox,cr,cg,cb
     x = cx0
     y = cy0 - 20
     catcherBox = [x,y,100,20]
     x1 = cx0+100
     y1 = cy0
     x2 = cx0+15
     y2 = y3 = cy0-20
     x3 = x1 -15
     cordinatelst = [[(cx0,cy0),(x1,y1)],[(cx0,cy0),(x2,y2)],[(x2,y2),(x3,y3)],[(x1,y1),(x3,y3)]]
     design(cordinatelst,cr,cg,cb) 
     
     
     
def cross():
     cordinatelst = [[(430,765),(460,735)],[(430,735),(460,765)]]
     r,g,b = 1.0, 0.0, 0.0
     design(cordinatelst,r,g,b)                



def playPause():
     r,g,b = 1.0, 1.0, 0.0
     if playPauseFlag == True :
          cordinatelst = [[(235,735),(235,765)],[(255,735),(255,765)]]
          design(cordinatelst,r,g,b)  
                       
     else :
          cordinatelst = [[(235,735),(235,765)],[(235,765),(255,750)],[(235,735),(255,750)]]
          design(cordinatelst,r,g,b)    
          
          
                 
def lArrow():
     r,g,b = 0.0, 0.85, 0.95
     cordinatelst = [[(25,750),(60,750)],[(25,750),(40,765)],[(25,750),(40,735)]]
     design(cordinatelst,r,g,b)  
     
     
     
def mouse_listener(button, state, x, y):
     global playPauseFlag , score ,gameOver,Dspeed,catcherSpeed ,y0,x0,colors,cr,cg,cb,r,g,b,autoPlayFlag
     yPrime = 800 - y
     glutPostRedisplay() 
     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
          if (235<=x<=255 ) and (735<=yPrime<=765):             
              playPauseFlag = not playPauseFlag     
          if (430<=x<=460) and (735<=yPrime<=765) :
               print(f"Goodbye | Your total Score : {score}")
               gameOver = not gameOver 
               glutLeaveMainLoop() 
          if (22<=x<=60) and (735<=yPrime<=765):
               Dspeed = 0.1
               catcherSpeed = 6
               score = 0  
               y0 = 700
               x0 = random.choice([40,45,110,210,310,389,420,465])
               colors = [(1.0,0.0,0.0),(1.0,0.5,0.0),(1.0,0.85,0.0),(0.0,0.75,0.75),(0.9,0.0,0.6)]
               r,g,b = random.choice(colors)
               cr,cg,cb = 1.0, 1.0, 1.0
               gameOver = not True
               playPauseFlag = not False
               autoPlayFlag = False
               print("Starting a New Game ")  
   
   
                  
def scoreUpdate(lst1,lst2):
     global score, Dspeed, catcherSpeed, cr, cg, cb ,y0, x0, colors, r, g, b, gameOver, playPauseFlag
     if ((lst1[0] < lst2[0] + lst2[2] ) and (lst1[0] + lst1[2] > lst2[0]) and (lst1[1] < lst2[1] + lst2[3] ) and (lst1[1] + lst1[3] > lst2[1])): 
          score += 1
          print(f"Score : {score}")  
          y0 = 700
          x0 = random.choice([40,45,110,210,310,389,420,465])
          colors = [(1.0,0.0,0.0),(1.0,0.5,0.0),(1.0,0.85,0.0),(0.0,0.75,0.75),(0.9,0.0,0.6)]
          r,g,b = random.choice(colors)  
          Dspeed += 0.008
          catcherSpeed += 0.002
     elif y0 <= 0:
          gameOver = True
          playPauseFlag = False
          cr,cg,cb = 1.0, 0.0, 0.0
          print(f"Game Over | Total Score --> {score}")     
        
         
                                               
def special_key_listener(key, x, y):    
    global cx0 ,catcherSpeed,playPauseFlag
    if playPauseFlag == True :
       maxRight = 400
       if key == GLUT_KEY_RIGHT:
            cx0 = min(cx0 + catcherSpeed, maxRight)  
       elif key == GLUT_KEY_LEFT:
            cx0 = max(cx0 - catcherSpeed, 0)
       glutPostRedisplay()              
 
 
 
def keyboard_listener(key, x, y):
    global autoPlayFlag
    if key == b'c': 
        if autoPlayFlag == False:
             autoPlayFlag = True
             print("Cheat Mode Activate")
        else:
             autoPlayFlag = False
             print("Cheat Mode Deactivate")  
 
                           
                       
def autoPlay():
    global x0, y0, cx0, cy0, autoPlaySpeed,score,bstScore
    center = x0 - 50
    maxRight = 400
    if cx0 > center:
        step = int(abs(cx0 - center))
        for i in range(step):
            cx0 -= autoPlaySpeed
            if cx0 < 0:
                cx0 = 0
            if cx0 > maxRight:
                cx0 = maxRight
            if cx0 <= center:
                cx0 = center
                if cx0 < 0:
                    cx0 = 0
                if cx0 > maxRight:
                    cx0 = maxRight
                break
    else:
        step = int(abs(center - cx0))
        for i in range(step):
            cx0 += autoPlaySpeed
            if cx0 < 0:
                cx0 = 0
            if cx0 > maxRight:
                cx0 = maxRight
            if cx0 >= center:
                cx0 = center
                if cx0 < 0:
                    cx0 = 0
                if cx0 > maxRight:
                    cx0 = maxRight
                break
    if score != 0 and score % 7 == 0 and bstScore != score:
          autoPlaySpeed += 0.001
          bstScore = score
  
  
                    
def setup_projection():
    glViewport(0,0,500,800)
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    glOrtho(0.0,500.0,0.0,800.0,-1.0,1.0);
    glMatrixMode(GL_MODELVIEW)



def animate():
    global y0, Dspeed, x0, r, g, b, playPauseFlag, diamondBox, catcherBox
    if playPauseFlag == True :
        if autoPlayFlag == True :
             autoPlay() 
        y0 -= Dspeed
        scoreUpdate(diamondBox, catcherBox)
        
        if y0 <= -30:
            y0 = 700
            x0 = random.choice([40,45,110,210,310,389,420,465])
            r, g, b = random.choice(colors)
            glColor3f(r, g, b)
        glutPostRedisplay()



def display():
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glLoadIdentity()
     setup_projection()
     diamond()
     catcher()
     cross()
     playPause()
     lArrow()
     glutSwapBuffers()  



def main():
    glutInit()                               
    glutInitDisplayMode(GLUT_RGBA)          
    glutInitWindowSize(500, 800)            
    glutInitWindowPosition(750, 150)          
    glutCreateWindow(b"Catch the Diamonds!")    
    glutDisplayFunc(display)
    glutIdleFunc(animate) 
    glutSpecialFunc(special_key_listener) 
    glutMouseFunc(mouse_listener)  
    glutKeyboardFunc(keyboard_listener)              
    glutMainLoop()                           



if __name__ == "__main__":
    main()