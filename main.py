import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')
fps = 60
clock = pygame.time.Clock()

while True:
    clock.tick(fps)

    pygame.display.flip()