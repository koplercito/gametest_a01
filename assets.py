import pygame as pg
import sys

WIDTH, HEIGHT = 500, 700
RES = WIDTH, HEIGHT
BLACK = 0, 0, 0
pg.init()
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()


running = True

while running:
    #Eventos del juego
    def UpdateEvents():
        pass
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit

    screen.fill(BLACK)

    pg.display.flip()

    clock.tick(60)

pg.quit()