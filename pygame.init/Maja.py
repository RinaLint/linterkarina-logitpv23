import pygame
import sys
import random
pygame.init()
#värvid
red=[255, 0, 0]
green=[0, 255, 0]
blue=[0, 0, 255]
pink=[255, 153, 255]
lBlue=[0, 85, 255]
#ekraani seaded
ekraani_pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Majake")
ekraani_pind.fill(lBlue)

ristkylik1=pygame.Rect(0,400,640,480) #Argumentid: x koordinat, y koordinat, laius, kõrgus.
pygame.draw.rect(ekraani_pind,(0,102,7),ristkylik1) #surface, color, Rect

#funktsioonid
def drawHouse(x, y, width, height, screen, color):
    points=[(x, y- ((3/4)*height)), (x,y), (x+width,y), (x+width,y-(3/4)*height),
            (x, y- ((3/4)*height)), (x+width/2,y-height), (x+width, y-(3/4)*height)]
    suurus=random.randint(1,10)
    pygame.draw.lines(screen, color, False, points, suurus)

def Uks(x, y, width, height, screen, color):
    points=[(x,y), (x,y-(1/2)*height), (x+(1/3)*width,y-(1/2)*height), (x+(1/3)*width, y), (x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(screen, color, True, points, suurus)
    pygame.draw.circle(screen, color, (x+10,y- (1/4)+height), 10)

def Aken(x, y, width, height, screen, color):
    points=[(x,y), (x,y-(1/3)*height), (x+(1/3)*width,y-(1/3)*height), (x+(1/3)*width,y), (x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(screen, color, True, points, suurus)
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    fon=[r,g,b]

center_cordinates=(450,60)
radius=40
pygame.draw.circle(ekraani_pind, (238,230,166), center_cordinates, radius )

#kutsun funktsiooni välja
drawHouse(100, 400, 300, 400, ekraani_pind, red)
Uks(100, 400, 300, 400, ekraani_pind, red)
Aken(100, 400, 300, 400, ekraani_pind, red)
pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()