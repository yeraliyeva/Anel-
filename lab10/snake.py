import pygame
import random
import time
import sys
import psycopg2
pygame.init()
sdata=psycopg2.connect(
    dbname="snake_db",
    user="postgres",
    password="12345678",
    host="localhost"
)
sdb=sdata.cursor()
def customer(username):
    sdb.execute("SELECT id FROM users WHERE username=%s", (username,))
    user=sdb.fetchone()#возвращает одну строку результата последнего SQL-запроса.
    if user:
        return user[0]
    else:
        sdb.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        sdata.commit()
        return sdb.fetchone()[0]
def level_current(user_id):
    sdb.execute("SELECT level FROM user_score WHERE user_id=%s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    row=sdb.fetchone()
    return row[0] if row else 0
def score_current(user_id):
    sdb.execute("SELECT score FROM user_score WHERE user_id=%s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    row=sdb.fetchone()
    return row[0] if row else 0
def speed_current(user_id):
    sdb.execute("SELECT speed FROM user_score WHERE user_id=%s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    row=sdb.fetchone()
    return row[0] if row and row[0] is not None else 5
def save_prog(user_id, level, score, speed):
    sdb.execute("INSERT INTO user_score (user_id, level, score, speed) VALUES (%s, %s, %s, %s)", (user_id, level, score, speed))
    sdata.commit()
# устанавливаем размеры экрана
Width = 600
Height = 600
screen = pygame.display.set_mode((Width, Height))  # устанавливаем окно игры с размерами 600x600
def get_username_input():
    input_box = pygame.Rect(Width//2 - 150, Height//2 - 30, 300, 50)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_inactive
    active = True
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if len(text) > 0:
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 20:
                            text += event.unicode

        screen.fill(RED)
        title = font.render("your name", True, WHITE)
        screen.blit(title, (Width//3 - title.get_width()//3, Height//2 - 100))

        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+10))

        pygame.display.flip()
        clock.tick(30)
    return text
# цвета
WHITE = (255, 255, 255)
GRAY = (192,192,192)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
GREEN = (0,255,255)
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
ORANGE = (128,0,128)
CELL = 15  # размер клетки для рисования объектов игры
DARGDRAY = (10, 10, 10)  # тёмный серый цвет
score = 0  # начальный счёт
level = 0  # начальный уровень
speed = 5  # начальная скорость игры
#шрифты
font = pygame.font.Font('/Users/yeraliyeva/Desktop/Luminari.ttf',30)
int_font = pygame.font.Font('/Users/yeraliyeva/Desktop/Luminari.ttf',30)

paused=False
# рисования сетки
def grid():
    for i in range(Height // 2):  #  по вертикали
        for j in range(Width // 2):  # по горизонтали
            pygame.draw.rect(screen, DARGDRAY, (i * CELL, j * CELL, CELL, CELL), 1)  # рисуем сетку
# рисования шахматной сетки
def chess_grid():
    colors = [DARGDRAY, BLACK]  # список цветов
    for i in range(Height // 2):
        for j in range(Width // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))  # чередующиеся цвета
#  отображения текста на экране (счёт и уровень)
def draw_text():
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)  # создаём текст с текущим счётом и уровнем
    screen.blit(score_text, (10, 10))  # отображаем текст в левом верхнем углу
#представляет точку на игровом поле с координатами (x, y)
class Point:
    def __init__(self, x, y):
        self.x = x  # координата X
        self.y = y  # координата Y
    # def __str__(self):
    #     return f"{self.x}, {self.y}"
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # snake's body
        self.dx = 1  # направление движения по оси X
        self.dy = 0  # направление движения по оси Y

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):  # each segment moves to the place of the previous one
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx  # двигаем голову змеи в направлении по X
        self.body[0].y += self.dy  # двигаем голову змеи в направлении по Y

    def draw(self):
        head = self.body[0] #голова
        pygame.draw.rect(screen, RED, (head.x * CELL, head.y * CELL, CELL, CELL), 0, 5)  # head color
        for segment in self.body[1:]:
            pygame.draw.rect(screen, ORANGE, (segment.x * CELL, segment.y * CELL, CELL, CELL), 0, 5)  # body color

    def check_collision(self, food):
        global score, level, speed
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:  # check if snake eats the food
            score += food.points # увеличиваем счёт на количество очков, полученных за еду
            score = max(score, 0) # Add food points to score
            if food.color==RED: # если еда красная, уменьшаем уровень
                if score // 10 < level: # Ensure score doesn't go below 0 # Decrease level based on score
                    level -= 1
                    print(level)
                    screen.fill(RED) # экран красный, когда уровень снижается
                    pygame.draw.rect(screen, BLACK, (Width // 2 - 215, Height // 2 - 45 - 40, 450, 150), 0, 20)
                    pygame.draw.rect(screen, WHITE, (Width // 2 - 190, Height // 2 - 20 - 40, 400, 100), 0, 10)
                    level_down = font.render("LEVEL DOWN!", True, (0, 0, 0)) # налпись о снижении уровня, когда уровень снижается
                    screen.blit(level_down, (Width // 2 - 110, Height // 2 - 30))
                    pygame.display.flip()
                    pygame.time.delay(500) 
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  # increase snake by 1 segment каждое яблоко
            food.update_food(self)  # Update food with new random properties

            if score // 10 > level:  # Если счёт больше уровня, повышаем уровень
                level += 1
                speed += 2  # Увеличиваем скорость игры
                # Green screen flash for 0.5 seconds
                screen.fill(GREEN)
                pygame.draw.rect(screen, BLACK, (Width // 2 - 215, Height // 2 - 45 - 40, 450, 150), 0, 20)
                pygame.draw.rect(screen, WHITE, (Width // 2 - 190, Height // 2 - 20 - 40, 400, 100), 0, 10)  # next level background
                next_level_text = font.render("NEXT LEVEL!", True, (0, 0, 0)) # налпись о повышении уровня, когда уровень повышается
                screen.blit(next_level_text, (Width // 2 - 110, Height // 2 - 30))
                pygame.display.flip()
                pygame.time.delay(500)  # Pause before continuing the game

    def check_wall_collision(self):
        head = self.body[0]
        # Проверяем, не столкнулась ли змея с границами экрана
        return head.x < 0 or head.x >= Width // CELL or head.y < 0 or head.y >= Height // CELL

    def check_self_collision(self):
        head = self.body[0]
        # Проверяем, не столкнулась ли змея с собой
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])



class Food:
    def __init__(self):
        self.pos = Point(0, 0)
        
        self.points, self.color = self.random_food_properties()  # присваиваем случайные баллы и цвет еды
        self.spawn_time = None  # обновляем время появления еды
        self.spawn(None)  # генерируем первую еду
    def random_food_properties(self):
        # генерация случайного цвета и баллов при каждом спавне еды
        food_type = random.choice(["green", "red", "yellow"])
        if food_type == "green":
            return 5, GREEN  # 5 points for green food
        elif food_type == "red":
            return -2, RED  # -2 points for red food
        elif food_type == "yellow":
            return 2, YELLOW  # 2 point for yellow food

    def spawn(self, snake):
        while True:
            new_x = random.randint(0, Width // CELL - 3)
            new_y = random.randint(0, Height // CELL - 3)
            #  чтобы еда не спавнилась в том месте, где уже есть сегменты змеи
            if snake and any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                
                continue
            self.pos = Point(new_x, new_y)
            self.spawn_time = pygame.time.get_ticks() # записываем время появления еды
            break

    def draw(self):
        # Отрисовка еды с текущим цветом
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL), 0, 20)
    
    def update_food(self, snake):
        # вызываться каждый раз, когда змейка съедает еду
        self.points, self.color = self.random_food_properties()  # генерируем новый цвет и баллы для еды
        self.spawn(snake)  # перегенерируем позицию еды
    
        
    # def chwck_expressionself(self):
    #     if pygame.time.get_ticks() - self.spawn_time >5000:
    #         print("serdar")
    #         return True
    #     return False




clock = pygame.time.Clock()
food = Food()
snake = Snake()
# управление направлением
nup=False
ndown=False
nright=True
nleft=False
running = True
username = get_username_input()
user_id = customer(username)
level = level_current(user_id)
score=score_current(user_id)
speed=speed_current(user_id)
def welcome(username, level):
    screen.fill(BLACK)
    msg = font.render(f" {username}!", True, WHITE)
    lvl = font.render(f"current level: {level}", True, WHITE)
    sc=font.render(f"current score: {score}", True, WHITE)
    screen.blit(msg, (Width // 2 - msg.get_width() // 2, Height // 2 - 50))
    screen.blit(lvl, (Width // 2 - lvl.get_width() // 2, Height // 2 + 10))
    screen.blit(sc, (Width // 2 - lvl.get_width() // 2, Height // 2 + 40))
    pygame.display.flip()
    pygame.time.delay(2000)
welcome(username, level)
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False # выход из игры при закрытии окна
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                paused = not paused  # переключаем паузу
                if paused:
                    save_prog(user_id, level, score, speed)
                    print("paused")
            # Обработка нажатий клавиш для управления движением змеи
            if event.key == pygame.K_ESCAPE: # Выход из игры при нажатии ESC
                running=False
            # Проверяем, была ли нажата клавиша стрелка вправо и змея не движется влево
            if event.key == pygame.K_RIGHT and not nleft:
                #  флаг движения вправо , чтобы змея начала двигаться вправо
                nright = True
                #  скорость движения змеи по оси X на 1, чтобы она двигалась вправо
                snake.dx = 1
                #  флаг движения вверх в False, так как змея не будет двигаться вверх
                nup = False
                # флаг движения вниз в False, так как змея не будет двигаться вниз
                ndown = False
                #флаг движения влево в False, так как змея не может двигаться одновременно вправо и влево
                nleft = False
                # скорость движения змеи по оси Y на 0, так как она не будет двигаться по вертикали
                snake.dy = 0
            elif event.key == pygame.K_LEFT and not nright:
                nleft=True
                nup=False
                ndown=False
                nright=False
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and not nup:
                nleft=False
                nup=False
                ndown=True
                nright=False
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and not ndown:
                nleft=False
                nup=True
                ndown=False
                nright=False
                snake.dx = 0
                snake.dy = -1
    if paused:
        screen.fill(BLACK)
        pause_text = font.render("PAUSED", True, WHITE)
 
        screen.blit(pause_text, (Width // 2 - pause_text.get_width() // 2, Height // 2 - 30))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_prog(user_id, level, score, speed)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    paused = False
                    waiting = False
            clock.tick(10)
    # Отображаем шахматную сетку
    chess_grid()
    snake.move()
   
    # Проверка на столкновение с границей или с собой
    if snake.check_wall_collision() or snake.check_self_collision():
        screen.fill(RED) # Экран красный при столкновении
        pygame.draw.rect(screen,BLACK,(Width//2 -215,Height//2-45-40,450,150),0,20)
        pygame.draw.rect(screen,WHITE,(Width//2 -190,Height//2-20-40,400,100),0,10)#fon vyveski you lose
        
        lose_text = font.render("YOU LOSE!", True, (0, 0, 0))#zagruzhaem text
        screen.blit(lose_text, (Width//2 -110, Height//2-30))
        pygame.display.update()
          
        time.sleep(3)
        pygame.quit() 
        save_prog(user_id, level, score, speed)
        print(f" уровень {level}, счёт {score}")
        sys.exit()
    snake.check_collision(food)
    # food.chwck_expressionself()
    # Обновление еды, если она была съедена
    if pygame.time.get_ticks() - food.spawn_time > 5000:  # Если еда на экране более 5 секунд, её обновляем
        food.update_food(snake)

    # Отрисовка
    snake.draw()
    food.draw()
    draw_text()

    # Обновляем экран
    pygame.display.flip()

    # Устанавливаем скорость игры
    clock.tick(speed)

pygame.quit()  # Завершаем игру
sys.exit()
sdata.close()
sdb.close()