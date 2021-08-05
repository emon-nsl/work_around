import pygame
BLACK = (0,0,0)
height =800
width =800
bg = pygame.image.load('images/brick.png')

class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, Color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])
        self.image = pygame.transform.scale(bg,(80,50))
        #self.image.fill(color)
        #self.image.set_colorkey(BLACK)

        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image,BLACK, [-100, 0, width, height])
        

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.flag = 0
        
    def update(self):
        self.rect.x += 0
        if self.flag % 4 ==0:
            self.rect.y += 1
            self.flag=1
        else:
            self.flag += 1
        if self.rect.top > height +10 or self.rect.left < -25 or self.rect.right >width +20 :
            #self.rect.x = random.randrange(width - self.rect.width)
            #self.rect.y = random.randrange(-100,-40)
            #self.speedy = random.randrange(1,8)
            self.kill()