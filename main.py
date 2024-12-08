import pygame

pygame.init()
class Tank():
    def __init__(self, hp, ammo, defence, range, color, x, y, l, h):
        self.hp = hp
        self.ammo = ammo
        self.defence = defence
        self.range = range
        self.color = color
        self.box = pygame.Rect(x, y, l, h)
    def fill(self):
        pygame.draw.rect(mw, self.color, self.box)

mw = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

in_game = True

tank1 = Tank(140, "pod", 60, 40, "gray", 40, 50, 20, 20)
tank2 = Tank(200, "bp", 100, 30, "gray", 750, 750, 25, 25)
tank3 = Tank(160, "he", 70, 20, "gray", 400, 400, 20, 20)


while in_game:
    mw.fill("gray")

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            in_game = False 




    pygame.display.update()
    clock.tick(90)




