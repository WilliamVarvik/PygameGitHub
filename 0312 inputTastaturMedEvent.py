import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
print(K_UP, K_DOWN, K_LEFT, K_RIGHT)
# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


class Ball:
    """Klasse for å representere en ball"""

    def __init__(self, x, y, fart, radius, farge, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart = fart
        self.radius = radius
        self.farge = farge
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.vindusobjekt, self.farge,
                       (self.x, self.y), self.radius)

    def flytt(self):
        """Metode for å flytte ballen"""
        # Henter en ordbok med status for alle tastatur-taster
        taster = pg.key.get_pressed()
        if taster[K_UP]:
            self.y -= self.fart
        if taster[K_DOWN]:
            self.y += self.fart
        if taster[K_LEFT]:
            self.x -= self.fart
        if taster[K_RIGHT]:
            self.x += self.fart


# Lager et Ball-objekt
ball = Ball(200, 200, 0.1, 20, (255, 69, 0), vindu)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        #Event styring
        # if event.type == pg.KEYDOWN:
        #     if event.key == K_UP:
        #         ball.y -= 2
        #     if event.key == K_DOWN:
        #         ball.y += 2
        #     if event.key == K_LEFT:
        #         ball.x -= 2
        #     if event.key == K_RIGHT:
        #         ball.x += 2

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballene
    ball.tegn()
    # Flytter ballen ved OOP. Vi trenger kun en av de to mulighetene
    ball.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
