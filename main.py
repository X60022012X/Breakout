import pygame as pg
from pygame.locals import K_ESCAPE

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)


from constants import *
from pictures import *
from game_bar import update_game_bar
from brick import create_bricks, update_bricks
from ball import Ball
from pad import Pad
from button import Button


screen_width, screen_height = screen.get_size()
pause = False
click_processed = False
ball_info = []
q_var = False
difficulity = 1
highscore = 0
score = 0

brick_list = create_bricks(screen_width, difficulity)



ball = Ball(farge=WHITE, radius=10, x=screen_width/2 - 5, y=screen_height- 150, dx=5, dy=-8)
pad = Pad(farge=WHITE, bredde=200, hoyde=20, fart=15, scr_width=screen_width, scr_height=screen_height)


butn1 = Button(x=screen_width - (75*1 - 5), y=10, image=pause_image)
butn2 = Button(x=screen_width - (75*2 - 5), y=10, image=restart_image)
butn3 = Button(x=screen_width - (75*3 - 5), y=10, image=quit_image)

running = True
while running:
    trykkede_taster = pg.key.get_pressed()
    for event in pg.event.get():
        if (event.type == pg.QUIT) or trykkede_taster[K_ESCAPE] or q_var:
            running = False

    clock.tick(60)
    screen.fill(BLACK)
   
    #PAD
    pad.oppdater(screen, screen_width, ball)
    
    #BRICKS
    score = update_bricks(screen, pad, ball, screen_width, screen_height, brick_list, score, difficulity)

    #BALL
    ball.oppdater(screen, pad, screen_width, screen_height)

    #GAME_BAR
    click_processed, ball_info, pause, q_var, brick_list, score, highscore, difficulity = update_game_bar(screen, butn1, butn2, butn3, pad, ball, pause, click_processed, ball_info, event, screen_width, screen_height, brick_list, score, highscore, difficulity)
    

    pg.display.update()

pg.quit()