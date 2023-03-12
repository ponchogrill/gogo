import random
from random import randint
import pygame as pg
import sys
from car import Car
from grass import Grass
from bar import Bar
def bar_spawn(bar_sprites, i):
    coord = [200, 250, 300, 350] 
    random.shuffle(coord)
    for i in range(3):
        b = Bar(sc, coord[i], 50)
        bar_sprites.append(b)
FPS = 60
W = 800
H = 1000
WHITE = (255, 255, 255)
sc = pg.display.set_mode((W, H))
clock = pg.time.Clock() 
# координата x будет случайна
car = Car(sc)
grass1 = Grass('grass.png', sc, (W - 200) // 2, 0)
grass2 = Grass('grass.png', sc, (W - 200) // 2, - H)
bar_sprites = []
coord = [200, 300, 400, 500] 
for i in range(3):
    random.shuffle(coord)
    b = Bar(sc, coord[i], 50)
    bar_sprites
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    grass1.update()
    grass2.update()
    car.update()
    for i in range(len(bar_sprites)):
        bar_sprites[i].update()
        if bar_sprites[i].rect.y > H:
            bar_sprites1.clear()
            bar_spawn(bar_sprites1, 0)
                      
        
    grass1.draw()
    grass2.draw()
    car.draw()
    pg.display.flip
    clock.tick(FPS)
    pg.display.update()
