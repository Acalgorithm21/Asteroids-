import pygame
from player import Player



###---------------------------game initialization variables------------------------###
pygame.init()

### screen variables 
WIDTH = 700
HEIGHT = 700
### screen display initialization settings 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
title = pygame.display.set_caption("astroid")
clock = pygame.time.Clock()
background = pygame.image.load('SBS - Seamless Space Backgrounds - Large 1024x1024\Large 1024x1024\Green Nebula\Green_Nebula_06-1024x1024.png')

### player initialization settings 
player1 = Player(10, 10 , 'white', WIDTH/2, HEIGHT/2)



### --------------------------------main game loop---------------------------------###
running = True 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scene = screen.blit(background, (0, 0))
    screen.blit(player1.player_img, (player1.posx, player1.posy))
  

    ### on-key press settings 
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass
    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass











    pygame.display.flip()
     

    clock.tick(60)
    
pygame.quit()