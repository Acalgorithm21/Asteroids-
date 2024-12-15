import pygame 

class Player:
    player_img = pygame.image.load('Foozle_2DS0011_Void_MainShip\Foozle_2DS0011_Void_MainShip\Main Ship\Main Ship - Bases\PNGs\Main Ship - Base - Full health.png')

    def __init__ (self, width, height, color, posx, posy):
        self.width = width
        self.height = height
        self.color = color
        self.posx = posx
        self.posy = posy

    

    def move_up (self):
        velocity = [0.5, 1.5, 3,0]
        for v in velocity:
            self.posy -= v
        
        
    def move_down (self):
        self.posy += 4.2
     
    def move_left (self):
        self.posx -= 4.2

    def move_right (self):
        self.posx += 4.2
