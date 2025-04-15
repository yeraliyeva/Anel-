import pygame
pygame.init()

W, H = 600, 400  
WHITE = (255, 255, 255)  
RED = (255, 0, 0) 
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE) 

clock = pygame.time.Clock()  
FPS = 60  # Частота обновления экрана (60 кадров в секунду)

x = W // 2  # Начальная позиция по оси X (в центре)
y = H // 2  # Начальная позиция по оси Y (в центре)
speed = 5  # Скорость движения
circle_radius = 25  # Радиус круга

flUp = flDown = flLeft = flRight = False  # Флаги для направления движения

while True:
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Если закрытие окна
            exit()  # Завершаем программу
        elif event.type == pygame.KEYDOWN:  # Если клавиша нажата
            if event.key == pygame.K_LEFT:  # Если нажата клавиша "влево"
                flLeft = True  # Устанавливаем флаг для движения влево
            elif event.key == pygame.K_RIGHT:  # Если нажата клавиша "вправо"
                flRight = True  # Устанавливаем флаг для движения вправо
            elif event.key == pygame.K_UP:  # Если нажата клавиша "вверх"
                flUp = True  # Устанавливаем флаг для движения вверх
            elif event.key == pygame.K_DOWN:  # Если нажата клавиша "вниз"
                flDown = True  # Устанавливаем флаг для движения вниз
        elif event.type == pygame.KEYUP:  # Если клавиша отпущена
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:  # Для всех стрелок
                flUp = flDown = flLeft = flRight = False  # Сбрасываем все флаги

        elif event.type == pygame.VIDEORESIZE:  # Если окно изменило размер
            W, H = event.size  # Обновляем размеры окна
            x = W // 2  # Центрируем круг по X
            y = H // 2  # Центрируем круг по Y
            sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)  # Обновляем окно

    # Движение по горизонтали
    if flLeft and x > 25:  # Если флаг движения влево и шарик не выходит за левую границу
        x -= speed  # Двигаем шарик влево
    elif flRight and x < W:  # Если флаг движения вправо и шарик не выходит за правую границу
        x += speed  # Двигаем шарик вправо

    # Движение по вертикали
    if flUp and y > 25:  # Если флаг движения вверх и шарик не выходит за верхнюю границу
        y -= speed  # Двигаем шарик вверх
    elif flDown and y < H:  # Если флаг движения вниз и шарик не выходит за нижнюю границу
        y += speed  # Двигаем шарик вниз

    sc.fill(WHITE)  # Заполняем экран белым цветом
    pygame.draw.circle(sc, RED, (x, y), circle_radius)  # Рисуем круг на новом месте
    pygame.display.update()  # Обновляем экран

    clock.tick(FPS)  # Задержка для ограничения FPS (60 кадров в секунду)
