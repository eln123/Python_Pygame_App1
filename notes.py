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


def main():
    run = True

    while run:
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
    pygame.quit()

if __name__ == "__main__":
    # this statement makes sure we are directly running on the Python file,
    # instead of importing it
    # if we imported this Python file from another Python file,
    # it would start running our game
    # that is a problem because we only want it to run
    # when we directly run this Python file ourselves
    main()