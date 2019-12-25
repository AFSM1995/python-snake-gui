# ------------------------------------------------ To-Do ------------------------------------------------
# Stop food from spawning on the snake.
# Fix pause traceback error
# Fix ignore user input while paused.
# Improve grid scaling
# Add sound
# Create simulation game mode and user game mode.
# Fix rapid control input causes collision. (moveing left fast down, right)

# ------------------------------------------------ Bug`s ------------------------------------------------
# Snake array needs and creates duplicate values at array locations 0 and 1.
# Traceback error when game quits while paused.

# ----------------------------------------- Screen x and y axis -----------------------------------------
# -------------------
# |  0,0  |  0,100  |
# -------------------
# | 100,0 | 100,100 |
# -------------------

import pygame as game
import sys
from random import randrange
from math import floor

# Python snake game.
def snake(snakeBlockLength, gameblockScale, screenWidthInBlockUnits, screenHeighInBlockUnits, snakeSpeed):
    # Set up the game window.
    screenWidthInPixelUnits = screenWidthInBlockUnits * gameblockScale
    screenHeighInPixelUnits = screenHeighInBlockUnits * gameblockScale
    screen = game.display.set_mode((screenWidthInPixelUnits+1, screenHeighInPixelUnits+1))
    game.display.set_caption(' Snake')
    game.display.set_icon(game.image.load(r'C:\Users\Alvaro Santillan\Documents\Programming Projects\perfect_snake\logo.png').convert())

    # Create and position the snake and the food.
    # Set the snake head position at bottom of screen x pixels before the screen ends.
    snakeDirection = 'right'
    snakeBlockLength = (snakeBlockLength*gameblockScale)-gameblockScale
    snakeYPos = screenHeighInPixelUnits-gameblockScale
    snakeBodyPos = []

    for i in range(snakeBlockLength, -gameblockScale, -gameblockScale):
        snakeBodyPos.append([i,snakeYPos])
    snakeBodyPos.insert(0, list(snakeBodyPos[0]))
    foodPos = [randrange(0,screenWidthInPixelUnits, gameblockScale),randrange(0,screenHeighInPixelUnits, gameblockScale)]

    # Set up the game colors.
    white = game.Color(255, 255, 255)
    lightGray = game.Color(35, 35, 35)
    black = game.Color(0, 0, 0)
    
    # Set up game statistics.
    gameScore = 0
    paused = False
    
    # Each loop represents playing one frame of the game.
    while True:
        # Listen for a keypress.
        for event in game.event.get():
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    gameOver(gameScore)
                if event.key == game.K_SPACE:
                    paused = not paused
                elif event.key == game.K_RIGHT and snakeDirection != 'left':
                    snakeDirection = 'right'
                elif event.key == game.K_LEFT and snakeDirection != 'right':
                    snakeDirection = 'left'
                elif event.key == game.K_UP and snakeDirection != 'down':
                    snakeDirection = 'up'
                elif event.key == game.K_DOWN and snakeDirection != 'up':
                    snakeDirection = 'down'
            elif event.type == game.QUIT:
                gameOver(gameScore)
        if not paused:
            # Create new block at snake head according to last key pressed.
            if snakeDirection == 'right':
                snakeBodyPos[0][0] += gameblockScale
            elif snakeDirection == 'left':
                snakeBodyPos[0][0] -= gameblockScale
            elif snakeDirection == 'up':
                snakeBodyPos[0][1] -= gameblockScale
            else:
                snakeBodyPos[0][1] += gameblockScale

            # Insert a new block at snake head according to last key pressed.    
            snakeBodyPos.insert(0, list(snakeBodyPos[0]))
            # Handle if snake head touched a screen edge.
            if snakeBodyPos[0][0] >= screenWidthInPixelUnits or snakeBodyPos[0][0] < 0:
                gameOver(gameScore)
            elif snakeBodyPos[0][1] >= screenHeighInPixelUnits or snakeBodyPos[0][1] < 0:
                gameOver(gameScore)
            # Handle if snake head touched the food.
            elif snakeBodyPos[0] == foodPos:
                gameScore += 1
                foodPos = [randrange(0,screenWidthInPixelUnits, gameblockScale),randrange(0,screenHeighInPixelUnits, gameblockScale)]
            # Pop and hide last tail block to simulate movement.
            else:
                game.draw.rect(screen, black, game.Rect(snakeBodyPos[-1][0],snakeBodyPos[-1][1],gameblockScale,gameblockScale))
                snakeBodyPos.pop()

            # Check for a self collision and draw the snake.
            for index, bodyBlock in enumerate(snakeBodyPos):
                game.draw.rect(screen, white, game.Rect(bodyBlock[0],bodyBlock[1],gameblockScale,gameblockScale))
                if index > 4 and snakeBodyPos[0] == bodyBlock:
                    gameOver(gameScore)

            # Draw food and grid.
            game.draw.rect(screen, white, game.Rect(foodPos[0],foodPos[1],gameblockScale,gameblockScale))
            if gameblockScale != 1:
                for i in range(0, screenWidthInPixelUnits+1, gameblockScale):
                    game.draw.line(screen, lightGray, [i, screenHeighInPixelUnits], [i,0], floor(gameblockScale/10))
                    game.draw.line(screen, lightGray, [screenWidthInPixelUnits, i], [0,i], floor(gameblockScale/10))
            # Load new frame on the screen and set famerate. 
            game.display.update()
            game.time.Clock().tick(snakeSpeed)

# Quit the snake game.
def gameOver(gameScore):
    game.quit()
    sys.exit
    print("Score:", gameScore)
    print("Game Length (ms):", game.time.get_ticks())

# snakeBlockLength, gameblockScale, screenWidthInBlockUnits, screenHeighInBlockUnits, snakeSpeed
# Note: Snake length must be between 1 and (screen width -1). 
snake(9,25,25,25,10)