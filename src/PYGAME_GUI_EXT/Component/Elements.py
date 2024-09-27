
import pygame
from abc import ABC, abstractmethod

# abstract class
class GuiElement(ABC):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    @abstractmethod
    def _draw(self, win):
        pass

    @abstractmethod
    def _checkEvent(self, event):
        pass

class TestingBox(GuiElement):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def _draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def _checkEvent(self, event):
        pass

class BasicButton(GuiElement):
    def __init__(self, text, action, color, textColor,fontName=None):
        super().__init__()
        self.text = text
        self.color = color
        self.action = action
        self.textColor =  textColor
        self.fontName = fontName


    def _draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, int(self.width*0.07))
        text = self.font.render(self.text, 1, self.textColor)
        win.blit(text, (self.x + self.padding, self.y + self.height/2 - self.textHeight/2))

    def setWidth(self, width):
        self.width = width
        
        self.fontSize = int(width*0.33) 
        self.font = pygame.font.SysFont(self.fontName, self.fontSize , True)
        self.textWidth, self.textHeight = self.font.size(self.text)
        self.padding = (width - self.textWidth)/2 


    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def _checkEvent(self, event):
        mouseX, mouseY = pygame.mouse.get_pos()

        if(self.x + self.width>=mouseX>= self.x and self.y + self.height>=mouseY>= self.y and event.type == pygame.MOUSEBUTTONDOWN):
            self.action()


class BasicLabel(GuiElement):
    def __init__(self, text, color, fontName = None):
        super().__init__()
        self.text = text
        self.color = color
        self.fontName = fontName

    def _draw(self,win):
        text = self.font.render(self.text, 1, self.color)
        win.blit(text, (self.x + self.padding, self.y + self.height/2 - self.textHeight/2))

    def centerText(self, winWidth):
        self.x = winWidth/2 - self.textWidth/2

    def setWidth(self, width):
        self.width = width
        
        self.setFont()

    def setText(self, text):
        self.text = text

        self.setFont()    

    def setFont(self):
        self.fontSize = int((self.width/ len(self.text))*2) 
        self.font = pygame.font.SysFont(self.fontName, self.fontSize , True)
        self.textWidth, self.textHeight = self.font.size(self.text)
        self.padding = (self.width - self.textWidth)/2 

    def _checkEvent(self, event):
        pass


