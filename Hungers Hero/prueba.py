import pygame, sys

pygame.init()

tamano = (1000, 600)
screen = pygame.display.set_mode(tamano)
clock = pygame.time.Clock()
white = (255, 255, 255)
bg = pygame.image.load("img/FondosMapas/Desieto.jpg")
bg = pygame.transform.scale(bg,(1000, 600))
tamano = pygame.display.set_mode(tamano)

msc = pygame.mixer.Sound("sounds/intro.mp3")

pygame.mixer.Sound.play(msc, loops=-1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            clock.tick(60)
            running = False