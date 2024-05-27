import pygame, random
pygame.init()

WIDTH, HEIGHT=800, 600
BACKGROUND_COLOR=(240, 240, 240)
NUM_CIRCLES=10
RADIUS=30

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Кликни на круги')

def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def get_random_position():
    return random.randint(RADIUS, WIDTH - RADIUS), random.randint(RADIUS, HEIGHT - RADIUS)

circles = [{'pos': get_random_position(), 'color': get_random_color()} for _ in range(NUM_CIRCLES)]

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for circle in circles[:]:
                    circle_pos = circle['pos']
                    distance = ((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2)**0.5
                    if distance <= RADIUS:
                        circles.remove(circle)

        screen.fill(BACKGROUND_COLOR)
        for circle in circles:
            pygame.draw.circle(screen, circle['color'], circle['pos'], RADIUS)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()