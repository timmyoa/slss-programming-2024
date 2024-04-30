import pygame as pg
import random
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

class snowflake(pg.sprite.Sprite):
    def __int__(self,size:int):
        super().__int__()
        self.image = pg.Surface((size,size)) #creating a blank image

        #draw a circle on the "blank image"
        pg.draw.circle(
            self.image,
            WHITE,
            (size//2,size//2),
            size//2)
        self.rect=self.image.get_rect()
        #spawn in center of screen
        self.rect.centerx = WIDTH//2
        self.rect.centery = HEIGHT //2
    # def update(self):
    #     self.rect.y+=self.vel_y
    #     #bounce if reach bottom
    #     if self.rect.top>1280:
    #         self.rect+=1380

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    #add one flake to sprite
    all_sprites.add(snowflake(6))
    pg.display.set_caption("<snowfalls>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state

        # --- Draw items
        # all_sprites.update()
        screen.fill(BLACK) #draw the background

        all_sprites.draw(screen) #draw everything above it
        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()