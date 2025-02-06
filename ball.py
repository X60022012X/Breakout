import pygame as pg
from constants import *

class Ball:
    def __init__(self, farge, radius, x, y, dx, dy):
        self.farge = farge
        self.radius = radius
        self.x = x
        self.y = y
        self.dx = dx 
        self.dy = dy
        self.lives = 3

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def posisjon(self):
        self.x += self.dx 
        self.y += self.dy

    def vegg_kollisjon(self, screen_width):
        if self.x <= self.radius:
            self.dx = abs(self.dx)

        if self.x >= screen_width - self.radius:
            self.dx = -abs(self.dx)

        if self.y <= self.radius + 80:
            self.dy = abs(self.dy)

    def game_over(self, screen, screen_width, screen_height, pad):
        if (self.y + self.radius) >= (screen_height - 80):
            if self.lives <= 1:
                self.lives = 0
                self.dx = 0
                self.dy = 0
                pad.fart = 0 
    
                transparent_surface = pg.Surface((screen_width, screen_height-80), pg.SRCALPHA)
                pg.draw.rect(transparent_surface, (10, 10, 10, 200), (0, 0, screen_width, screen_height-160))
                screen.blit(transparent_surface, (0, 80))
                
                text = "GAME OVER"
                font = pg.font.SysFont("Arial", 200)
                tekst_surface = font.render(text, True, WHITE)
                text_width, text_height = font.size(text)
                screen.blit(tekst_surface, (screen_width/2 - text_width/2, screen_height/2 - text_height/2))

            else:
                self.lives -= 1
                self.x, self.y = (screen_width/2) - self.radius, screen_height - pad.hoyde - 150
                self.dx, self.dy = 5, -8
                pad.x = (screen_width - pad.bredde) / 2
                pad.y = screen_height - pad.hoyde - 100
                pad.fart = 15
            


    def oppdater(self, screen, pad, screen_width, screen_height):
        self.tegn(screen)
        self.posisjon()
        self.vegg_kollisjon(screen_width)
        self.game_over(screen, screen_width, screen_height, pad)