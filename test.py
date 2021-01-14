import pygame


class Button:
    def __init__(self, x, y, w, h, text=''):
       self.rect = pygame.Rect(x, y, w, h)
       self.color = (200,200,200)
       self.text = text
       self.txt_surface = FONT.render(text, True, self.color)
       self.active = False
    def update(self):
       width = max(200, self.txt_surface.get_width()+10)
       self.rect.w = width
    def draw(self, screen):
       pygame.draw.rect(screen, self.color, self.rect, 0)
       self.txt_surface = FONT.render(self.text, True, (0,0,0))
       screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
    def onClick(self):
        r = self.active
        self.active = False
        return r


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        r = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    r = self.text
                    self.text = ''
                elif event.key == pygame.K_DELETE:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
        return r
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    button1 = Button(100, 140, 140, 32, "button1")
    button2 = Button(100, 340, 140, 32, "button2")
    buttons = [button1, button2]

    exit_sw = False
    while not exit_sw:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_sw = True
            for n, box in enumerate(input_boxes):
                r = box.handle_event(event)
                if r != "":
                    buttons[n].text = r
            for box in input_boxes:
                box.update()
            for b in buttons:
                b.handle_event(event)
            for b in buttons:
                b.update()
        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)
        for b in buttons:
            b.draw(screen)
        for b in buttons:
            if b.onClick():
                print(b.text+" hit")

        pygame.display.flip()
        clock.tick(30)


pygame.init()
screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont("hg正楷書体pro", 16) #Ubuntu18.04 標準日本語フォント
main()
pygame.quit()