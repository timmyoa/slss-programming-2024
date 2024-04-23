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

class Dvdlogo(pygame.sprite.Sprite):
    #represent dvd logo sprite
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/dvd-logo.png")

        self.rect= self.image.get_rect()

#boilerplate:

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
    all_sprites.add(dvdlogo)


    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Update the world state

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