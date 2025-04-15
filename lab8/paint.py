import pygame  

pygame.init()  

screen = pygame.display.set_mode((800, 600))  
clock = pygame.time.Clock()  


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen.fill(WHITE)  
pygame.display.flip() 
colors = [RED, GREEN, BLUE]  
color = BLACK  
# Загружаем изображение для ластика и изменяем его размер
eraser = pygame.image.load('/Users/yeraliyeva/Desktop/eraser.png')  # Загружаем изображение ластика
eraser = pygame.transform.scale(eraser, (70, 70))  # Масштабируем изображение
eraser_rect = eraser.get_rect(topleft=(1010, 0))  # Определяем область для ластика (прямоугольник)

# Функция для рисования прямоугольников с выбором цвета
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))  # Рисуем прямоугольники для выбора цвета

# Функция для определения выбранного цвета
def pick_color():
    click = pygame.mouse.get_pressed()  # Получаем информацию о нажатых клавишах мыши
    x, y = pygame.mouse.get_pos()  # Получаем текущую позицию мыши
    if click[0]:  # Если нажата левая кнопка мыши
        if 0 <= x <= 40 and 0 <= y <= 40:  # Если клик в области первого прямоугольника
            return RED  # Возвращаем красный цвет
        elif 40 < x <= 80 and 0 <= y <= 40:  # Если клик в области второго прямоугольника
            return GREEN  # Возвращаем зеленый цвет
        elif 80 < x <= 120 and 0 <= y <= 40:  # Если клик в области третьего прямоугольника
            return BLUE  # Возвращаем синий цвет
        elif 1010 <= x <= 1080 and 0 <= y <= 40:  # Если клик в области ластика
            return BLACK  # Возвращаем черный цвет
    return color  # Если не было клика, возвращаем текущий цвет

# Функция для рисования на экране
def painting(color, mode):
    click = pygame.mouse.get_pressed()  # Получаем информацию о нажатых клавишах мыши
    x, y = pygame.mouse.get_pos()  # Получаем текущую позицию мыши
    if click[0] and not (0 <= x <= 400 and 0 <= y <= 90):  # Если нажата левая кнопка и не в области выбора цвета
        if mode == 'circle':  # Если выбран режим рисования круга
            pygame.draw.circle(screen, color, (x, y), 27, 4)  # Рисуем круг
        elif mode == 'rect':  # Если выбран режим рисования прямоугольника
            pygame.draw.rect(screen, color, (x, y, 40, 40), 4)  # Рисуем прямоугольник
        elif mode == 'equal_triangle':  # Если выбран режим рисования равностороннего треугольника
            pygame.draw.polygon(screen, color, ((x, y), (x+20, y-40), (x+40, y)))  # Рисуем треугольник
        elif mode == 'eraser':  # Если выбран режим ластика
            pygame.draw.circle(screen, WHITE, (x, y), 20)  # Стираем часть с белым цветом (ластик)

mode = 'circle'  # Начальный режим - рисование круга

# Определяем шрифт для отображения текста
font_size = 24
font = pygame.freetype.SysFont("Arial", font_size)

# Функция для рисования текста на экране
def draw_text(text, position, color):
    font.render_to(screen, position, text, color)  # Отображаем текст на экране
    
draw_text("E: Eraser", (10, 40), BLACK)  # Рисуем текст "E: Eraser" на экране

while True:  # Главный игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Если окно закрывается
            pygame.quit()  # Завершаем программу
        elif event.type == pygame.KEYDOWN:  # Если нажата клавиша
            if event.key == pygame.K_e:  # Если нажата клавиша 'E'
                mode = 'eraser'  # Меняем режим на ластик

    # Рисуем прямоугольники для выбора цветов
    for i in range(len(colors)):
        draw_rect(i)  # Рисуем прямоугольники для каждого цвета

    screen.blit(eraser, (1010, 0))  # Отображаем изображение ластика

    # Создаем области для различных режимов рисования
    rect = pygame.draw.rect(screen, (0, 0, 0), (130, 0, 40, 40), 3)  # Прямоугольник
    circle = pygame.draw.circle(screen, (0, 0, 0), (197, 20), 23, 3)  # Круг
    equal = pygame.draw.polygon(screen, (0, 0, 0), ((230, 0), (230, 40), (270, 40)), 3)  # Равносторонний треугольник

    pos = pygame.mouse.get_pos()  # Получаем текущую позицию мыши
    if rect.collidepoint(pos):  # Если мышь в области прямоугольника
        mode = "rect"  # Меняем режим на рисование прямоугольника
    if circle.collidepoint(pos):  # Если мышь в области круга
        mode = "circle"  # Меняем режим на рисование круга
    if equal.collidepoint(pos):  # Если мышь в области треугольника
        mode = 'equal_triangle'  # Меняем режим на рисование треугольника
    if eraser_rect.collidepoint(pos):  # Если мышь в области ластика
        mode = 'eraser'  # Меняем режим на ластик

    color = pick_color()  # Выбираем текущий цвет
    painting(color, mode)  # Рисуем с выбранным цветом и в выбранном режиме

    clock.tick(370)  # Ограничиваем FPS до 370 кадров в секунду
    pygame.display.update()  # Обновляем экран
