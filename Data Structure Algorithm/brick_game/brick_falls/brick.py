# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:37:19 2021

@author: DELL
"""

import pygame
BLACK = (0,0,0)
 
class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        #
        self.gravity = 0.2
        self.speed_y = 0
        self.pos_y = self.rect.y
    
    def update(self, screen):
        self.speed_y += self.gravity
        self.pos_y += self.speed_y
        self.rect.y += self.speed_y
        print(self.pos_y)
        if self.pos_y > screen.get_height():
            self.kill()  # Remove off-screen circles.