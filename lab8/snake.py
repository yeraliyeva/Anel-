import pygame
import random

pygame.init()


WIDTH = 600
HEIGHT = 600
CELL_SIZE = 30

# Стартовые параметры игры
INITIAL_FPS = 5          # базовая скорость игры (кадров в секунду)
FOOD_PER_LEVEL = 4       # каждые 4 съеденных яблока - новый уровень
LEVEL_SPEED_INCREMENT = 2 # при повышении уровня увеличиваем FPS на 2

# Цвета (RGB)
WHITE  = (255, 255, 255)
GRAY   = (200, 200, 200)
GREEN  = (0, 255, 0)
RED    = (255, 0, 0)
YELLOW = (255,255,0)
BLACK  = (0, 0, 0)
PINK  = (255,153,204)


# Создаём окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Levels")

# Шрифты для отображения текста
font_small = pygame.font.SysFont("Verdana", 20)
font_big   = pygame.font.SysFont("Verdana", 50)

# Часы для контроля FPS
clock = pygame.time.Clock()

# Функция для рисования «шахматного» фона
def draw_grid():
    colors = [PINK, WHITE]
    rows = HEIGHT // CELL_SIZE
    cols = WIDTH // CELL_SIZE
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            # (row + col) % 2 даёт чередование цветов
            pygame.draw.rect(screen, colors[(row + col) % 2], rect)

# Класс для хранения координат (x, y) в клетках (а не в пикселях)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс еды (яблока)
class Food:
    def __init__(self):
        self.pos = Point(9, 9)  # начальное положение

    def draw(self):
        # Рисуем зелёный квадрат в позиции еды
        pygame.draw.rect(screen, GREEN,
                         (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def respawn(self, snake_body):
        # Случайно выбираем координаты до тех пор, пока не найдём пустую клетку
        max_x = (WIDTH // CELL_SIZE) - 1
        max_y = (HEIGHT // CELL_SIZE) - 1

        while True:
            new_x = random.randint(0, max_x)
            new_y = random.randint(0, max_y)
            # Проверяем, что новая позиция не находится в теле змейки
            conflict = False
            for segment in snake_body:
                if segment.x == new_x and segment.y == new_y:
                    conflict = True
                    break
            if not conflict:
                self.pos.x = new_x
                self.pos.y = new_y
                break

# Класс змейки
class Snake:
    def __init__(self):
        # Три звена по умолчанию, выстроенные по вертикали
        self.body = [Point(10, 10), Point(10, 11), Point(10, 12)]
        # Движемся изначально вверх (dx=0, dy=-1)
        self.dx = 0
        self.dy = -1

    def move(self):
        # Двигаем хвост вперёд: начиная с конца, копируем координаты предыдущего сегмента
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Двигаем голову в направлении dx, dy
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        # Голова красная
        head = self.body[0]
        pygame.draw.rect(screen, RED,
                         (head.x * CELL_SIZE, head.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        # Остальное тело - жёлтое
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW,
                             (segment.x * CELL_SIZE, segment.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def check_wall_collision(self):
        # Если голова вышла за границы, возвращаем True
        head = self.body[0]
        if head.x < 0 or head.x >= (WIDTH // CELL_SIZE):
            return True
        if head.y < 0 or head.y >= (HEIGHT // CELL_SIZE):
            return True
        return False

    def check_self_collision(self):
        # Проверяем, не врезалась ли голова в одно из звеньев
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def check_food_collision(self, food):
        # Если координаты головы и еды совпали
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            return True
        return False

    def grow(self):
        # При росте добавляем новый сегмент в конец
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))

# Инициализируем объекты
snake = Snake()
food = Food()

# Счётчики
score = 0
level = 1
current_fps = INITIAL_FPS

# Основной игровой цикл
running = True
while running:
    clock.tick(current_fps)

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Меняем направление змейки, если нажаты стрелки
            if event.key == pygame.K_UP and snake.dy != 1:    # не двигаемся вниз
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0

    # Двигаем змейку
    snake.move()

    # Проверяем столкновение со стеной или с собой
    if snake.check_wall_collision() or snake.check_self_collision():
        running = False

    # Проверяем, не съела ли змейка яблоко
    if snake.check_food_collision(food):
        score += 1            # увеличиваем счёт
        snake.grow()          # увеличиваем длину змейки
        food.respawn(snake.body)  # ставим еду в новое место, не занятое змейкой

        # Проверяем, не пора ли перейти на новый уровень
        if score % FOOD_PER_LEVEL == 0:
            level += 1
            current_fps += LEVEL_SPEED_INCREMENT

    # Рисуем фон, змейку и еду
    draw_grid()
    snake.draw()
    food.draw()

    # Выводим счёт и уровень в левом верхнем углу
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    level_text = font_small.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()


pygame.quit()
