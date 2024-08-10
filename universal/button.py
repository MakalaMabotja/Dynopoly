import pygame
import universal.fonts as fonts

class Button:
    def __init__(self, screen, ftc, txt, bg_colour, txt_colour, bgc_hover, txtc_hover, x, y, width, height):
        self.screen = screen
        self.ftc = ftc
        self.txt = txt
        self.bg_colour = bg_colour
        self.txt_colour = txt_colour
        self.bgc_hover = bgc_hover
        self.txtc_hover = txtc_hover
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def updateButton(self, bgc, txtc):
        pygame.draw.rect(self.screen, bgc, pygame.Rect(self.x, self.y, self.width, self.height))
        btn_lbl = fonts.default_font.render(str(self.txt), False, txtc)
        self.screen.blit(btn_lbl, pygame.Vector2(self.x, self.y))

    def checkHover(self):
        mousepos = pygame.mouse.get_pos()

        if mousepos[0] >= self.x and mousepos[1] >= self.y and mousepos[0] <= self.x + self.width and mousepos[1] <= self.y + self.height:
            self.updateButton(self.bgc_hover, self.txtc_hover)

            if pygame.mouse.get_pressed()[0]:
                pass # Call function