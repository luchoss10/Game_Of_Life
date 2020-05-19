import pygame
import time
import numpy as np
#Start the module pygame
pygame.init()

#Establishing the width and height of the window
width, height = 1000, 1000

#Create the window with the size selected
screen = pygame.display.set_mode((height, width))

#Create the color for backGround
bgc = 25, 25, 24 

#Colored the window whit the background color
screen.fill(bgc)

#Variables for the size of grid cells
nxC, nyC = 25, 25

#Division of size window whit the size of grid cells to distribuid them 
sizeX = width/nxC
sizeY = height/nyC

#Create grid cell for stablishing the state of cells 0 for deads, 1 for alive
gameState =  np.zeros((nxC,nyC))

#Atomata stick
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1

#Atomata moving
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

#Pause variable for pause th game
pause = False

#The Game Of Life While 
while True:

    newGameState = np.copy(gameState)

    screen.fill(bgc)
    time.sleep(0.5)

    #Check press keyboard or mouse
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause
        
        mouseClick =  pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/sizeX)), int(np.floor(posY/sizeY))
            newGameState[celX, celY] = not mouseClick[2]
    
        #Recoed all cells 
    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pause:

                #Calculate the number of neighbers alive for the cell
                nNeighbors = gameState[(x-1) %nxC , (y-1) %nyC] + \
                            gameState[(x)    %nxC , (y-1) %nyC] + \
                            gameState[(x+1)  %nxC , (y-1) %nyC] + \
                            gameState[(x-1)  %nxC , (y) %nyC] + \
                            gameState[(x+1)  %nxC , (y) %nyC] + \
                            gameState[(x-1)  %nxC , (y+1) %nyC] + \
                            gameState[(x)    %nxC , (y+1) %nyC] + \
                            gameState[(x+1)  %nxC , (y+1) %nyC] 
                
                #Rule 1: Cell dead whit 3 neighbors

                if(gameState[x,y] == 0 and nNeighbors == 3):
                    newGameState[x,y] = 1
                
                #Rule 2: Cell alive whit less 2 neighbors or more than 3, cell died

                elif(gameState[x,y] == 1 and (nNeighbors < 2 or nNeighbors > 3)):
                    newGameState[x,y] = 0

                #Construction of each cell to draw
                poly = [((x)   * sizeX, y * sizeY), 
                        ((x+1) * sizeX, y * sizeY), 
                        ((x+1) * sizeX, (y+1) * sizeY), 
                        ((x)   * sizeX, (y+1) * sizeY)]

            #Draw Grid whit all Cells which a widht of 1 in 
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, 0)

    #Actualizate the game state for the new state
    gameState = np.copy(newGameState)

    #Refresh the screen in each fps
    pygame.display.flip()
