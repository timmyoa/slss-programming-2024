#pygame-exercise-shootemup.py

import random
import pygame as pg


# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
GREEN = (0, 255, 0)
WIDTH = 720
HEIGHT = 1000
TITLE = "shootemup"
LAWS_IMAGE= pg.image.load("./Images/lawsuite.jpeg")
LAWS_IMAGE=pg.transform.scale(#the method
    LAWS_IMAGE,
    (LAWS_IMAGE.get_width()//2, LAWS_IMAGE.get_height()//2)
)
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("./Images/ship.png")
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.center=pg.mouse.get_pos()
        self.rect.top= HEIGHT-200


class Laser(pg.sprite.Sprite):
    def __init__(self,plaloc: list):
        super().__init__()
        self.image=LAWS_IMAGE
        self.rect=self.image.get_rect()
        self.rect.centerx=plaloc[0]
        self.rect.bottom=plaloc[1]
        self.vel_x=-100
    def update(self):
        self.rect.centery+=self.vel_x
        if self.rect.centery<-20:
            self.kill()

class Mario(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("./Images/Mario.png")
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2
        self.rect.centery=100
        self.y=20
    def update(self):
        self.rect.centerx+=self.y
        if self.rect.centerx>710:
            self.y=random.randrange(-15,-7)
        if self.rect.centerx<10:
            self.y=random.randrange(7,15)



def main():
    pg.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    # Create a snow sprites group
    all_sprites=pg.sprite.Group()
    player=Player()
    all_sprites.add(player)
    mario=Mario()
    all_sprites.add(mario)
    tests=pg.sprite.Group() #lazer

    score=0
    font=pg.font.SysFont("Papyrus",24)



    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                print(f"FINAL SCORE:{score}")
            if event.type == pg.MOUSEBUTTONDOWN:
                tests.add(Laser((player.rect.centerx, player.rect.top)))


        # ----- LOGIC
        all_sprites.update()

        # ----- RENDER
        screen.fill(BLACK)
        tests.update()
        tests.draw(screen)
        # Draw all the sprite groups
        all_sprites.draw(screen)
        score_image=font.render(f"Score: {score}", True, GREEN)
        l_collided=pg.sprite.spritecollide(mario, tests, True)
        for i in l_collided:
            score+=1
        screen.blit(score_image, (5,5))
        # ----- UPDATE DISPLAY
        pg.display.flip()
        clock.tick(60)

    pg.quit()


def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y


if __name__ == "__main__":
    main()