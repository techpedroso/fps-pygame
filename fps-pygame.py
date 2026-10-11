import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FPS Game")

running = True

while running:
    screen.fill((25, 28, 45))

    pygame.draw.rect(
        screen,
        (60, 200, 140),
        (300, 50, 100, 100)
    )

    #Update de screen content
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()