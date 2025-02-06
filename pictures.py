import pygame as pg

pause_image = pg.image.load("pictures/pause.png").convert_alpha()
pause_image = pg.transform.scale(pause_image, (40, 40))

play_image = pg.image.load("pictures/play.png").convert_alpha()
play_image = pg.transform.scale(play_image, (40, 40))

restart_image = pg.image.load("pictures/restart.png").convert_alpha()
restart_image = pg.transform.scale(restart_image, (40, 40))

quit_image = pg.image.load("pictures/quit.png").convert_alpha()
quit_image = pg.transform.scale(quit_image, (40, 40))

full_heart = pg.image.load("pictures/full_heart.png").convert_alpha()
full_heart = pg.transform.scale(full_heart, (40, 40))

empty_heart = pg.image.load("pictures/empty_heart.png").convert_alpha()
empty_heart = pg.transform.scale(empty_heart, (40, 40))

#cracked_heart = pg.image.load("pictures/cracked_heart.png").convert_alpha()
#cracked_heart = pg.transform.scale(cracked_heart, (40, 40))

#shield_heart = pg.image.load("pictures/shield_heart.png").convert_alpha()
#shield_heart = pg.transform.scale(shield_heart, (40, 40))

sort_up = pg.image.load("pictures/sort_up.png").convert_alpha()
sort_up = pg.transform.scale(sort_up, (40, 40))

sort_down = pg.image.load("pictures/sort_down.png").convert_alpha()
sort_down = pg.transform.scale(sort_down, (40, 40))


sort_up_gray = pg.image.load("pictures/sort_up_gray.png").convert_alpha()
sort_up_gray = pg.transform.scale(sort_up_gray, (40, 40))

sort_down_gray = pg.image.load("pictures/sort_down_gray.png").convert_alpha()
sort_down_gray = pg.transform.scale(sort_down_gray, (40, 40))