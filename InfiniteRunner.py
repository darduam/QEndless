import random
import pygame

pygame.init()

#constantes

white=(255, 255, 255)
black=(0, 0, 0)
green=(0, 255, 0)
purple=(128, 0, 128)
red=(255, 0, 0)
gris=(128, 128, 128)

WIDTH=450
HEIGHT=300

#game variables
score=0
player_x=115
player_y=250
player2_x=115
player2_y=250

screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Infinite QRunner')
background=black
fps=60
font=pygame.font.Font('freesansbold.ttf',16)
timer=pygame.time.Clock()
running=True

while running:
    timer.tick(fps)
    screen.fill(background)
    floor1=pygame.draw.rect(screen,green,[90,0,70,300])
    floor2=pygame.draw.rect(screen,white,[160,0,70,300])
    floor3=pygame.draw.rect(screen,purple,[230,0,70,300])
    floor4=pygame.draw.rect(screen,red,[300,0,70,300])
    player=pygame.draw.rect(screen,black,[player_x, player_y, 20, 20])
    player2=pygame.draw.rect(screen,gris,[player2_x, player2_y, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x=115
                player2_x=115
            if event.key == pygame.K_s:
                player_x=185
                player2_x=185
            if event.key == pygame.K_d:
                player_x=255
                player2_x=255
            if event.key == pygame.K_f:
                player_x=325
                player2_x=325

            if event.key == pygame.K_z:
                player2_x=185
                player_x=115
            if event.key == pygame.K_x:
                player_x=185
                player2_x=255
            if event.key == pygame.K_c:
                player_x=255
                player2_x=325

            if event.key == pygame.K_v:
                player_x=115
                player2_x=255                
            if event.key == pygame.K_b:
                player_x=185
                player2_x=325
            if event.key == pygame.K_n:
                player_x=115
                player2_x=325
                            
    pygame.display.flip()
pygame.quit()
