import pygame as pg
W = 800
H = 1000
class Car(pg.sprite.Sprite):
    def __init__(self, filename):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        img = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image,(50, 80))
        self.surf = pg.image.load('car.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = W // 2
        self.rect.bottom = H - 10
        self.x = 400
    def update(self, x):
        keys = pg.key.get_pressed()
        #если нажата
        if keys[pg.K_RIGHT]:
            self.rect_x = 10
            self.x += self.rect_x
        #если нажата
        if keys[pg.K_LEFT]:
            self.rect_x = -10
            self.x += self.rect_x
            
        
