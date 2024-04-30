#intro to pygame
#boilerplate is useful to set up our environment
#the sprite class cool things in it

#things like java: funct{printin("hello world")} -> the funct thing is boilerplate
# sprite is a two dimensional object. in pygame: has two parts as its representation: an image, a rectangle(hitbox)

#creating a class representing the dvd logo
# -child class of pygame sprites
# -create a constuctor method
# -- image-> visual reprentation
# -- rect(rectange) -> hitbox representation

import pygame
import random
class Dvdlogo(pygame.sprite.Sprite):
    #represent dvd logo sprite
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/dvd-logo.png")

        self.rect= self.image.get_rect()
        # new properity: velocity of the dvd logo
        self.vel_x=random.randrange(3,35)
        self.vel_y=random.randrange(3,35)
        self.rect.centerx = random.randrange(100,1100)
        self.rect.centery = random.randrange(100,620)

    def update(self):
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        #bounce if reach bottom
        if self.rect.bottom > 720:
            self.vel_y *= -1
        elif self.rect.top <0:
            self.vel_y *=-1
        if self.rect.right>1280:
            self.vel_x*=-1
        elif self.rect.left<0:
            self.vel_x*=-1


#boilerplate: below

def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    EMERALD = (21, 219, 147)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)

    WIDTH = 1280  # Pixels
    HEIGHT = 720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("SUPER DUPER UBER LUBER CHIPPI CHAPPA CHOPPY LABA OMEGA FUN DVD LOGO SCREENSAVER BOUNCER CORNER FUN FOR THE FAMILY AND HAPPY AND COOL COOKIE FOREVER")
    
    #create a dvd logo object

    dvdlogo=Dvdlogo()

    #create group of spirite
    all_sprites=pygame.sprite.Group()
    #add dvd logo to group of sprites
    for i in range(1):
        all_sprites.add(Dvdlogo())



    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type==pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    all_sprites.add(Dvdlogo())

        # --- Update the world state
        #update the location of the dvdlogo
        #    dvdlogo.rect.x +dedlogo.vel_ś
        #    dvdlogo.rect.y+dvdlogo.vel_y
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()