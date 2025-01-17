import pygame as pg

pause_image = pg.image.load("test/pictures/pause.png").convert_alpha()
pause_image = pg.transform.scale(pause_image, (40, 40))

play_image = pg.image.load("test/pictures/play.png").convert_alpha()
play_image = pg.transform.scale(play_image, (40, 40))

restart_image = pg.image.load("test/pictures/restart.png").convert_alpha()
restart_image = pg.transform.scale(restart_image, (40, 40))

quit_image = pg.image.load("test/pictures/quit.png").convert_alpha()
quit_image = pg.transform.scale(quit_image, (40, 40))

