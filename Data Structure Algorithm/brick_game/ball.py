# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:49:42 2021

@author: DELL
"""

import pygame
from random import randint
BLACK = (0,0,0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.circle(self.image, color, (width//2, height//2), 5)
        
        self.velocity = [randint(3,6),randint(-6,6)]
        while(self.velocity[1] == 0):
            self.velocity = [randint(3,6),randint(-6,6)]

        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-6,6)
        while(self.velocity[1] == 0):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-6,6)