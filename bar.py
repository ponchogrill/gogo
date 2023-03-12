import pygame as pg
W = 800
H = 1000
class Bar(pg.sprite.Sprite):
    def __init__(self, filename, screen, x, y):
        self.screen = screen
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load(filename).convert()
        self.image = pg.image.load(img,(600,1000))
        self.rect.x = self.image.get_rect()
        self.rect.y += self.speedy
        def draw(self):
            self.screen.blit(self.image, self.rect)
