import pygame
from random import randint

xline = []
fild = []

for x in range (10):

    for i in range (10):
        a = randint(1, 2)
        if a == 1:
            xline.append(1)
        else:
            xline.append(0)
    fild.append(xline)
    xline = []

for i in range (10):
    print(fild[i])


pygame.init()
class Tank():
    def __init__(self, filename , hp, ammo, defence, range, color, x, y, l, h):
        self.hp = hp
        self.ammo = ammo
        self.defence = defence
        self.range = range
        self.color = color
        self.box = pygame.Rect(x, y, l, h)
        self.picture = pygame.image.load(filename)
    def fill(self):
        pygame.draw.rect(mw, self.color, self.box)
    def draw(self):
        mw.blit(self.picture, (self.box.x, self.box.y))


mw = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

in_game = True

tank1 = Tank("images/tank1.png", 140, "pod", 60, 40, "gray", 40, 50, 20, 20)
Tank2 = Tank("images/Tank2.png",200, "bp", 100, 30, "gray", 750, 750, 25, 25)
# tank3 = Tank(160, "he", 70, 20, "gray", 400, 400, 20, 20)


while in_game:
    mw.fill("gray")

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            in_game = False 

    tank1.draw()
    Tank2.draw()




    pygame.display.update()
    clock.tick(90)




