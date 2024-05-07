# pygame-exercise-jewelthief.py
# Clone of Jewel Thief Game

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
#load image than scale it
LAWS_IMAGE= pg.image.load("./Images/lawsuite.jpeg")
LAWS_IMAGE=pg.transform.scale(#the method
    LAWS_IMAGE,
    (LAWS_IMAGE.get_width()//1.1, LAWS_IMAGE.get_height()//1.1)
)

class Lawsuite(pg.sprite.Sprite):
    #represent dvd logo sprite
    def __init__(self):
        super().__init__()
        #scale the image to a set size

        self.image = LAWS_IMAGE

        self.rect= self.image.get_rect()
        # new properity: velocity of the dvd logo
        self.vel_x=random.randrange(20,50)
        self.vel_y=random.randrange(20,50)
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


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("./Images/Mario.png")
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2
        self.rect.centery=HEIGHT//2
    def update(self):
        self.rect.centerx=pg.mouse.get_pos()[0]
        self.rect.centery=pg.mouse.get_pos()[1]

class Coins(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("./Images/coin.png")
        self.rect=self.image.get_rect() 
        self.rect.x=random.randrange(0, WIDTH)
        self.rect.y=random.randrange(0, HEIGHT)           
        

def start():
    """Environment Setup and Game Loop"""
    lawt=0
    pg.init()
    pg.mouse.set_visible(False)
    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()
    score=0
    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    coin_sprites = pg.sprite.Group()
    dvd_sprites=pg.sprite.Group()
    player=Player()
    all_sprites.add(player)
    for i in range(1000):
        coin=Coins()
        all_sprites.add(coin)
        coin_sprites.add(coin)
    for i in range(3):
        law=Lawsuite()
        all_sprites.add(law)
        dvd_sprites.add(law)
    pg.display.set_caption("<jewel theif>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)
        law_collided=pg.sprite.spritecollide(player, dvd_sprites, False)
        for coin in  coins_collided:
            score += 1
            print(score)
        for law in law_collided:
            lawt+=1
            print(f"Collison: {lawt}")
        if len(coin_sprites) <= 0:
            for i in range (1000):
                coin= Coins()
                all_sprites.add(coin)
                coin_sprites.add(coin)
            # print(f"COLLISION at {coin.rect.x}, {coin.rect.y}")
        # --- Draw items
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()