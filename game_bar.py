import pygame as pg
from constants import *
from pictures import *
from brick import create_bricks


def is_button_clicked(button, event, click_processed):
    if event.type == pg.MOUSEBUTTONDOWN and not click_processed:
        if button.collidepoint(pg.mouse.get_pos()):
            return True
    return False


def pause_play_button(butn1, pad, ball, pause, click_processed, ball_info, event):
    if is_button_clicked(butn1.rect, event, click_processed):
        if not pause:
            ball_info = [ball.dx, ball.dy]
            ball.dx, ball.dy = 0, 0
            pad.fart = 0
            butn1.image = play_image
            pause = True
        else:
            ball.dx, ball.dy = ball_info
            pad.fart = 15
            butn1.image = pause_image
            pause = False
        click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False
    
    if butn1.rect.collidepoint(pg.mouse.get_pos()):
        butn1.hover = True
    else: 
        butn1.hover = False

    return pause, click_processed, ball_info


def restart_button(butn1, butn2, pad, ball, screen_width, screen_height, event, click_processed, brick_list, score, highscore, difficulity, ball_info, pause):
    if is_button_clicked(butn2.rect, event, click_processed):
            ball.x, ball.y = (screen_width/2) - ball.radius, screen_height - pad.hoyde - 150
            ball.dx, ball.dy = 5, -8
            pad.x = (screen_width - pad.bredde) / 2
            pad.y = screen_height - pad.hoyde - 100
            pad.fart = 15
            brick_list = create_bricks(screen_width, difficulity)
            ball.lives = 3
            ball_info = []
            pause = False   
            butn1.image = pause_image
            if score > highscore:
                highscore = score
            score = 0
            click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False

    if butn2.rect.collidepoint(pg.mouse.get_pos()):
        butn2.hover = True
    else: 
        butn2.hover = False

    return click_processed, brick_list, score, highscore, difficulity, ball_info, pause


def quit_button(butn3, event, click_processed):
    if butn3.rect.collidepoint(pg.mouse.get_pos()):
        butn3.hover = True
    else: 
        butn3.hover = False

    if is_button_clicked(butn3.rect, event, click_processed):
            return True


def game_bar_text(screen, screen_width, score, highscore, screen_height, ball, difficulity):
    #Score
    font_score = pg.font.SysFont("Arial", 60)
    text_score = font_score.render(f"{score}", True, BLACK)
    text_width_score, text_height_score = font_score.size(f"{score}")
    back_score = pg.Surface((text_width_score + 100, text_height_score))
    back_score.fill(BLACK)
    front_score = pg.Surface((text_width_score + 100 - 6, text_height_score - 6))
    front_score.fill(GRAY)
    back_score.blit(front_score, (3, 3))
    back_score.blit(text_score, (50, 0))
    screen.blit(back_score, (screen_width/2 - text_width_score/2 - 50, (80-text_height_score)/2))


    #Highscore
    font_high = pg.font.SysFont("Arial", 35)
    text_high = font_high.render(f"Highscore: {highscore}", True, BLACK)
    text_width_high, text_height_high = font_high.size(f"Highscore: {highscore}")
    back_high = pg.Surface((text_width_high + 30, 60))
    back_high.fill(BLACK)
    front_high = pg.Surface((text_width_high + 30 - 6, 60 - 6))
    front_high.fill(GRAY)
    back_high.blit(front_high, (3, 3))
    back_high.blit(text_high, (15, (60 - text_height_high)/2))
    screen.blit(back_high, (10, 10))



    #Lives
    font_lives = pg.font.SysFont("Arial", 35)
    text_lives = font_lives.render(f"Lives:", True, BLACK)
    text_width_lives, text_height_lives = font_lives.size(f"Lives:")
    back_lives = pg.Surface((text_width_lives + 185, 60))
    back_lives.fill(BLACK)
    front_lives = pg.Surface((text_width_lives + 185 - 6, 60 - 6))
    front_lives.fill(GRAY)
    back_lives.blit(front_lives, (3, 3))
    back_lives.blit(text_lives, (15, (60 - text_height_lives)/2))
    screen.blit(back_lives, (10, screen_height - 70))

    for i in range(3):
      if i < ball.lives:
          screen.blit(full_heart, (130 + i * 50, screen_height - 60))
      else:
          screen.blit(empty_heart, (130 + i * 50, screen_height - 60))
      

    #Difficulity
    font_diff = pg.font.SysFont("Arial", 35)
    text_diff = font_diff.render(f"Difficulity: {difficulity}", True, BLACK)
    text_width_diff, text_height_diff = font_diff.size(f"Difficulity: {difficulity}")
    back_diff = pg.Surface((text_width_diff + 90, 60))
    back_diff.fill(BLACK)
    front_diff = pg.Surface((text_width_diff + 90 - 6, 60 - 6))
    front_diff.fill(GRAY)
    back_diff.blit(front_diff, (3, 3))
    back_diff.blit(text_diff, (15, (60 - text_height_lives)/2))
    screen.blit(back_diff, (screen_width - text_width_diff - 90 - 10, screen_height - 70))


