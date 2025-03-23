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
GAME_OVER_TIME = 2000

# Окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Картинки
background = pygame.image.load('/Users/yeraliyeva/Desktop/AnimatedStreet.png')
player_img = pygame.image.load('/Users/yeraliyeva/Desktop/Player.png')
enemy_img = pygame.image.load('/Users/yeraliyeva/Desktop/Enemy.png')
coin_img = pygame.image.load('/Users/yeraliyeva/Desktop/Coin.png')

# Звуки
pygame.mixer.music.load('/Users/yeraliyeva/Desktop/Lectures_G1_Week10_racer_resources_background.wav')
crash_sound = pygame.mixer.Sound('/Users/yeraliyeva/Desktop/Lectures_G1_Week10_racer_resources_crash.wav')
pygame.mixer.music.play(-1)

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_surf = font.render("Game Over", True, "black")

score = 0

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
        self.reset_position()
    def update(self):
        # Едет вниз
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.reset_position()
    def reset_position(self):
        # Респавн сверху
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

class Coin(pygame.sprite.Sprite):
    # Монетка, которую собираем
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.reset_position()
    def update(self):
        # Тоже вниз
        self.rect.y += COIN_SPEED
        if self.rect.top > HEIGHT:
            self.reset_position()
    def reset_position(self):
        # Случай сверху
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

# Создаём
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)

running = True
game_over = False
game_over_start_time = 0

# Цикл игры
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()
        coin_sprites.update()
        if pygame.sprite.spritecollideany(player, enemy_sprites):
            crash_sound.play()
            game_over = True
            game_over_start_time = pygame.time.get_ticks()
        # Собираем монеты
        coins_collected = pygame.sprite.spritecollide(player, coin_sprites, True)
        if coins_collected:
            score += len(coins_collected)
            new_coin = Coin()
            coin_sprites.add(new_coin)
    else:
        # Ждём пару секунд
        if pygame.time.get_ticks() - game_over_start_time >= GAME_OVER_TIME:
            running = False

    # Фон
    screen.blit(background, (0, 0))
    # Рисуем всё
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    for c in coin_sprites:
        screen.blit(c.image, c.rect)
    # Счёт
    score_text = font_small.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))
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
