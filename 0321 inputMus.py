import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
print(K_UP, K_DOWN, K_LEFT, K_RIGHT)
# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.rect = pg.rect.Rect(x,y,radius,radius) #Lagrer et rect for ballen
    self.fart = fart
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  def tegn(self):
    """Metode for å tegne ballen"""
    self.rect = pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)  # oppdaterer Rectet til ballen
  def flytt(self):
    print(pg.mouse.get_pressed())
    if pg.mouse.get_pressed()[0]:
       
      pos = pg.mouse.get_pos()
      x = self.x = pos[0]
      y = self.y = pos[1]

      l = m.sqrt(x**2 + y**2)
      self.x += x/l * self.fart
      self.y += y/l * self.fart
  
# Lager et Ball-objekt
ball = Ball(200, 200, 0.1, 20, (255, 69, 0), vindu)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

        # Musetrykk    
        if event.type == pg.MOUSEBUTTONDOWN:
            print(event) # info om eventet
            if event.button == 1: # om første musetrykk
              # OBS her har vi en egenskap ball.rect som er rektangelet til ballen. Denne oppdateres i tegnemetoden.
              print(ball.rect.collidepoint(event.pos))
            
  
    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballene
    ball.tegn()
    ball.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()