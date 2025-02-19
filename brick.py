import pygame as pg
from constants import *
from pictures import *
import math as M


def create_bricks(screen_width, difficulity):
    block_width = screen_width/10
    block_height = 35
    brick_list = []

    for i in range(BLOCKS_PER_ROW):
        for j in range(BLOCKS_PER_COL):
            x = i * block_width + 5
            y = j * block_height + 80 + 6
            rect = pg.Rect(x, y, block_width - 10, block_height - 6)
            brick_list.append([rect, difficulity])  
    return brick_list



def pre_render_difficulty_text(font, color):
    difficulty_surfaces = {}
    for difficulty in range(1, 11):
        text_surface = font.render(str(difficulty), True, color)
        difficulty_surfaces[difficulty] = text_surface
    return difficulty_surfaces



def draw_bricks(screen, brick_list, difficulty_surfaces):
    for rect, difficulty in brick_list:
        pg.draw.rect(screen, GRAY, rect)
        if difficulty > 1:
            text_surface = difficulty_surfaces[difficulty]
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)



def detect_collision_brick(rect, ball):
    cx = ball.x
    cy = ball.y

    closest_x = max(rect.left, min(cx, rect.right))
    closest_y = max(rect.top, min(cy, rect.bottom))

    distance = M.sqrt((cx - closest_x) ** 2 + (cy - closest_y) ** 2)

    return distance <= ball.radius



def handle_ball_rebound(ball, rect):
    if (ball.y > rect.bottom):
        ball.dy = abs(ball.dy)
    elif (ball.y < rect.top):
        ball.dy = -abs(ball.dy)
    else:
        if ball.x <= rect.left:
            ball.dx = -abs(ball.dx) 
        elif ball.x >= rect.right:
            ball.dx = abs(ball.dx)



def brick_collision(ball, brick_list, score, difficulity):
    for rect in brick_list:
        if detect_collision_brick(rect[0], ball):
          handle_ball_rebound(ball, rect[0])
          rect[1] -= 1
          if rect[1] == 0:
            score += difficulity
            brick_list.remove(rect)
    return brick_list, score 



def game_won(screen, pad, ball, screen_width, screen_height):
    ball.dx = 0
    ball.dy = 0
    pad.fart = 0 

    transparent_surface = pg.Surface((screen_width, screen_height-80), pg.SRCALPHA)
    pg.draw.rect(transparent_surface, (10, 10, 10, 200), (0, 0, screen_width, screen_height-80))
    screen.blit(transparent_surface, (0, 80))
    
    text = "YOU WON"
    font = pg.font.SysFont("Arial", 200)
    tekst_surface = font.render(text, True, WHITE)
    text_width, text_height = font.size(text)
    screen.blit(tekst_surface, (screen_width/2 - text_width/2, screen_height/2 - text_height/2))



def check_score(screen, pad, ball, screen_width, screen_height, brick_list, score, difficulity):
    if score == (BLOCKS_PER_ROW * BLOCKS_PER_COL) * difficulity:
        game_won(screen, pad, ball, screen_width, screen_height)
    return score



def update_bricks(screen, pad, ball, screen_width, screen_height, brick_list, score, difficulity):
    brick_list, score = brick_collision(ball, brick_list, score, difficulity)
    difficulty_surfaces = pre_render_difficulty_text(pg.font.SysFont("Arial", 20), BLACK)
    draw_bricks(screen, brick_list, difficulty_surfaces)
    score = check_score(screen, pad, ball, screen_width, screen_height, brick_list, score, difficulity)
    return score