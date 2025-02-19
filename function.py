import pygame as pg
from constants import *
from pictures import *
from brick import create_bricks



def is_button_clicked(button, event, click_processed):
    if event.type == pg.MOUSEBUTTONDOWN and not click_processed:
        if button.collidepoint(pg.mouse.get_pos()):
            return True
    return False



def pause_func(butn1, pad, ball):
    ball_info = [ball.dx, ball.dy]
    ball.dx, ball.dy = 0, 0
    pad.fart = 0
    butn1.image = play_image
    pause = True
    return ball_info, pause



def unpause_func(butn1, pad, ball, ball_info):
    ball.dx, ball.dy = ball_info
    pad.fart = 15
    butn1.image = pause_image
    pause = False
    return pause



def restart_func(butn1, pad, ball, screen_width, screen_height, score, highscore, difficulity):
    ball.x, ball.y = (screen_width/2) - ball.radius, screen_height - pad.hoyde - 150
    ball.dx, ball.dy = 5, -8
    pad.x = (screen_width - pad.bredde) / 2
    pad.y = screen_height - pad.hoyde - 100
    pad.fart = 15
    brick_list = create_bricks(screen_width, difficulity)
    ball.lives = 3
    pause = False   
    butn1.image = pause_image
    if score > highscore:
        highscore = score
    score = 0
    return brick_list, score, highscore, pause



def difficulity_reset(butn1, ball, pad, screen_width, screen_height, difficulity, score, highscore, pause):
    ball.x, ball.y = (screen_width/2) - ball.radius, screen_height - pad.hoyde - 150
    ball.dx, ball.dy = 5, -8
    pad.x = (screen_width - pad.bredde) / 2
    pad.y = screen_height - pad.hoyde - 100
    pad.fart = 15
    brick_list = create_bricks(screen_width, difficulity)
    ball.lives = 3
    score = 0
    highscore = 0
    pause = False   
    butn1.image = pause_image
    return brick_list, score, highscore, pause



def text_size(size, content):
    font = pg.font.SysFont("Arial", size)
    text = font.render(content, True, BLACK)
    text_width, text_height = font.size(content)
    
    return text_width, text_height, text



def text_box(screen, text_width, text_height, text, back_width_height, back_color, front_width_height, front_color, font_position, text_position, screen_width, screen_height, position):
    back = pg.Surface(back_width_height)
    back.fill(back_color)

    front = pg.Surface(front_width_height)
    front.fill(front_color)

    back.blit(front, font_position)
    back.blit(text, text_position)

    screen.blit(back, position)

    return text_width, text_height