#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==============================================================================
# Title: 2048
# Author: Ryan J Slater
# Date: 12/25/2017
#==============================================================================

import pygame
import random as rand
import numpy as np

class colors():
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (200,0,0)
    GREEN = (0,200,0)
    BLUE = (0, 0, 200)
    BRIGHTRED = (255,0,0)
    BRIGHTGREEN = (0,255,0)
    BRIGHTBLUE = (0, 0, 255)
    BOARD = (187, 173, 160)

    def getTileColor(number):
        if number == 0:
            return((248, 238, 228,))
        elif number == 2:
            return((238, 228, 218))
        elif number == 4:
            return((237, 224, 200))
        elif number == 8:
            return((242, 177, 121))
        elif number == 16:
            return((245, 149, 99))
        elif number == 32:
            return((246, 124, 95))
        elif number == 64:
            return((246, 94, 59))
        elif number == 128:
            return((237, 207, 114))
        elif number == 256:
            return((237, 204, 97))
        elif number == 512:
            return((237, 200, 80))
        elif number == 1024:
            return((237, 197, 63))
        elif number == 2048:
            return((237, 194, 46))
        else:
            if number >= 131072:
                return((0, 0, 0))
            val = 4096
            color = 50
            while True:
                if number == val:
                    return((color, color, color))
                else:
                    color -= 10
                    val *= 2

    def getTileTextColor(number):
        if number >= 8:
            return((249, 246, 242))
        return((119, 110, 101))

def text_objects(text, font):
    textSurface = font.render(text, True, colors.BLACK)
    return textSurface, textSurface.get_rect()

def tileText(text, font, val):
    textSurface = font.render(text, True, colors.getTileTextColor(val))
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == game:
                game(displayWidth, displayHeight)
            elif action == optionMenu:
                optionMenu()
            else:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    text = pygame.font.SysFont('comicsansms', buttonTextSize)
    textSurf, textRect = text_objects(msg, text)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():
    text = pygame.font.SysFont('comicsansms', titleTextSize)
    TextSurf, TextRect = text_objects('Paused', text)
    TextRect.center = ((displayWidth/2), (displayHeight/2))
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        button('CONTINUE', int(displayWidth/2-(125/640)*displayWidth), int((3/4)*displayHeight), int((12/64)*displayWidth), int((5/48)*displayHeight), colors.GREEN, colors.BRIGHTGREEN, unpause)
        button('MAIN MENU', int((displayWidth/2)+(5/640)*displayWidth), int((3/4)*displayHeight), int((13/64)*displayWidth), int((5/48)*displayHeight), colors.RED, colors.BRIGHTRED, game)
        pygame.display.update()
        clock.tick(60)

def quitGame():
    pygame.quit()
    quit


#==================================================================================================================


def gameIntro():
    gameDisplay.fill(colors.WHITE)
    largeText = pygame.font.SysFont('comicsansms', titleTextSize)
    smallText = pygame.font.SysFont('comicsansms', buttonTextSize)
    TextSurf, TextRect = text_objects('2048', largeText)
    TextRect.center = (int(displayWidth/2), int(displayHeight/2))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects('Ryan J Slater', smallText)
    TextRect.center = ((displayWidth/2), (displayHeight/2)+int((4/48)*displayHeight))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        button('PLAY', int((displayWidth/2)-(165/640)*displayWidth), int((3/4)*displayHeight), int((10/64)*displayWidth), int((5/48)*displayHeight), colors.GREEN, colors.BRIGHTGREEN, gameLoop)
        button('OPTIONS', int((displayWidth/2)-(55/640)*displayWidth), int((3/4)*displayHeight), int((11/64)*displayWidth), int((5/48)*displayHeight), colors.BLUE, colors.BRIGHTBLUE, optionMenu)
        button('QUIT', int((displayWidth/2)+(65/640)*displayWidth), int((3/4)*displayHeight), int((10/64)*displayWidth), int((5/48)*displayHeight), colors.RED, colors.BRIGHTRED, quitGame)

        pygame.display.update()
        clock.tick(60)

def changeRes1():
    global displayWidth
    global displayHeight
    global buttonTextSize
    global titleTextSize
    titleTextSize = 77
    buttonTextSize = 20
    displayWidth = 480
    displayHeight = 320
    game(displayWidth, displayHeight)

def changeRes2():
    global displayWidth
    global displayHeight
    global buttonTextSize
    global titleTextSize
    titleTextSize = 115
    buttonTextSize = 30
    displayWidth = 640
    displayHeight = 480
    game(displayWidth, displayHeight)

