import pygame
from random import randint

# Создаем поле с минами
fild = []

for x in range(10):
    xline = []
    for i in range(10):
        a = randint(1, 2)  # Генерация случайного значения для клетки
        if a == 1:
            xline.append(1)  # 1 - это мина
        else:
            xline.append(0)  # 0 - пустая клетка
    fild.append(xline)
    xline = []

for i in range(10):
    print(fild[i])  # Выводим поле в консоль для проверки

pygame.init()

# Класс танка
class Tank():
    def __init__(self, filename, hp, ammo, defence, range, color, x, y, l, h):
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

    def move(self, dx, dy):
        self.box.x += dx
        self.box.y += dy
    # проверка какой это танк
    def writeHP(side):
        fontObj = pygame.font.SysFont()

        if side == "left":
            print()
            # пишем текст слева
        else:
            print()
            # пишем текст справа


# Инициализация окна
mw = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

in_game = True

tank1 = Tank("images/tank1.png", 140, "pod", 60, 40, "gray", 40, 50, 40, 40)
tank2 = Tank("images/tank2.png", 200, "bp", 100, 30, "gray", 750, 550, 40, 40)

# Функция для рисования мин
def draw_mines():
    cell_size = 60  # Размер одной клетки (800/10)
    for row in range(10):
        for col in range(10):
            if fild[row][col] == 1:  # Если мина
                mine_x = col * cell_size
                mine_y = row * cell_size
                pygame.draw.circle(mw, (255, 0, 0), (100 + mine_x + cell_size // 2, mine_y + cell_size // 2), cell_size // 4)

# Проверка на столкновение с миной
def check_mines(tank):
    cell_size = 80
    tank_row = tank.box.y // cell_size
    tank_col = tank.box.x // cell_size
    if fild[tank_row][tank_col] == 1:  # Если танк на мине
        tank.hp -= 10  # Уменьшаем здоровье
        print(f"Tank hit a mine! HP left: {tank.hp}")
        fild[tank_row][tank_col] = 0  # Убираем мину с поля

while in_game:
    mw.fill("gray")

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            in_game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if tank1.box.y > 0:
            tank1.move(0, -2)
    if keys[pygame.K_DOWN]:
        
        if tank1.box.y < 785:
            tank1.move(0, 2)
    if keys[pygame.K_LEFT]:
        if tank1.box.x > 0:
            tank1.move(-2, 0)
    if keys[pygame.K_RIGHT]:
        if tank1.box.x < 780:
            tank1.move(2, 0)

    # Рисуем мины
    draw_mines()

    # Проверяем столкновения танков с минами
    check_mines(tank1)

    # Рисуем танки
    tank1.draw()
    tank2.draw()

    tank1.writeHP("left")
    tank2.writeHP("")
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
