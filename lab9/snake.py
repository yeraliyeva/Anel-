import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 30

# Стартовые параметры игры
INITIAL_FPS = 5
FOOD_PER_LEVEL = 4
LEVEL_SPEED_INCREMENT = 2

# Цвета (RGB)
WHITE  = (255, 255, 255)
GRAY   = (200, 200, 200)
GREEN  = (0, 255, 0)
RED    = (255, 0, 0)
YELLOW = (255,255,0)
BLACK  = (0, 0, 0)
PINK   = (255,153,204)
BLUE   = (0, 0, 255)
ORANGE = (255,165,0)

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Levels")

font_small = pygame.font.SysFont("Verdana", 20)
font_big   = pygame.font.SysFont("Verdana", 50)

clock = pygame.time.Clock()

def draw_grid():
    colors = [PINK, WHITE]
    rows = HEIGHT // CELL_SIZE
    cols = WIDTH // CELL_SIZE
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, colors[(row + col) % 2], rect)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Food:
    def __init__(self):
        self.respawn([])

    def draw(self):
        pygame.draw.rect(screen, self.color,
                         (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def respawn(self, snake_body):
        max_x = (WIDTH // CELL_SIZE) - 1
        max_y = (HEIGHT // CELL_SIZE) - 1

        while True:
            new_x = random.randint(0, max_x)
            new_y = random.randint(0, max_y)
            conflict = any(segment.x == new_x and segment.y == new_y for segment in snake_body)
            if not conflict:
                self.pos = Point(new_x, new_y)
                self.spawn_time = time.time()
                self.weight, self.color = random.choice([
                    (1, GREEN),
                    (2, BLUE),
                    (3, ORANGE)
                ])
                break

    def is_expired(self, duration=5):
        return time.time() - self.spawn_time > duration

class Snake:
    def __init__(self):
        self.body = [Point(10, 10), Point(10, 11), Point(10, 12)]
        self.dx = 0
        self.dy = -1

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, RED,
                         (head.x * CELL_SIZE, head.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW,
                             (segment.x * CELL_SIZE, segment.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= (WIDTH // CELL_SIZE) or head.y < 0 or head.y >= (HEIGHT // CELL_SIZE)

    def check_self_collision(self):
        head = self.body[0]
        return any(head.x == segment.x and head.y == segment.y for segment in self.body[1:])

    def check_food_collision(self, food):
        head = self.body[0]
        return head.x == food.pos.x and head.y == food.pos.y

    def grow(self, amount=1):
        tail = self.body[-1]
        for _ in range(amount):
            self.body.append(Point(tail.x, tail.y))

snake = Snake()
food = Food()

score = 0
level = 1
current_fps = INITIAL_FPS

running = True
while running:
    clock.tick(current_fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
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

    snake.move()

    if snake.check_wall_collision() or snake.check_self_collision():
        running = False

    if food.is_expired():
        food.respawn(snake.body)

    if snake.check_food_collision(food):
        score += food.weight
        snake.grow(food.weight)
        food.respawn(snake.body)

        if score // FOOD_PER_LEVEL + 1 > level:
            level += 1
            current_fps += LEVEL_SPEED_INCREMENT

    draw_grid()
    snake.draw()
    food.draw()

    score_text = font_small.render(f"Score: {score}", True, BLACK)
    level_text = font_small.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()

pygame.quit()
