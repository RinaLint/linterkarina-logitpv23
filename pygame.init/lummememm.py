import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((600, 600))
ekraani_pind.fill( (0,0,0))
pygame.display.set_caption("Lumemees")

center_coordinates=(150, 100) 
radius=30  
pygame.draw.circle(ekraani_pind, (255, 255, 255), center_coordinates, radius)
center_coordinates=(150, 50) 
radius=30  
pygame.draw.circle(ekraani_pind, (255, 255, 255), center_coordinates, radius)
center_coordinates=(150, 0) 
radius=30  
pygame.draw.circle(ekraani_pind, (255, 255, 255), center_coordinates, radius)

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()