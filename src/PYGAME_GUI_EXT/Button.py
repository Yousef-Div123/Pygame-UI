import pygame

class BasicButton():
    def __init__(self, x, y, size, text, action, color, textColor,fontName=None):
        self.x = x
        self.y = y
        self.width = size
        self.text = text
        self.color = color
        self.action = action
        self.textColor =  textColor
        self.padding = size *0.05
        
        self.fontSize = int(size*0.25) 
        self.font = pygame.font.SysFont(fontName, self.fontSize , True)
        self.textWidth, self.textHeight = self.font.size(self.text)

        self.width = self.textWidth + self.padding*2
        self.height = self.textHeight + + self.padding*2

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, int(self.width*0.05))
        text = self.font.render(self.text, 1, self.textColor)
        win.blit(text, (self.x + self.padding, self.y + self.height/2 - self.textHeight/2))

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def checkClicked(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if(self.x + self.width>=mouseX>= self.x and self.y + self.height>=mouseY>= self.y):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.action()


        return self.textHeight