def changeRes3():
    global displayWidth
    global displayHeight
    global buttonTextSize
    global titleTextSize
    titleTextSize = 144
    buttonTextSize = 38
    displayWidth = 1024
    displayHeight = 600
    game(displayWidth, displayHeight)

def changeRes4():
    global displayWidth
    global displayHeight
    global buttonTextSize
    global titleTextSize
    titleTextSize = 216
    buttonTextSize = 56
    displayWidth = 1200
    displayHeight = 900
    game(displayWidth, displayHeight)

def changeRes5():
    global displayWidth
    global displayHeight
    global buttonTextSize
    global titleTextSize
    titleTextSize = 259
    buttonTextSize = 68
    displayWidth = 1920
    displayHeight = 1080
    game(displayWidth, displayHeight)

def optionMenu():
    # TODO:
    # Graphics Options:
        # Color Scheme
        # Display Resolution
    global displayWidth
    global displayHeight
    gameDisplay.fill(colors.WHITE)
    text = pygame.font.SysFont('comicsansms', titleTextSize)
    TextSurf, TextRect = text_objects('Options', text)
    TextRect.center = ((displayWidth/2), int((5/48)*displayHeight))
    gameDisplay.blit(TextSurf, TextRect)

    text = pygame.font.SysFont('comicsansms', buttonTextSize)
    TextSurf, TextRect = text_objects('Resolution', text)
    TextRect.center = (int(displayWidth/3), int((11/48)*displayHeight))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects('Color Scheme', text)
    TextRect.center = (int(2*displayWidth/3), int((11/48)*displayHeight))
    gameDisplay.blit(TextSurf, TextRect)

    text = pygame.font.SysFont('comicsansms', int(buttonTextSize/2))
    TextSurf, TextRect = text_objects(str(displayWidth) + 'x' + str(displayHeight), text)
    TextRect.center = (int(displayWidth/3), int((125/480)*displayHeight))
    gameDisplay.blit(TextSurf, TextRect)

    buttonWidth = int((11/48)*displayWidth)
    buttonHeight =  int((5/48)*displayHeight)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        button('BACK', int((1/48)*displayWidth), int((1/48)*displayHeight), buttonWidth, buttonHeight, colors.RED, colors.BRIGHTRED, game)
        button('480x320', int((displayWidth/3)-(buttonWidth/2)), int((135/480)*displayHeight), buttonWidth, buttonHeight, colors.BLUE, colors.BRIGHTBLUE, changeRes1)
        button('640x480', int((displayWidth/3)-(buttonWidth/2)), int((195/480)*displayHeight), buttonWidth, buttonHeight, colors.BLUE, colors.BRIGHTBLUE, changeRes2)
        button('1024x600', int((displayWidth/3)-(buttonWidth/2)), int((255/480)*displayHeight), buttonWidth, buttonHeight, colors.BLUE, colors.BRIGHTBLUE, changeRes3)
        button('1200x900', int((displayWidth/3)-(buttonWidth/2)), int((315/480)*displayHeight), buttonWidth, buttonHeight, colors.BLUE, colors.BRIGHTBLUE, changeRes4)
        button('1920x1080', int((displayWidth/3)-(buttonWidth/2)), int((375/480)*displayHeight), buttonWidth, buttonHeight, colors.BLUE, colors.BRIGHTBLUE, changeRes5)
        pygame.display.update()
        clock.tick(60)

def getInitialBoard():
    board = np.zeros((4, 4), dtype=int)
    coord = (rand.randint(0, 3), rand.randint(0, 3))
    if rand.randint(0, 100) > 10:
        board[coord] = 2
    else:
        board[coord] = 4
    while True:
        coord2 = (rand.randint(0, 3), rand.randint(0, 3))
        if coord2 != coord:
            board[coord2] = 2
            if rand.randint(0, 100) < 10 and board[coord] != 4:
                board[coord2] = 4
            return board

def checkLoss(board):
    zeros = 0
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                zeros += 1
            else:
                if row > 0:
                    if board[row][col] == board[row-1][col]:
                        return False
                if row < 3:
                    if board[row][col] == board[row+1][col]:
                        return False
                if col > 0:
                    if board[row][col] == board[row][col-1]:
                        return False
                if col < 3:
                    if board[row][col] == board[row][col+1]:
                        return False
    if zeros > 0:
        return False
    return True

