import pygame as pg

def skriv_tekst(screen, x, y, tekst, farge, storrelse, font):
  font = pg.font.SysFont(font, storrelse)
  tekst_surface = font.render(tekst, True, farge)
  screen.blit(tekst_surface, (x, y))

