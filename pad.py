import pygame as pg
from pygame.locals import (K_LEFT, K_RIGHT)

class Pad:
    def __init__(self, farge, bredde, hoyde, fart, scr_width, scr_height):
        self.farge = farge
        self.bredde = bredde
        self.hoyde = hoyde
        self.fart = fart
        self.x = (scr_width - bredde) / 2
        self.y = scr_height - 100 - hoyde
  

    def tegn(self, screen):
        pg.draw.rect(screen, self.farge, (self.x, self.y, self.bredde, self.hoyde))


    def posisjon(self, screen_width):
        trykkede_taster = pg.key.get_pressed()
        if trykkede_taster[K_LEFT] and self.x > 0:
            self.x -= self.fart
        if trykkede_taster[K_RIGHT] and self.x < screen_width - self.bredde:
            self.x += self.fart


    def ball_kollisjon(self, ball, screen_width):    
        if (self.y <= (ball.y + ball.radius) <= (self.y + self.hoyde)) and (self.x <= ball.x <= self.x + self.bredde):
            ball.dy = -abs(ball.dy)

            trykkede_taster = pg.key.get_pressed()
            if trykkede_taster[K_LEFT] and (self.x > 0) and (ball.dx > -15):
                ball.dx = ball.dx - 1
            elif trykkede_taster[K_RIGHT] and (self.x < screen_width - self.bredde) and (ball.dx < 15):
                ball.dx = ball.dx + 1
                 


    def oppdater(self, screen, screen_width, ball):
        self.tegn(screen)
        self.posisjon(screen_width)
        self.ball_kollisjon(ball, screen_width)