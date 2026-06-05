import sys

import pygame

from classes.Enemy import Enemy
from classes.Player import Player

pygame.init()

SCREEN_W, SCREEN_H = 800, 600
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
background = pygame.transform.scale(pygame.image.load("images/background.jpg"), (SCREEN_W, SCREEN_H))
pygame.display.set_caption("Ping-Pong")

player1 = Player("images/platform.png", 107, 408, 0, 4, 40, 200)
player2 = Player("images/platform_enemy.png", 107, 408, 0, 4, 735, 200)
player1.change_size_factor(0.3)
player2.change_size_factor(0.3)
player1.reset()
player2.reset()

ball = Enemy('images/ball.png', 224, 224, 0, 5, (300, 200), end_pos=None)
ball.change_size_factor(0.3)


fps = 60
clock = pygame.time.Clock()

while True:
    clock.tick(fps)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.rect.top > 0:
        player1.rect.y -= player1.speed
    if keys[pygame.K_s] and player1.rect.bottom < SCREEN_H:
        player1.rect.y += player1.speed

    if keys[pygame.K_UP] and player2.rect.top > 0:
        player2.rect.y -= player2.speed
    if keys[pygame.K_DOWN] and player2.rect.bottom < SCREEN_H:
        player2.rect.y += player2.speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(background, (0, 0))
    window.blit(player1.image, player1.rect)
    window.blit(player2.image, player2.rect)
    window.blit(ball.image, ball.rect)

    pygame.display.flip()