import pygame as pg

class Button:
    def __init__(self, farge, x, y, bredde, hoyde, image):
        self.farge = farge
        self.bredde = bredde
        self.hoyde = hoyde
        self.x = x
        self.y = y
        self.image = image
        self.rect = pg.Rect(self.x, self.y, self.bredde, self.hoyde)

    def tegn(self, screen):
        pg.draw.rect(screen, self.farge, (self.x, self.y, self.bredde, self.hoyde))
        screen.blit(self.image, (self.x + 10, self.y + 10))

    def oppdater(self, screen):
        self.tegn(screen)
    