def game_bar_desing(screen, screen_width, screen_height):
    pg.draw.rect(screen, "gray", (0, 0, screen_width, 80))

    pg.draw.rect(screen, "gray", (0, screen_height-80, screen_width, 80))


def difficulity_reaset(butn1, ball, pad, screen_width, screen_height, difficulity, score, highscore, pause):
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



def difficulity_change(butn1, event, click_processed, screen_width, screen_height, screen, difficulity, ball, pad, brick_list, score, highscore, pause):
    up_rect = pg.Rect(screen_width - 75, screen_height - 66, 50, 24)
    down_rect = pg.Rect(screen_width - 75, screen_height - 39, 50, 24)

    if is_button_clicked(up_rect, event, click_processed):  
        if difficulity < 10:
            difficulity += 1
        brick_list, score, highscore, pause = difficulity_reaset(butn1, ball, pad, screen_width, screen_height, difficulity, score, highscore, pause)
        click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False

    if is_button_clicked(down_rect, event, click_processed):
        if difficulity > 1:
            difficulity -= 1
        brick_list, score, highscore, pause = difficulity_reaset(butn1,ball, pad, screen_width, screen_height, difficulity, score, highscore, pause)
        click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False

    if up_rect.collidepoint(pg.mouse.get_pos()) or difficulity == 10:
        screen.blit(sort_up_gray, (screen_width - 70, screen_height - 61, 40, 30))
    else: 
        screen.blit(sort_up, (screen_width - 70, screen_height - 61, 40, 30))
    
    if down_rect.collidepoint(pg.mouse.get_pos()) or difficulity == 1:
        screen.blit(sort_down_gray, (screen_width - 70, screen_height - 61, 40, 30))
    else: 
        screen.blit(sort_down, (screen_width - 70, screen_height - 61, 40, 30))
        

    return click_processed, difficulity, brick_list, score, highscore, pause




def update_game_bar(screen, butn1, butn2, butn3, pad, ball, pause, click_processed, ball_info, event, screen_width, screen_height, brick_list, score, highscore, difficulity):
    #Game bar general
    game_bar_desing(screen, screen_width, screen_height)
    game_bar_text(screen, screen_width, score, highscore, screen_height, ball, difficulity)

    #Draw buttons
    butn1.oppdater(screen)
    butn2.oppdater(screen)
    butn3.oppdater(screen)

    #Button functions
    pause, click_processed, ball_info = pause_play_button(butn1, pad, ball, pause, click_processed, ball_info, event)
    click_processed, brick_list, score, highscore, difficulity, ball_info, pause = restart_button(butn1, butn2, pad, ball, screen_width, screen_height, event, click_processed, brick_list, score, highscore, difficulity, ball_info, pause)
    q_var = quit_button(butn3, event, click_processed)
    click_processed, difficulity, brick_list, score, highscore, pause = difficulity_change(butn1, event, click_processed, screen_width, screen_height, screen, difficulity, ball, pad, brick_list, score, highscore, pause)


    return click_processed, ball_info, pause, q_var, brick_list, score, highscore, difficulity