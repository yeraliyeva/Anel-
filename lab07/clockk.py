import pygame  
import datetime  

pygame.init()  
screen = pygame.display.set_mode((820, 700))  
clock = pygame.time.Clock()  


image = pygame.image.load('/Users/yeraliyeva/Desktop/clock.png')  
image = pygame.transform.scale(image, (600, 600))  
minute_img = pygame.image.load('/Users/yeraliyeva/Desktop/min_hand.png')  
minute_img = pygame.transform.scale(minute_img, (350, 400))  

second_img = pygame.image.load('/Users/yeraliyeva/Desktop/sec_hand.png')  
second_img = pygame.transform.scale(second_img, (400, 400))  

done = False  # Флаг для завершения работы цикла

while not done:  # Главный игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Если окно закрывается
            done = True  # Завершаем цикл

    # Получаем текущее время
    current_time = datetime.datetime.now()
    hour = int(current_time.strftime("%I"))  # Извлекаем текущий час (12-часовой формат)
    minute = int(current_time.strftime("%M"))  # Извлекаем текущую минуту
    second = int(current_time.strftime("%S"))  # Извлекаем текущую секунду

    # Вычисляем углы для поворота стрелок
    hour_angle = (hour % 12 + minute / 60) * 30 * -1  # Угол для часовой стрелки (учитываем минуты)
    minute_angle = minute * 6 * -1 - 10  # Угол для минутной стрелки (минуты умножаем на 6, минус 10 для точности)
    second_angle = second * 6 * -1 - 5  # Угол для секундной стрелки (секунды умножаем на 6, минус 5 для точности)

    # Поворачиваем стрелки
    rotated_minute = pygame.transform.rotate(minute_img, minute_angle)  # Поворачиваем минутную стрелку
    rotated_second = pygame.transform.rotate(second_img, second_angle)  # Поворачиваем секундную стрелку

    screen.fill((255, 255, 255))  # Заполняем экран белым цветом
    screen.blit(image, (100, 100))  # Отображаем циферблат в центре окна
    # Отображаем секундную стрелку (центрируем ее на экране)
    screen.blit(rotated_second, (400 - int(rotated_second.get_width() / 2), 400 - int(rotated_second.get_height() / 2)))
    # Отображаем минутную стрелку (центрируем ее на экране)
    screen.blit(rotated_minute, (400 - int(rotated_minute.get_width() / 2), 400 - int(rotated_minute.get_height() / 2)))
    
    pygame.display.flip()  # Обновляем экран
    clock.tick(60)  # Ограничиваем FPS до 60 кадров в секунду

pygame.quit()  # Завершаем работу pygame
