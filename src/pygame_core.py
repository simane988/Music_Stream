import pygame
import os
import definitions

WIDTH = 1920
HEIGHT = 1080
FPS = 24

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)
pygame.display.set_caption("LoFi_Stream")
clock = pygame.time.Clock()
surf = pygame.Surface((WIDTH, HEIGHT))

running = True
i = 0
img_array = sorted(os.listdir(definitions.ROOT_DIR+'/media/img/'))

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    img = pygame.image.load(definitions.ROOT_DIR+"/media/img/" + img_array[i])

    img = pygame.transform.scale(img, (WIDTH, HEIGHT))

    screen.blit(img, (0, 0))

    pygame.display.update()

    if i == len(img_array) - 1:
        i = 0

    i += 1

pygame.quit()
