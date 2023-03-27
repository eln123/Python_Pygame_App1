import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
# they are capitalized because
# of convention, we are communicating
# that we don't want them to change

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

#now that we have the window, width and height,
# we need to set up the main game loop
# whenever you are working in pygame, you need
# a loop. typically a while loop that runs while the game runs to keep it going
# the loop does things like: 
# check for collisions
# check for movements
# check for key presses (e.g. hitting X on the window)
# then adjust what's being displayed on the screen

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
# this scales our image to be the width and height

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0, 0))

    # WIN is the variable for window, as defined above
    # blit is a function when you want to draw an image
    # or a surface (the Python term is surface) on the screen
    # so we are going to blit the background image
    # then pass the coordinates of the top left hand corner of this image
    # in PYGAME, (0, 0) is the top left hand corner of the screen
    # (0, WIDTH) is top right
    # (HEIGHT, 0) is bottom left
    # (HEIGHT, WIDTH) is bottom right
    # we want the background image to fill the entire screen
    # so we are going to put (0, 0) as the coordinates of where the top left hand corner of this background
    # image should be placed
    # then width and height will fill the screen
  

    pygame.draw.rect(WIN, "red", player)
    # the first argument is where you want to draw the rectangle (player)
    # the second argument is the color you want it to be
    # the 3rd argument, the player, is the coordinates of the rectangle and the width and height of it. Look below for where player is created

    pygame.display.update()
    # pygame.display.update() updates every time something is drawn on the screen


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    # pass the starting x position, starting y position, width and height of the player 
    # the y position is a calculation used to get the player at the bottom of the screen
    # remember when y = 0, you are at the top of the screen
    # and going down the height increases positively

    # the speed the character moves at is determined by how fast the while loop runs
    # you want the speed to be consistent, without depending on the computer it is running on
    # to do this, you want to set up a clock "object" - not dictionary
    clock = pygame.time.Clock() 

    start_time = time.time()
    # time.time() gives us the current time
    elapsed_time = 0

    while run:
        clock.tick(60)
        # here you are putting in maximum frames per second, or number of times you want while loop to run per second

        elapsed_time = time.time() - start_time
        # every time we iterate, we are getting what the current time is and subtracting the start time to get number of seconds elapsed 
        # we can then draw the elapsed time on the screen
        # which we will do in the draw function for this code




        # the first thing to check
        # is whether the player hit the X on the window
        # if they did you want to close the window
        # this is not automatically programmed in
        # you need to handle the "key press" yourself
        for event in pygame.event.get():
            # this is a list of all the different
            # events that have occurred in the last 
            # iteration of this loop
            if event.type == pygame.QUIT:
                run = False
                # end while loop
                break
                # break out of for loop


        # to move the rectangle, we just have to adjust the x coordinate of the rectangle
        # the 1st thing we need to do is listen for different key presses
        # left arrow key = move left
        # right arrow key = move right
        keys = pygame.key.get_pressed()
       
        # this function gives you a dictionary of all the keys
        # the user can press and whether they have been pressed or not
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            # if they hit the left arrow key, move it to the left by the velocity you want the character to move at
            # the and statement, keeps the player from going off the screen
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + player.width + PLAYER_VEL <= WIDTH:
            player.x += PLAYER_VEL
            # you can obviously access player.y, player.width, and player.height too
            # other keys are pygame.K_SHIFT, pygame.K_SPACE, etc. there are many print them out to see




        draw(player, elapsed_time)
        
    pygame.quit()

if __name__ == "__main__":
    # this statement makes sure we are directly running on the Python file,
    # instead of importing it
    # if we imported this Python file from another Python file,
    # it would start running our game
    # that is a problem because we only want it to run
    # when we directly run this Python file ourselves
    main()