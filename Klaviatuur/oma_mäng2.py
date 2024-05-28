import pygame, random
pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (240, 240, 240)
MAX_CIRCLES = 10
INITIAL_RADIUS = 10
GROWTH_RATE = 5

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Click game')

def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


running=True
clock=pygame.time.Clock()
circles=[]

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(circles) >= MAX_CIRCLES:
                circles.pop(0)
                circles.append({'pos': event.pos, 'color': get_random_color(), 'radius': INITIAL_RADIUS})
                
                screen.fill(BACKGROUND_COLOR)
                for circle in circles:
                    circle['radius'] += GROWTH_RATE
                    pygame.draw.circle(screen, circle['color'], circle['pos'], circle['radius'])
                    
                    pygame.display.flip()
                    clock.tick(30)
                    
pygame.quit()