import pygame, random
 
pygame.mixer.music.load('music/Michael_Jackson.mp3')
pygame.mixer.music.play(0)

#sounds=['snd1.mp3', 'snd2.mp3', 'snd3.mp3', 'snd4.mp3', 'snd5.mp3']
#pygame.mixer.music.load('music/'+random.choice(sounds))
#pygame.mixer.music.play()

pygame.mixer.music.set_volume(0.2)

#hit_sound = pygame.mixer.Sound('music/Hit.wav')
#pygame.mixer.Sound.play(hit_sound)
