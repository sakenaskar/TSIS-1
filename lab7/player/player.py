import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("PyGame Player")

playlist = ['player\Brent Faiyaz - Clouded.mp3',
            'player\Brent Faiyaz - Fuck The World (Summer in London).mp3',
            'player\Brent Faiyaz - JACKIE BROWN.mp3',
            'player\Brent Faiyaz - Mercedes.mp3',
            'player\Brent Faiyaz - ROLE MODEL.mp3']

i = 0
j = 0

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                i += 1
                if i == 1:
                    pygame.mixer.music.load(playlist[0])
                    pygame.mixer.music.play()
                elif i % 2 == 0:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                j += 1
                i = 1
                if j < len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
            elif event.key == pygame.K_LEFT:
                j -= 1
                i = 1
                if j > -len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
                