def drawTile(row, col, w, h, origin, val):
    text = [pygame.font.SysFont('comicsansms', int((3/2)*buttonTextSize)), pygame.font.SysFont('comicsansms', int((7/6)*buttonTextSize)), pygame.font.SysFont('comicsansms', int((5/6)*buttonTextSize))]
    pygame.draw.rect(gameDisplay, colors.getTileColor(val), (origin[0]+col*(w+10), origin[1]+row*(h+10), w, h))
    if val < 1000:
        text = text[0]
    elif val < 10000:
        text = text[1]
    elif val < 100000:
        text = text[2]
    if val != 0:
        TextSurf, TextRect = tileText(str(val), text, val)
        TextRect.center = ((origin[0]+col*(w+10)+int(w/2), origin[1]+row*(h+10)+int(h/2)))
        gameDisplay.blit(TextSurf, TextRect)

def drawBoard(board, dw, dh):
    gameDisplay.fill(colors.WHITE)
    tileWidth, tileHeight = int(dh/5), int(dh/5)
    if dw < dh:
        tileWidth, tileHeight = int(dw/5), int(dw/5)

    origin = (int(dw/2)-2*tileHeight-15, int(dh/2)-2*tileWidth-15)
    pygame.draw.rect(gameDisplay, colors.BOARD, (origin[0]-10, origin[1]-10, 4*tileWidth+50, 4*tileHeight+50))
    for row in range(4):
        for col in range(4):
            drawTile(row, col, tileWidth, tileHeight, origin, board[row][col])

def gameLoss():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        largeText = pygame.font.SysFont('comicsansms', titleTextSize)
        TextSurf, TextRect = text_objects('You Lose', largeText)
        TextRect.center = ((displayWidth/2), (displayHeight/2))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf, TextRect)
        button('PLAY AGAIN', int((displayWidth/2)-(135/640)*displayWidth), int((3/4)*displayHeight), int((13/64)*displayWidth), int((5/48)*displayHeight), colors.GREEN, colors.BRIGHTGREEN, gameLoop)
        button('QUIT', int((displayWidth/2)+(5/640)*displayWidth), int((3/4)*displayHeight), int((10/64)*displayWidth), int((5/48)*displayHeight), colors.RED, colors.BRIGHTRED, quitGame)
        pygame.display.update()
        clock.tick(60)

def moveRow(row, direction):
    if direction == 'left' or direction == 'up':
        for i in range(len(row)):
            if row[i] != 0:
                if i > 0:
                    moveto = 0
                    for j in range(i-1, -1, -1):
                        if row[j] != 0:
                            moveto = j
                            break
                    if row[moveto] != 0:
                        if row[moveto] != row[i]:
                            moveto += 1
                    if moveto != i:
                        row[moveto] += row[i]
                        row[i] = 0
                else:
                    i += 1
    else:
        for i in range(len(row)-1, -1, -1):
            if row[i] != 0:
                if i < len(row)-1:
                    moveto = len(row)-1
                    for j in range(i+1, len(row)):
                        if row[j] != 0:
                            moveto = j
                            break
                    if row[moveto] != 0:
                        if row[moveto] != row[i]:
                            moveto -= 1
                    if moveto != i:
                        row[moveto] += row[i]
                        row[i] = 0
                else:
                    i -= 1
    return row

def shift(board, direction):
    origBoard = np.copy(board)
    if direction == 'left' or direction == 'right':
        for row in range(4):
            tmprow = np.array([0, 0, 0, 0])
            for col in range(4):
                tmprow[col] = board[row][col]
            tmprow = moveRow(tmprow, direction)
            for i in range(len(tmprow)):
                board[row][i] = tmprow[i]

    elif direction == 'up' or direction == 'down':
        for col in range(4):
            tmpcol = np.array([0, 0, 0, 0])
            for row in range(4):
                tmpcol[row] = board[row][col]
            tmpcol = moveRow(tmpcol, direction)
            for i in range(len(tmpcol)):
                board[i][col] = tmpcol[i]

    if np.array_equal(origBoard, board):
        return(board)

    while True:
        coord = (rand.randint(0, 3), rand.randint(0, 3))
        if board[coord] == 0:
            if rand.randint(0, 100) > 10:
                board[coord] = 2
            else:
                board[coord] = 4
            return(board)

def gameLoop():
    global pause
    board = getInitialBoard()

    while True:
        if checkLoss(board):
            gameLoss()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    board = shift(board, 'left')
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    board = shift(board, 'right')
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    board = shift(board, 'down')
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    board = shift(board, 'up')
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()
        drawBoard(board, displayWidth, displayHeight)
        pygame.display.update()
        clock.tick(60)

def game(dw, dh):
    global displayWidth
    global displayHeight
    global pause
    global gameDisplay
    global clock
    global options

    pygame.init()
    displayWidth = dw
    displayHeight = dh
    pause = False
    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption('2048')
    clock = pygame.time.Clock()

    gameIntro()
    gameLoop()
    quitGame()

titleTextSize = 115
buttonTextSize = 30
game(640, 480)