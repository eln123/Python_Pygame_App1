import pygame
import time
import random
pygame.font.init()
# we need to initialize the font module to render (draw) text
# this is a pygame requirement

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

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)
# comicsans is the type of font
# 30 is the font size

def draw(player, eLapsed_time, stars):
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

    time_text = FONT.render("Time: " + str(round(eLapsed_time)) + "s", 1, "white")
    # the round function rounds the time to the nearest second
    # the 1 stands for Anti-Aliasing, makes your text look better
    # white is color of text

    WIN.blit(time_text, (10, 10))
    # (10, 10) are the coordinates you want it to display at
  

    pygame.draw.rect(WIN, "red", player)
    # the first argument is where you want to draw the rectangle (player)
    # the second argument is the color you want it to be
    # the 3rd argument, the player, is the coordinates of the rectangle and the width and height of it. Look below for where player is created

    for star in stars:
        # drawing each star
        pygame.draw.rect(WIN, "white", star)
   


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

    star_add_increment = 2000
    star_count = 0
    # we will use this variable to keep a count so we know when to add the next star 

    stars = []
    # this list is where we will store all of the stars
    # then draw all the stars in this list onto the screen

    hit = False

    while run:
        star_count += clock.tick(60)
        # clock tick is storing the number of milliseconds since the last clock tic
        # for the clock tick, you are putting in maximum frames per second (e.g. 60), or number of times you want while loop to run per second

        elapsed_time = time.time() - start_time
        # every time we iterate, we are getting what the current time is and subtracting the start time to get number of seconds elapsed 
        # we can then draw the elapsed time on the screen
        # which we will do in the draw function for this code

        if star_count > star_add_increment:
            # if this is true, we are going to generate 3 stars to the screen
            for _ in range(3):
                                # here we are creating the stars
                # here, we are adding 3 stars to the screen
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                # here, we are picking a random integer for the x value, within the range of 0 to WIDTH of screen
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                # STAR_HEIGHT starts the star at top of screen, it is the Y coordinate
                # having a negative Y coordinate starts the star a little above the top of the screen
                # then as we move it down it looks like it came down from above
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 50)
            # 200 means star_add_increment will never be less than 200, it's a min
            # the - 50 means every time this runs, stars will be added 50 milliseconds faster
            # but the fastest time increment before it stops is 200 milliseconds, that is max speed
            # so first stars are added every 2000 milliseconds, then 1950, then 1900, etc until it gets to as fast as 200 millseconds
            star_count = 0



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


        for star in stars[:]:
            # in this loop, we are moving the stars
            # if the star hits the bottom of the screen,
            # without hitting our player, we want to get rid of them
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                # colliderect is a function that tells us if 2 rectangles have collided
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, ((WIDTH / 2) - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height()/2))
            # we have to calculate the coordinates so that the text will show up in the middle of screen, not too far to the right, or too high, so you need to take width and height of text into account
            pygame.display.update()
            # ^ this updates the screen after the window is blitted with lost_text puts the lost_text on the screen
            pygame.time.delay(4000)  
            # ^ this freezes the game
            break  
            # ^ this breaks us out of the while loop, ending the game



        draw(player, elapsed_time, stars)
     # here we are drawing the stars

    pygame.quit()

if __name__ == "__main__":
    # this statement makes sure we are directly running on the Python file,
    # instead of importing it
    # if we imported this Python file from another Python file,
    # it would start running our game
    # that is a problem because we only want it to run
    # when we directly run this Python file ourselves
    main()