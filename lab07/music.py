import pygame  

pygame.mixer.init()  
pygame.init()  
sc = pygame.display.set_mode((400, 300), pygame.RESIZABLE)  
pygame.display.set_caption("Music Player")  


music = [
    "/Users/yeraliyeva/Desktop/The Neighbourhood - Compass.mp3",
    "/Users/yeraliyeva/Desktop/Selena Gomes - The Heart Wants What It Wants.mp3",
    "/Users/yeraliyeva/Desktop/The Neighbourhood - Cry Baby.mp3",
    "/Users/yeraliyeva/Desktop/Steve Lacy - Dark Red.mp3",
    "/Users/yeraliyeva/Desktop/Olivia Rodrigo - jealousy jealousy.mp3"
]

# Текущий индекс трека в списке
current_music = 0
pygame.mixer.music.load(music[current_music])  # Загружаем первый трек из списка

pygame.mixer.music.play()  # Воспроизводим первый трек

running = True  # Флаг, чтобы программа продолжала работать
while running:  # Главный игровой цикл
    for event in pygame.event.get():  # Обрабатываем все события
        if event.type == pygame.QUIT:  # Если событие — закрытие окна
            running = False  # Завершаем главный цикл
        elif event.type == pygame.KEYDOWN:  # Если нажата клавиша
            if event.key == pygame.K_SPACE:  # Если нажата клавиша пробела
                if pygame.mixer.music.get_busy():  # Если музыка в данный момент играет
                    pygame.mixer.music.pause()  # Приостанавливаем воспроизведение
                else:
                    pygame.mixer.music.unpause()  # Если музыка на паузе, возобновляем воспроизведение
            elif event.key == pygame.K_RIGHT:  # Если нажата клавиша вправо
                current_music = (current_music + 1) % len(music)  # Переходим к следующему треку
                pygame.mixer.music.load(music[current_music])  # Загружаем новый трек
                pygame.mixer.music.play()  # Воспроизводим его
            elif event.key == pygame.K_LEFT:  # Если нажата клавиша влево
                current_music = (current_music - 1) % len(music)  # Переходим к предыдущему треку
                pygame.mixer.music.load(music[current_music])  # Загружаем новый трек
                pygame.mixer.music.play()  # Воспроизводим его

    pygame.display.flip()  # Обновляем экран

pygame.quit()  # Закрываем pygame, когда окно закрыто
