from pygame import *

back = (200,255,255)
win_width = 750
win_heigh = 500
mw = display.set_mode((win_width, win_heigh))
mw.fill(back)

class Player():
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 5:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 5:
            self.rect.y += self.speed

clock = time.Clock()
FPS = 40
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False  
        if not finish:
            display.update()
    clock.tick(FPS)

