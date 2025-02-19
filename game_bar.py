import pygame as pg
from constants import *
from pictures import *
from function import *



def pause_play_button(butn1, pad, ball, pause, click_processed, ball_info, event):
    #Pause/Play button
    if is_button_clicked(butn1.rect, event, click_processed):
        if not pause:
            ball_info, pause = pause_func(butn1, pad, ball)
        else:
            pause = unpause_func(butn1, pad, ball, ball_info)
        click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False
    
    #Hover effect
    if butn1.rect.collidepoint(pg.mouse.get_pos()):
        butn1.hover = True
    else: 
        butn1.hover = False

    return pause, click_processed, ball_info



def restart_button(butn1, butn2, pad, ball, screen_width, screen_height, event, click_processed, brick_list, score, highscore, difficulity, ball_info, pause):
    #Restart button
    if is_button_clicked(butn2.rect, event, click_processed):
        brick_list, score, highscore, pause = restart_func(butn1, pad, ball, screen_width, screen_height, score, highscore, difficulity)
        click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False

    #Hover effect
    if butn2.rect.collidepoint(pg.mouse.get_pos()):
        butn2.hover = True
    else: 
        butn2.hover = False

    return click_processed, brick_list, score, highscore, difficulity, ball_info, pause



def quit_button(butn3, event, click_processed):
    #Hover effect
    if butn3.rect.collidepoint(pg.mouse.get_pos()):
        butn3.hover = True
    else: 
        butn3.hover = False

    #Quit button
    if is_button_clicked(butn3.rect, event, click_processed):
        return True



def game_bar_text(screen, screen_width, score, highscore, screen_height, ball, difficulity):
    #Score
    text_width, text_height, text = text_size(60, f"{score}")
    back_width_height = (text_width + 100, text_height)
    front_width_height = (text_width + 100 - 6, text_height - 6)
    font_position = (3, 3)
    text_position = (50, 0)
    position = (screen_width / 2 - text_width / 2 - 50, (80 - text_height) / 2)  
    text_box(screen, text_width, text_height, text, back_width_height, BLACK, front_width_height, GRAY, font_position, text_position, screen_width, screen_height, position)  
    

    #Highscore
    text_width, text_height, text = text_size(35, f"Highscore: {highscore}")
    back_width_height = (text_width + 30, 60)
    front_width_height = (text_width + 30 - 6, 60 - 6)
    font_position = (3, 3)
    text_position = (15, (60 - text_height)/2)
    position = (10, 10)  
    text_box(screen, text_width, text_height, text, back_width_height, BLACK, front_width_height, GRAY, font_position, text_position, screen_width, screen_height, position)  


    #Lives
    text_width, text_height, text = text_size(35, f"Lives:")
    back_width_height = (text_width + 185, 60)
    front_width_height = (text_width + 185 - 6, 60 - 6)
    font_position = (3, 3)
    text_position = (15, (60 - text_height)/2)
    position = (10, screen_height - 70) 
    text_box(screen, text_width, text_height, text, back_width_height, BLACK, front_width_height, GRAY, font_position, text_position, screen_width, screen_height, position)  
    
    for i in range(3):
      if i < ball.lives:
          screen.blit(full_heart, (130 + i * 50, screen_height - 60))
      else:
          screen.blit(empty_heart, (130 + i * 50, screen_height - 60))
      

    #Difficulity
    text_width, text_height, text = text_size(35, f"Difficulity: {difficulity}")
    back_width_height = (text_width + 90, 60)
    front_width_height = (text_width + 90 - 6, 60 - 6)
    font_position = (3, 3)
    text_position = (15, (60 - text_height)/2)
    position = (screen_width - text_width - 90 - 10, screen_height - 70) 
    text_box(screen, text_width, text_height, text, back_width_height, BLACK, front_width_height, GRAY, font_position, text_position, screen_width, screen_height, position)  
    


def game_bar_desing(screen, screen_width, screen_height):
    #Game bars
    pg.draw.rect(screen, "gray", (0, 0, screen_width, 80))
    pg.draw.rect(screen, "gray", (0, screen_height-80, screen_width, 80))



def difficulity_change_btn(butn1, event, click_processed, screen_width, screen_height, screen, difficulity, ball, pad, brick_list, score, highscore, pause):
    #Buttons
    up_rect = pg.Rect(screen_width - 75, screen_height - 66, 50, 24)
    down_rect = pg.Rect(screen_width - 75, screen_height - 39, 50, 24)

    #Increase difficulity
    if is_button_clicked(up_rect, event, click_processed):  
        if difficulity < 10:
            difficulity += 1
        brick_list, score, highscore, pause = difficulity_reset(butn1, ball, pad, screen_width, screen_height, difficulity, score, highscore, pause)
        click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False

    #Decrease difficulity
    if is_button_clicked(down_rect, event, click_processed):
        if difficulity > 1:
            difficulity -= 1
        brick_list, score, highscore, pause = difficulity_reset(butn1, ball, pad, screen_width, screen_height, difficulity, score, highscore, pause)
        click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False

    #Draw buttons
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
    click_processed, difficulity, brick_list, score, highscore, pause = difficulity_change_btn(butn1, event, click_processed, screen_width, screen_height, screen, difficulity, ball, pad, brick_list, score, highscore, pause)

    return click_processed, ball_info, pause, q_var, brick_list, score, highscore, difficulity