"""
Faça um programa que reproduza uma arquivo MP3.
"""
import code

# Inicializando o mixer PyGame
onCommand:sound-in-code.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('python021drive.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()