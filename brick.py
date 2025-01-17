import pygame as pg
from constants import *
from pictures import *
import math as M


def create_bricks(screen_width):
    block_width = screen_width/10
    block_height = 35
    brick_list = []

    for i in range(10):
        for j in range(8):
            x = i * block_width + 5
            y = j * block_height + 80 + 6
            rect = pg.Rect(x, y, block_width - 10, block_height - 6)
            brick_list.append(rect)  

    return brick_list


def draw_bricks(screen, brick_list):
    for rect in brick_list:
        pg.draw.rect(screen, GRAY, rect)


def detect_collision_brick(rect, ball):
    cx = ball.x
    cy = ball.y
    closest_x = max(rect.left, min(cx, rect.right))
    closest_y = max(rect.top, min(cy, rect.bottom))
    distance = M.sqrt((cx - closest_x) ** 2 + (cy - closest_y) ** 2)

    return distance <= ball.radius


def handle_ball_rebound(ball, rect):
    if ((ball.x - ball.radius) <= rect.left) or ((ball.x + ball.radius) >= rect.right):
        ball.dx = -ball.dx

    if ((ball.y - ball.radius) <= rect.bottom) or ((ball.y + ball.radius) >= rect.top):
        ball.dy = -ball.dy


def brick_collision(ball, brick_list):
    for rect in brick_list[:]:
          if detect_collision_brick(rect, ball):
              handle_ball_rebound(ball, rect)
              brick_list.remove(rect)
    return brick_list




def update_bricks(screen, ball, brick_list):
    brick_list = brick_collision(ball, brick_list)
    draw_bricks(screen, brick_list)