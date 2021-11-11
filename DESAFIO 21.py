import pygame
pygame.mixer.init() # Inicializando o mixer PyGame
pygame.init() # Iniciando o Pygame
pygame.mixer.music.load('teste.mp3') #carregando a musica (precisa esta na msm pasta) colocar o nome completo
pygame.mixer.music.play() #executa a musica
pygame.event.wait() #espera o evento acabar para encerrar o programa