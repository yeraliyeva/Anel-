import pygame 

pygame.mixer.init()
pygame.init()
sc = pygame.display.set_mode((400,300), pygame.RESIZABLE)

pygame.display.set_caption("Music Player")


music = [
    "/Users/yeraliyeva/Desktop/The Neighbourhood - Compass.mp3",
    "/Users/yeraliyeva/Desktop/Selena Gomes - The Heart Wants What It Wants.mp3",
    "/Users/yeraliyeva/Desktop/The Neighbourhood - Cry Baby.mp3",
    "/Users/yeraliyeva/Desktop/Steve Lacy - Dark Red.mp3",
    "/Users/yeraliyeva/Desktop/Olivia Rodrigo - jealousy jealousy.mp3"
]


# music = ["Olivia Rodrigo - jealousy jealousy.mp3","Selena Gomes - The Heart Wants What It Wants.mp3","The Neighbourhood - Cry Baby.mp3", "The Neighbourhood - Compass.mp3"]

current_music = 0
pygame.mixer.music.load(music[current_music])

pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()


   
    pygame.display.flip()


pygame.quit()