import pygame
import sys
pygame.init() #Pygame'i tööle rakendamiseks
#värvid
lGreen=[153, 255, 153]
lBlue=[153, 204, 255]

ekraani_pind=pygame.display.set_mode((640, 480))
ekraani_pind.fill(lGreen)
pygame.display.set_caption("Esimene mäng")

gameover=False
while not gameover:
    #Lisame pildid
    youWin=pygame.image.load("win.jpg")
    youWin=pygame.transform.scale(youWin,[300, 200])
    ekraani_pind.blit(youWin,[180, 100])
    
    pygame.display.flip()
    #mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
pygame.quit() #Pygame välja lülitamine