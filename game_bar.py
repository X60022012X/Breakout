import pygame as pg
from constants import *
from pictures import *
import tekst

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

    return pause, click_processed, ball_info


def restart_button(butn2, pad, ball, screen_width, screen_height, event, click_processed):
    if is_button_clicked(butn2.rect, event, click_processed):
            ball.x, ball.y = 500, 500
            ball.dx, ball.dy = 10, 10
            pad.x = (screen_width - pad.bredde) / 2
            pad.y = screen_height - pad.hoyde - 100
            pad.fart = 15
            if pad.score > pad.highscore:
                pad.highscore = pad.score
            pad.score = 0
            click_processed = True
    elif event.type == pg.MOUSEBUTTONUP:
        click_processed = False

    return click_processed


def quit_button(butn3, event, click_processed):
    if is_button_clicked(butn3.rect, event, click_processed):
            return True


def game_bar_text(screen, screen_width, pad):
    #Score
    text = f"{pad.score}"
    font = pg.font.SysFont("Arial", 60)
    tekst_surface = font.render(text, True, BLACK)
    text_width, text_height = font.size(text)
    back_surface = pg.Surface((text_width + 100, text_height))
    back_surface.fill(GRAY)
    back_surface.blit(tekst_surface, (50, 0))
    screen.blit(back_surface, (screen_width/2 - text_width/2 - 50, (80-text_height)/2))

    #Highscore
    tekst.skriv_tekst(screen, 20, 20, f"Highscore: {pad.highscore}", BLACK, 35, "Arial")


def game_bar_desing(screen, screen_width):
    pg.draw.rect(screen, "gray", (0, 0, screen_width, 80))





def update_game_bar(screen, butn1, butn2, butn3, pad, ball, pause, click_processed, ball_info, event, screen_width, screen_height):
    #Draw buttons
    butn1.oppdater(screen)
    butn2.oppdater(screen)
    butn3.oppdater(screen)

    #Button functions
    pause, click_processed, ball_info = pause_play_button(butn1, pad, ball, pause, click_processed, ball_info, event)
    click_processed = restart_button(butn2, pad, ball, screen_width, screen_height, event, click_processed)
    q_var = quit_button(butn3, event, click_processed)

    #Game bar general
    game_bar_desing(screen, screen_width)
    game_bar_text(screen, screen_width, pad)

    return click_processed, ball_info, pause, q_var