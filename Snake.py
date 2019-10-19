# ------------------------------------------------ To-Do ------------------------------------------------
# Make game scale customizable ie 10 pixels size snake vs 1 pixel size.
# Custom snake size ie 9 block snake vs 5 block snake.
# fix food spawn on snake
# add pause
# add sound
# fix red x on game window

# ------------------------------------------------ Bug`s ------------------------------------------------
# snake array needs and creates duplicate values at array locations 0 and 1.

# ----------------------------------------- Screen x and y axis -----------------------------------------
# -------------------
# |  0,0  |  0,100  |
# -------------------
# | 100,0 | 100,100 |
# -------------------

import pygame as game
from random import randrange

# Python snake game.
def snake(screenWidthInBlockUnits, screenHeighInBlockUnits, snakeSpeed):
    # Set up the game window.
    screenWidthInPixelUnits = screenWidthInBlockUnits * 10
    screenHeighInPixelUnits = screenHeighInBlockUnits * 10
    screen = game.display.set_mode((screenWidthInPixelUnits, screenHeighInPixelUnits))
    game.display.set_caption(' Snake')
    game.display.set_icon(game.image.load(r'C:\Users\Alvaro Santillan\Documents\Programming Projects\perfect_snake\logo.png').convert())

    # Create and position the snake and the food.
    # Set the snake head position at bottom of screen x pixels before the screen ends.
    snakeYPos = screenHeighInPixelUnits-10
    snakeBodyPos = [[70,snakeYPos], [70,snakeYPos], [60,snakeYPos], [50,snakeYPos], [40,snakeYPos], [30,snakeYPos], [20,snakeYPos], [10,snakeYPos], [0,snakeYPos], 
        [-10,snakeYPos]]
    snakeDirection = 'right'
    foodPos = [randrange(0,screenWidthInPixelUnits, 10),randrange(0,screenHeighInPixelUnits, 10)]

    # Set up the game colors.
    white = game.Color(255, 255, 255)
    lightGray = game.Color(35, 35, 35)
    black = game.Color(0, 0, 0)
    
    # Set up game statistics.
    gameScore = 0
    
    # Each loop represents playing one frame of the game.
    while True:
        # Listen for a keypress.
        for event in game.event.get():
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    print(snakeBodyPos)
                    gameOver(gameScore)
                if event.key == game.K_RIGHT and snakeDirection != 'left':
                    snakeDirection = 'right'
                if event.key == game.K_LEFT and snakeDirection != 'right':
                    snakeDirection = 'left'
                if event.key == game.K_UP and snakeDirection != 'down':
                    snakeDirection = 'up'
                if event.key == game.K_DOWN and snakeDirection != 'up':
                    snakeDirection = 'down'
        # Create new block at snake head according to last key pressed.
        if snakeDirection == 'right':
            snakeBodyPos[0][0] += 10
        if snakeDirection == 'left':
            snakeBodyPos[0][0] -= 10
        if snakeDirection == 'up':
            snakeBodyPos[0][1] -= 10
        if snakeDirection == 'down':
            snakeBodyPos[0][1] += 10

        # Insert a new block at snake head according to last key pressed.    
        snakeBodyPos.insert(0, list(snakeBodyPos[0]))
        # Handle if snake head touched a screen edge.
        if snakeBodyPos[0][0] >= screenWidthInPixelUnits or snakeBodyPos[0][0] < 0:
            gameOver(gameScore)
        if snakeBodyPos[0][1] >= screenHeighInPixelUnits or snakeBodyPos[0][1] < 0:
            gameOver(gameScore)
        # Handle if snake head touched the food.
        if snakeBodyPos[0] == foodPos:
            gameScore += 1
            foodPos = [randrange(0,screenWidthInPixelUnits, 10),randrange(0,screenHeighInPixelUnits, 10)]
        # Pop and hide last tail block to simulate movement.
        else:
            game.draw.rect(screen, black, game.Rect(snakeBodyPos[-1][0],snakeBodyPos[-1][1],9,9))
            snakeBodyPos.pop()

        # Check for a self collision and draw the snake.
        for index, bodyBlock in enumerate(snakeBodyPos):
            game.draw.rect(screen, white, game.Rect(bodyBlock[0],bodyBlock[1],9,9))
            if index > 4 and snakeBodyPos[0] == bodyBlock:
                gameOver(gameScore)

        # Draw food and grid.
        game.draw.rect(screen, white, game.Rect(foodPos[0],foodPos[1],9,9))
        for i in range(-1, screenWidthInPixelUnits, 10):
            game.draw.line(screen, lightGray, [i, screenHeighInPixelUnits], [i,0], 1)
            game.draw.line(screen, lightGray, [screenWidthInPixelUnits, i], [0,i], 1)
        
        # Load new frame on the screen and set famerate. 
        game.display.update()
        game.time.Clock().tick(snakeSpeed)

# Quit the snake game.
def gameOver(gameScore):
    game.quit()
    print("Score:", gameScore)
    print("Game Length (ms):", game.time.get_ticks())

# screen width in block units, screen height in block units, game speed
snake(30,30,10)