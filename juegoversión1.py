import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Dark Fantasy Game")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("Juego/data/images/characters/knight.png")
        self.img = pygame.transform.scale(self.img, (64, 64)) # Ajusta el (64, 64) al ancho y alto que prefieras

        self.img_pos = [160, 360] # Posición inicial de la imagen
        self.movement = [False, False]

        self.collision_area = pygame.Rect(300, 400, 100, 60) #primero es x y luego y, luego ancho y alto

    def run(self):
        while True:
            self.screen.fill((0, 0, 70))  # Rellena la pantalla con negro

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r. colliderect (self.collision_area ):
                pygame.draw.rect(self.screen, (216, 191, 216), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (150, 100, 216), self.collision_area)

            self.img_pos[0] += (self.movement[1] - self.movement[0]) * 5  # Mueve la imagen a la izquierda o derecha
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    elif event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    elif event.key == pygame.K_d:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()