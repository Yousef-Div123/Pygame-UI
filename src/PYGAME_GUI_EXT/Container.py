import pygame
from abc import ABC, abstractmethod

class Grid():
    def __init__(self, window, numberOfCols, numberOfRows):
        self.x = 0
        self.y = 0
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.numberOfCols = numberOfCols if numberOfCols >= 1 else 1
        self.numberOfRows = numberOfRows if numberOfRows >= 1 else 1
        self.blockWidth = self.width/numberOfCols
        self.blockHeight = self.height/numberOfRows
        self.children = []

    def showGrid(self):
        for x in range(self.numberOfRows):
            xPos = self.blockWidth * (x + 1)
            pygame.draw.line(self.window, (0, 0, 0), (xPos, 0), (xPos, self.height))

        for y in range(self.numberOfCols):
            yPos = self.blockHeight * (y + 1)
            pygame.draw.line(self.window, (0, 0, 0), (0, yPos), (self.width, yPos))

    def addChild(self, child, startPos: tuple, colSpan = 1, rowSpan = 1):
        # startPos[0] = colNumber, startPos[1] = rowNumber


        # input validation
        
        if(startPos[0] + colSpan >  self.numberOfCols or startPos[1] + rowSpan > self.numberOfRows ):
            raise ValueError("object is out of bound")
        
        
        # setting y and x for the child
        child.setX(startPos[0]*self.blockWidth)
        child.setY(startPos[1]*self.blockHeight)

        # setting the width and height of the child
        width = colSpan * self.blockWidth
        height = rowSpan * self.blockHeight
        child.setWidth(width)
        child.setHeight(height)
        
        self.children.append(child)

    def render(self):
        for child in self.children:
            child._draw(self.window)
            # print("x:", child.x)
            # print("y:", child.y)
            # print("width:", child.width)
            # print("height:", child.height)

    def checkEvent(self, event):    
        for child in self.children:
            child._checkEvent(event)