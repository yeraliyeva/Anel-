import pygame
import random

pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 400, 600
FPS = 60

# Скорость и время
PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 7

# Окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Racer")

# Картинки
background = pygame.image.load('/Users/yeraliyeva/Desktop/AnimatedStreet.png')
player_img = pygame.image.load('/Users/yeraliyeva/Desktop/Player.png')
enemy_img = pygame.image.load('/Users/yeraliyeva/Desktop/Enemy.png')
coin_img = pygame.image.load('/Users/yeraliyeva/Desktop/Coin.png')

# Фоны для монет
red_coin_img = pygame.image.load('/Users/yeraliyeva/Desktop/red.png')  # Красная монета с фоном
pink_coin_img = pygame.image.load('/Users/yeraliyeva/Desktop/pink.png')  # Розовая монета с фоном
minus_coin_img = pygame.image.load('/Users/yeraliyeva/Desktop/red.png')  # Минус монета (для штрафов)

# Изменяем размер монет на 100x100 пикселей
red_coin_img = pygame.transform.scale(red_coin_img, (100, 100))  # Красная монета с фоном
pink_coin_img = pygame.transform.scale(pink_coin_img, (100, 100))  # Розовая монета с фоном
minus_coin_img = pygame.transform.scale(minus_coin_img, (100, 100))  # Минус монета (для штрафов)

# Звуки
pygame.mixer.music.load('/Users/yeraliyeva/Desktop/Lectures_G1_Week10_racer_resources_background.wav')
crash_sound = pygame.mixer.Sound('/Users/yeraliyeva/Desktop/Lectures_G1_Week10_racer_resources_crash.wav')
pygame.mixer.music.play(-1)

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
coin_font = pygame.font.SysFont("Verdana", 18)  # Шрифт для отображения веса монеты
game_over_surf = font.render("Game Over", True, "black")

score = 0
total_coins = 0  # Общее количество собранных монет
level = 1  # Начальный уровень

class Player(pygame.sprite.Sprite):
    # Игрок, чтобы ездить
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
    def update(self):
        # Движение
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    # Враг, чтоб мешать
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
    def update(self):
        # Едет вниз
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = -self.rect.height

class Coin(pygame.sprite.Sprite):
    # Монетка, которую собираем
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.score = 0
        # Генерируем случайный вес для монеты
        self.gen_coin()

    def set_coin_image(self):
        self.split_or_double = random.choice(["normal", "minus", "pink"])
        self.weight = 0
        if self.split_or_double == "normal":
            self.weight = random.randint(0, 50)
            self.image = coin_img
        elif self.split_or_double == "pink":
            # Розовая монета для удвоения счета
            self.image = pink_coin_img
        elif self.split_or_double == "minus":
            self.weight = random.randint(-50, 0)
            # Минус монета для штрафа
            self.image = minus_coin_img

    def gen_coin(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0
        self.set_coin_image()

    def move(self):
        # Тоже вниз
        self.rect.move_ip(0, COIN_SPEED)
        print(self.rect.top)
        if self.rect.top > HEIGHT:
            self.gen_coin()
        elif self.rect.colliderect(player.rect):
            if self.split_or_double == "normal" or self.split_or_double == "minus":
                self.score += self.weight
            elif self.split_or_double == "pink":
                self.score *= 2
            self.gen_coin()
        else:
            screen.blit(self.image, self.rect)
            self.draw_weight()


    def draw_weight(self):
        # Отображаем текст "2x" для розовой монеты
        if self.split_or_double == "pink":
            weight_text = coin_font.render("2x", True, "black")
            screen.blit(weight_text, (self.rect.x + self.rect.width // 2 - weight_text.get_width() // 2, self.rect.y - 20))
        else:
            weight_text = coin_font.render(f"{self.weight}", True, "black")
            screen.blit(weight_text, (self.rect.x + self.rect.width // 2 - weight_text.get_width() // 2, self.rect.y - 20))


# Создаём
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy)
enemy_sprites = pygame.sprite.Group(enemy)


running = True
game_over = False
game_over_start_time = 0

# Функция для обновления уровня
def update_level():
    global level, ENEMY_SPEED, COIN_SPEED
    if coin.score >= 300 and level == 1:  # Достигнут 300 монет, уровень 2
        level = 2
        ENEMY_SPEED = 12  # Увеличиваем скорость врагов
        COIN_SPEED = 9   # Увеличиваем скорость монет
    if coin.score >= 500 and level == 2:  # Достигнут 500 монет, уровень 3
        level = 3
        ENEMY_SPEED = 14  # Увеличиваем скорость врагов
        COIN_SPEED = 11   # Увеличиваем скорость монет

# Ограничиваем количество монет на экране
MAX_COINS = 2

# Цикл игры
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()
        if pygame.sprite.spritecollideany(player, enemy_sprites):
            crash_sound.play()
            game_over = True
            game_over_start_time = pygame.time.get_ticks()
    screen.blit(background, (0, 0))  
    coin.move()
    update_level()

    # Фон
    
    # Рисуем всё
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    # Счёт
    score_text = font_small.render(f"Score: {coin.score}", True, "black")
    screen.blit(score_text, (10, 10))
    # Уровень
    level_text = font_small.render(f"Level: {level}", True, "black")
    screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))
    # Если конец
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill("red")
        overlay.set_alpha(128)
        screen.blit(overlay, (0, 0))
        r = game_over_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(game_over_surf, r)

    pygame.display.flip()

pygame.quit()
