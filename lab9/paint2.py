import pygame
import pygame.freetype

pygame.init()

screen = pygame.display.set_mode((1080, 500))
clock = pygame.time.Clock()

RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE

eraser_img = pygame.image.load('/Users/yeraliyeva/Desktop/eraser.png')
eraser_img = pygame.transform.scale(eraser_img, (70, 70))

def draw_rect(index):
    """Рисуем цветные «кнопки» на верхней полосе."""
    pygame.draw.rect(screen, colors[index], (index * 40, 0, 40, 40))

def pick_color(current_color):
    """Выбираем цвет, если нажали на одну из цветовых кнопок на верхней полосе."""
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return RED
        elif 40 < x <= 80 and 0 <= y <= 40:
            return GREEN
        elif 80 < x <= 120 and 0 <= y <= 40:
            return BLUE
    return current_color

def painting(current_color, current_mode):
    """Функция рисования выбранной фигурой/ластиком."""
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0] and 90 <= y <= 500:
        if current_mode == 'circle':
            pygame.draw.circle(screen, current_color, (x, y), 20,5)
        elif current_mode == 'rect':
            pygame.draw.rect(screen, current_color, (x, y, 40, 40), 4)
        elif current_mode == 'right_triangle':
            pygame.draw.polygon(screen, current_color, ((x, y), (x, y+40), (x+40, y+40)), 3)
        elif current_mode == 'equal_triangle':
            pygame.draw.polygon(screen, current_color, ((x, y), (x+20, y-40), (x+40, y)), 3)
        elif current_mode == 'rhomb':
            pygame.draw.polygon(screen, current_color, ((x, y), (x+20, y-20), (x+40, y), (x+20, y+20)), 3)
        elif current_mode == 'eraser':
            # Ластик: «рисуем» белым (фон)
            pygame.draw.circle(screen, BLACK, (x, y), 20)

# Шрифт для надписей
font_size = 24
font = pygame.freetype.SysFont("Arial", font_size)

def draw_text(text, position, color):
    font.render_to(screen, position, text, color)

draw_text("E: Eraser", (10, 40), BLACK)
mode = 'circle'  # по умолчанию

# Прямоугольник (область) под ластик
eraser_rect = pygame.Rect(1010, 430, 70, 70)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Рисуем три цветные «кнопки»
    for i in range(len(colors)):
        draw_rect(i)

    # Рисуем иконку ластика + «рамку» для наглядности
    pygame.draw.rect(screen, WHITE, eraser_rect, 2)
    screen.blit(eraser_img, (eraser_rect.x, eraser_rect.y))

    # Координаты курсора
    pos = pygame.mouse.get_pos()
    # Если навели мышь на ластик и кликнули - переключаемся в режим 'eraser'
    if eraser_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        mode = 'eraser'

    # Рисуем «кнопки»-фигуры (обведённые контуры), при наведении – меняем режим
    rect_button = pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 3)
    circle_button = pygame.draw.circle(screen, WHITE, (197, 20), 23, 3)
    right_button = pygame.draw.polygon(screen, WHITE, ((230, 0), (230, 40), (270, 40)), 3)
    equal_button = pygame.draw.polygon(screen, WHITE, ((280, 40), (300, 0), (320, 40)), 3)
    rhomb_button = pygame.draw.polygon(screen, WHITE, ((330, 20), (350, 0), (370, 20), (350, 40)), 3)

    if rect_button.collidepoint(pos):
        mode = 'rect'
    if circle_button.collidepoint(pos):
        mode = 'circle'
    if right_button.collidepoint(pos):
        mode = 'right_triangle'
    if equal_button.collidepoint(pos):
        mode = 'equal_triangle'
    if rhomb_button.collidepoint(pos):
        mode = 'rhomb'

    # Обновляем цвет (если кликнули на «цветные кнопки»)
    color = pick_color(color)

    # Рисуем в зависимости от режима
    painting(color, mode)

    clock.tick(60)
    pygame.display.update()
