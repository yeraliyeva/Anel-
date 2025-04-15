import pygame  
import random  
import time 

pygame.init() 


WIDTH = 600
HEIGHT = 600
CELL_SIZE = 30

# Стартовые параметры игры
INITIAL_FPS = 5  # Начальная скорость игры (кадры в секунду)
FOOD_PER_LEVEL = 4  # Количество еды для повышения уровня
LEVEL_SPEED_INCREMENT = 2  # Увеличение скорости игры при повышении уровня

# Цвета (RGB)
WHITE  = (255, 255, 255)
GRAY   = (200, 200, 200)
GREEN  = (0, 255, 0)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK  = (0, 0, 0)
PINK   = (255, 153, 204)
BLUE   = (0, 0, 255)
ORANGE = (255, 165, 0)

# Окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем окно с размерами 600x600
pygame.display.set_caption("Snake with Levels")  # Устанавливаем заголовок окна

# Шрифты для отображения текста
font_small = pygame.font.SysFont("Verdana", 20)  # Маленький шрифт
font_big = pygame.font.SysFont("Verdana", 50)  # Большой шрифт

# Таймер для управления FPS
clock = pygame.time.Clock()

# Функция для рисования сетки
def draw_grid():
    colors = [PINK, WHITE]  # Цвета клеток
    rows = HEIGHT // CELL_SIZE  # Количество строк
    cols = WIDTH // CELL_SIZE  # Количество столбцов
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, colors[(row + col) % 2], rect)  # Рисуем клетки с чередующимися цветами

# Класс для представления точки (координаты)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс для еды
class Food:
    def __init__(self):
        self.respawn([])  # Инициализация еды (сразу появляется на экране)

    def draw(self):
        # Рисуем еду
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def respawn(self, snake_body):
        # Перезапускаем еду в случайном месте, избегая пересечений с телом змеи
        max_x = (WIDTH // CELL_SIZE) - 1
        max_y = (HEIGHT // CELL_SIZE) - 1

        while True:
            new_x = random.randint(0, max_x)  # Случайная позиция по X
            new_y = random.randint(0, max_y)  # Случайная позиция по Y
            conflict = any(segment.x == new_x and segment.y == new_y for segment in snake_body)
            if not conflict:
                self.pos = Point(new_x, new_y)  # Если еда не на теле змеи, создаем новую позицию
                self.spawn_time = time.time()  # Время появления еды
                self.weight, self.color = random.choice([
                    (1, GREEN),  # Еда весом 1 (зеленая)
                    (2, BLUE),   # Еда весом 2 (синяя)
                    (3, ORANGE)  # Еда весом 3 (оранжевая)
                ])
                break

    def is_expired(self, duration=5):
        # Проверка, истекло ли время для еды
        return time.time() - self.spawn_time > duration

# Класс для змеи
class Snake:
    def __init__(self):
        # Инициализация змеи
        self.body = [Point(10, 10), Point(10, 11), Point(10, 12)]  # Начальная позиция змеи
        self.dx = 0  # Направление по оси X
        self.dy = -1  # Направление по оси Y (вверх)

    def move(self):
        # Двигаем змею
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx  # Перемещаем голову
        self.body[0].y += self.dy  # Перемещаем голову

    def draw(self):
        # Рисуем змею
        head = self.body[0]  # Голова змеи
        pygame.draw.rect(screen, RED, (head.x * CELL_SIZE, head.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Голова
        for segment in self.body[1:]:  # Тело змеи
            pygame.draw.rect(screen, YELLOW, (segment.x * CELL_SIZE, segment.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def check_wall_collision(self):
        # Проверка столкновения с границами экрана
        head = self.body[0]
        return head.x < 0 or head.x >= (WIDTH // CELL_SIZE) or head.y < 0 or head.y >= (HEIGHT // CELL_SIZE)

    def check_self_collision(self):
        # Проверка столкновения с телом змеи
        head = self.body[0]
        return any(head.x == segment.x and head.y == segment.y for segment in self.body[1:])

    def check_food_collision(self, food):
        # Проверка столкновения с едой
        head = self.body[0]
        return head.x == food.pos.x and head.y == food.pos.y

    def grow(self, amount=1):
        # Увеличение размера змеи
        tail = self.body[-1]
        for _ in range(amount):
            self.body.append(Point(tail.x, tail.y))  # Добавляем новый сегмент в хвост

# Инициализация объектов
snake = Snake()
food = Food()

# Начальные параметры игры
score = 0
level = 1
current_fps = INITIAL_FPS

# Главный игровой цикл
running = True
while running:
    clock.tick(current_fps)  # Ограничиваем FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Завершаем игру, если закрыли окно
        elif event.type == pygame.KEYDOWN:
            # Управление змейкой с помощью клавиш
            if event.key == pygame.K_UP and snake.dy != 1:
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

    snake.move()  # Двигаем змею

    # Проверка на столкновение с границей или телом змеи
    if snake.check_wall_collision() or snake.check_self_collision():
        running = False  # Если есть столкновение, завершаем игру

    # Проверка на истекшее время еды
    if food.is_expired():
        food.respawn(snake.body)  # Перезапускаем еду

    # Проверка на съеденную еду
    if snake.check_food_collision(food):
        score += food.weight  # Увеличиваем счет за съеденную еду
        snake.grow(food.weight)  # Увеличиваем змею
        food.respawn(snake.body)  # Перезапускаем еду

        # Повышаем уровень, если собрали достаточно еды
        if score // FOOD_PER_LEVEL + 1 > level:
            level += 1
            current_fps += LEVEL_SPEED_INCREMENT  # Увеличиваем скорость игры

    draw_grid()  # Рисуем сетку
    snake.draw()  # Рисуем змею
    food.draw()  # Рисуем еду

    # Отображение счета и уровня на экране
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    level_text = font_small.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()  # Обновление экрана

pygame.quit()  # Закрытие игры
