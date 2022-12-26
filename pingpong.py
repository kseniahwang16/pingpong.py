from pygame import *

back = (200,255,255)
win_width = 750
win_heigh = 500
mw = display.set_mode((win_width, win_heigh))
mw.fill(back)

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
