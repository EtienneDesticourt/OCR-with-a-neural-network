'''
Created on 13 Jun 2014

@author: Etienne2
'''


import pygame,time
from pygame.locals import *
import os


class Render:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.grid = []
        for i in xrange(9):
            self.grid.append([])
            for j in xrange(9):
                self.grid[-1].append(pygame.Surface((800/9,600/9)))
                self.grid[-1][-1].fill((255,255,255))
                
        #################################  
        self.saveGrid = []    
        for i in xrange(9):
            self.saveGrid.append([])
            for j in xrange(9):
                self.saveGrid[-1].append(pygame.Surface((1,1)))
                self.saveGrid[-1][-1].fill((255,255,255))   
        self.saveSurf = pygame.Surface((9,9))
        #####################################
        self.endRun = False
        self.background = pygame.Surface((800,600))
        self.background.fill((255,255,255))
        self.block = pygame.Surface((800/9,600/9))
        self.currentLetter = "A"
    def resetGrid(self):
        for i in xrange(9):
            for j in xrange(9):
                self.grid[i][j].fill((255,255,255))
        for i in xrange(9):
            for j in xrange(9):
                self.saveGrid[i][j].fill((255,255,255))
    def run(self):
        while not self.endRun:
            
            for e in pygame.event.get():
                if e.type == MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0]:
                        x = e.pos[0]/89
                        y = e.pos[1]/67
                        self.grid[x][y].fill((0,0,0))
                        self.saveGrid[x][y].fill((0,0,0))
                elif e.type == KEYDOWN:
                    if e.key == 49:
                        temp = os.listdir("Dataset")
                        maximum = 0
                        for i in temp:
                            if self.currentLetter in i:
                                temp2 = int(i[1:].split(".")[0])
                                if temp2>maximum: maximum = temp2
                        pygame.image.save(self.saveSurf,"Dataset\\"+self.currentLetter+str(maximum+1)+".png")
                        self.resetGrid()
                    elif e.key == 50:
                        self.resetGrid()
                    else:
                        try:
                            #print chr(e.key)
                            if chr(e.key)==" ":
                                if self.currentLetter=="A":
                                    self.currentLetter = "B"
                                else:
                                    self.currentLetter = "A"
                                print self.currentLetter
                        except ValueError, e:
                            pass
                            #print e.key
                elif e.type == QUIT:
                    self.endRun = True
                    
            self.screen.blit(self.background,(0,0))
            for i in xrange(len(self.grid)):
                for j in xrange(len(self.grid[i])):
                    self.screen.blit(self.grid[i][j],(i*89,j*67))
            
            
            for i in xrange(len(self.grid)):
                for j in xrange(len(self.grid[i])):
                    self.saveSurf.blit(self.saveGrid[i][j],(i,j))
                    
                    
            
            pygame.display.flip()   
            time.sleep(0.01)
        pygame.quit()