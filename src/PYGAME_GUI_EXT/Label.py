import pygame

class BasicLabel():
    def __init__(self, x, y, size, text, color, fontName = None):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color
        self.fontName = fontName

        self.font = pygame.font.SysFont(fontName, size, True)
        self.textWidth, self.textHeight = self.font.size(text)

    def draw(self,win):
        text = self.font.render(self.text, 1, self.color)
        win.blit(text, (self.x , self.y))

    def centerText(self, winWidth):
        self.x = winWidth/2 - self.textWidth/2

    def getWidth(self):
        return self.textWidth
    
    def getHeight(self):
        return self.textHeight