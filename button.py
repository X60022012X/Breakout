import pygame as pg
from constants import *

class Button:
    def __init__(self, x, y, image):
        self.farge = GRAY
        self.bredde = 60
        self.hoyde = 60
        self.x = x
        self.y = y
        self.image = image
        self.rect = pg.Rect(self.x, self.y, self.bredde, self.hoyde)
        self.hover = False

    def tegn(self, screen):
        back = pg.Surface((self.bredde, self.hoyde))
        back.fill(BLACK)
        
        front = pg.Surface((self.bredde - 6, self.hoyde - 6))
        if self.hover:
            front.fill(LIGHT_GRAY)
        else:
            front.fill(GRAY)

        back.blit(front, (3, 3))
        back.blit(self.image, (10, 10))

        screen.blit(back, (self.x, self.y))


    def oppdater(self, screen):
        self.tegn(screen)
    