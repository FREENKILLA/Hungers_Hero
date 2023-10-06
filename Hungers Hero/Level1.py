import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        size = (1000, 600) 
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hungers_Hero_Lv1")
        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("img/principal/Tilin_right.png")
        self.img_pos = [500, 300]
        self.movement = [False, False]

        

    def run(self):
        while True:
            Desierto = pygame.image.load("img/FondosMapas/Desieto.jpg")
            Desierto = pygame.transform.scale(Desierto,(1000, 600))
            self.img_pos[1] += self.movement[1] - self.movement[0] * 2
            #self.screen.fill ((14, 219, 248))
            self.screen.blit(Desierto, (0, 0))

            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement [1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement [1] = False
            pygame.display.update()
            self.clock.tick(60)

Game().run()