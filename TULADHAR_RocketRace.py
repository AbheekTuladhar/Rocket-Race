'''
Student Name: Abheek Tuladhar 
Game title: Rocket Race
Period: 4 - HCP
Features of Game: Choose a rocket to win a race!
'''

import pygame, sys, random
pygame.init()                                         # Initialize game engine

# declare global variables here
WIDTH = 680                                           # Set window size
HEIGHT = WIDTH * 1.4
BLACK    = (0, 0, 0)                                  # Color Constants 
WHITE    = (255, 255, 255)
GREEN    = (0, 255, 0)
RED      = (255, 0, 0)
BLUE     = ( 0, 0, 255)

# Other global variables (WARNING: use sparingly):

# There are 50 units across and 40 units below
xu = WIDTH / 50
yu = HEIGHT/ 40

size = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("ROCKET RACE!!!")          # Window title
bg = pygame.image.load("SpaceBackground.jpg").convert_alpha()
red = pygame.image.load("red.png").convert_alpha()
blue = pygame.image.load("blue.png").convert_alpha()
green = pygame.image.load("green.png").convert_alpha()
redflame = pygame.image.load("RocketFlames.png").convert_alpha()
blueflame = pygame.image.load("RocketFlames.png").convert_alpha()
greenflame = pygame.image.load("RocketFlames.png").convert_alpha()

redRect = red.get_rect()
blueRect = blue.get_rect()
greenRect = green.get_rect()

win = 0
lose = 0
set_score = False

clock = pygame.time.Clock()                            # Manage timing for screen updates

def initRockets():
    redRect.bottom = HEIGHT
    blueRect.bottom = HEIGHT
    greenRect.bottom = HEIGHT

    redRect.centerx = 7*xu
    blueRect.centerx = WIDTH - 25*xu
    greenRect.centerx = WIDTH - 8*xu


def show_message(words, font_name, size, x, y, color, bg=None, hover=False):
    font = pygame.font.SysFont(font_name, size, True, False)
    text_image = font.render(words, True, color, bg)
    text_bounds = text_image.get_rect()  # bounding box of the text image
    text_bounds.center = (x, y)  # center text within the bounding box
    
    # find position of mouse pointer
    mouse_pos = pygame.mouse.get_pos()  # returns (x,y) of mouse location

    if text_bounds.collidepoint(mouse_pos) and bg != None and hover:
        # Regenerate the image on hover
        text_image = font.render(words, True, bg, color)  # swap bg and text color

    surface.blit(text_image, text_bounds)    #render on screen
    return text_bounds                      #bounding box returned for collision detection


def get_winner(choice):
    green = False
    blue = False
    red = False
    if choice == "Green":
        green = True
    elif choice == "Blue":
        blue = True
    elif choice == "Red":
        red = True

    if greenRect.top < 0 and redRect.top < 0:
        if green or red:
            return "Tie", "No Points!"
        else:
            return "Tie", "You Lose"
    elif greenRect.top < 0 and blueRect.top< 0:
        if green or blue:
            return "Tie", "No Points!"
        else:
            return "Tie", "You Lose"
    elif blueRect.top < 0 and redRect.top < 0:
        if blue or red:
            return "Tie", "No Points!"
        else:
            return "Tie", "You Lose"
    elif blueRect.top < 0 and redRect.top < 0 and greenRect.top < 0:
        return "All Tie!", "No Points!"    
    
    
    if greenRect.top < redRect.top and greenRect.top < blueRect.top:
        if green:
            return "Green Won!", "You Win"
        else:
            return "Green Won!", "You Lose"
    elif redRect.top < greenRect.top and redRect.top < blueRect.top:
        if red:
            return "Red Won!", "You Win"
        else:
            return "Red Won!", "You Lose"
    elif blueRect.top < redRect.top and blueRect.top < greenRect.top:
        if blue:
            return "Blue Won!", "You Win"
        else:
            return "Blue Won!", "You Lose"
    return "", ""


def drawScreen(game_in_play, choice):
    global win, lose, set_score

    surface.blit(bg, (0, 0))
    surface.blit(red, redRect)
    surface.blit(blue, blueRect) 
    surface.blit(green, greenRect)

    if game_in_play:
        surface.blit(redflame, (WIDTH - 48.5*xu, redRect.bottom))
        surface.blit(blueflame, (WIDTH-30.5*xu, blueRect.bottom))
        surface.blit(greenflame, (WIDTH-13.5*xu, greenRect.bottom))
    else:
        winner, ifwinner = get_winner(choice)
        show_message(str(winner), "Consolas", WIDTH//7, WIDTH//2, HEIGHT//2 + (2*yu), BLACK)
        show_message(str(ifwinner), "Consolas", WIDTH//7, WIDTH//2, HEIGHT//2 - (2*yu), BLACK)
        if set_score:
            if ifwinner == "You Win":
                win += 1
            elif ifwinner == "You Lose":
                lose += 1
            set_score = False

        win_message = "Wins: " + str(win)
        lose_message = "Lose: " + str(lose)
        show_message(win_message, "Consolas", WIDTH//30, WIDTH//2, 27*yu, BLACK, WHITE)
        show_message(lose_message, "Consolas", WIDTH//30, WIDTH//2, 28*yu, BLACK, WHITE)


# -------- Main Program Loop -----------
def main():                                # every program should have a main function
    global set_score

    initRockets()                          # other functions go above main

    # local  variables  
    game_in_play = False
    choice = None
    
    while True:
        for event in pygame.event.get():   # captures state of the game - loops thru changes
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):  # end game
                pygame.quit()                          
                sys.exit()

            # button, mouse, or keyboard interaction here
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if choose_bound_red.collidepoint(mouse_pos):
                    choice = "Red"
                elif choose_bound_blue.collidepoint(mouse_pos):
                    choice = "Blue"
                elif choose_bound_green.collidepoint(mouse_pos):
                    choice = "Green"

                initRockets()
                game_in_play = True
                set_score = True

        # ongoing game logic here  (repeats every 1/60 second) 

        redspeed = random.randint(1, 10)
        bluespeed = random.randint(1, 10)
        greenspeed = random.randint(1, 10)
        
        if game_in_play:
            redRect.top -= redspeed
            blueRect.top -= bluespeed
            greenRect.top -= greenspeed

        if redRect.top <= 0 or blueRect.top <= 0 or greenRect.top <= 0:
            game_in_play = False

        drawScreen(game_in_play, choice)

        if not game_in_play:
            choose_bound_red = show_message("Choose Red Rocket", "Consolas", WIDTH//40, 8*xu, HEIGHT - (5*yu), WHITE, RED, True)
            choose_bound_blue = show_message("Choose Blue Rocket", "Consolas", WIDTH//40, 25*xu, HEIGHT - (5*yu), WHITE, BLUE, True)
            choose_bound_green = show_message("Choose Green Rocket", "Consolas", WIDTH//40, 42*xu, HEIGHT - (5*yu), WHITE, GREEN, True)
        
        pygame.display.update()                         # updates the screen-
        clock.tick(60)                                  # FPS for animation (lower number to slow)
        
#----------------------------------------------------------------            
main()                                                  # runs the game