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

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def posisjon(self):
        self.x += self.dx 
        self.y += self.dy

    def vegg_kollisjon(self, screen_width):
        if self.x <= self.radius or self.x >= screen_width - self.radius:
            self.dx = -self.dx
        if self.y <= self.radius + 80:
            self.dy = -self.dy

    def game_over(self, screen, screen_width, screen_height, pad):
        if (self.y + self.radius) >= screen_height:
            self.dx = 0
            self.dy = 0
            pad.fart = 0 

            text = "GAME OVER"
            font = pg.font.SysFont("Arial", 100)
            tekst_surface = font.render(text, True, WHITE)
            text_width, text_height = font.size(text)
            screen.blit(tekst_surface, (screen_width/2 - text_width/2, screen_height/2 - text_height/2 - 200))



    def oppdater(self, screen, pad, screen_width, screen_height):
        self.tegn(screen)
        self.posisjon()
        self.vegg_kollisjon(screen_width)
        self.game_over(screen, screen_width, screen_height, pad)