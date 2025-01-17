import pygame as pg
from pygame.locals import K_ESCAPE
from pygame import MOUSEBUTTONDOWN

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

from constants import *
from game_bar import update_game_bar
from brick import create_bricks, update_bricks
from ball import Ball
from pad import Pad
from button import Button
from pictures import *





screen_width, screen_height = screen.get_size()
pause = False
click_processed = False
ball_info = []
q_var = False
brick_list = create_bricks(screen_width)

ball = Ball(farge=WHITE, radius=10, x=500, y=500, dx=10, dy=10)
pad = Pad(farge=WHITE, bredde=200, hoyde=20, fart=15, scr_width=screen_width, scr_height=screen_height)

butn1 = Button(farge=GRAY, x=screen_width - (70+30)*1 + 30, y=10, bredde=60, hoyde=60, image=pause_image)
butn2 = Button(farge=GRAY, x=screen_width - (70+30)*2 + 50, y=10, bredde=60, hoyde=60, image=restart_image)
butn3 = Button(farge=GRAY, x=screen_width - (70+30)*3 + 70, y=10, bredde=60, hoyde=60, image=quit_image)


running = True
while running:
    trykkede_taster = pg.key.get_pressed()

    for event in pg.event.get():
        if (event.type == pg.QUIT) or trykkede_taster[K_ESCAPE] or q_var:
            running = False

    clock.tick(FPS)
    screen.fill(BLACK)
   
    #GAME_BAR
    click_processed, ball_info, pause, q_var = update_game_bar(screen, butn1, butn2, butn3, pad, ball, pause, click_processed, ball_info, event, screen_width, screen_height)
    
    #PAD
    pad.oppdater(screen, screen_width, ball)
    
    #BALL
    ball.oppdater(screen, pad, screen_width, screen_height)
    
    #BRICKS
    update_bricks(screen, ball, brick_list)


    pg.display.update()

pg.quit()