
import sys
import pygame

class UI(object):
    def __init__(self):
        self.running = False
        self.bgcolor = (0,0,0)
        self.color = (255, 255, 255)
        self.fps = .25
        self.header_height = 24
        self.line_height = 16

        self.pygame_init()


    def pygame_init(self):
        try:
            pygame.display.init()
        except pygame.error:
            print 'Failed to initialize, {0}'.format(pygame.error)
            sys.exit(1)

        self.display_height = pygame.display.Info().current_h
        self.display_width = pygame.display.Info().current_w

        pygame.mouse.set_visible(0)
        clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.display_width, self.display_height), pygame.FULLSCREEN, 0)

    def pygame_font_init(self):
        try:
            pygame.font.init()
        except pygame.error:
            print 'Failed to initialize pygame.font, {0}'.format(pygame.error)
            sys.exit(1)

        self.header = pygame.font.Font("assets/whitrabt.ttf", header_height)
        self.line = pygame.font.Font("assets/whitrabt.ttf", line_height)

    def fade(self, screen=self.screen, start_pos=0, end_pos=self.display_height, color=self.bgcolor):
        y = start_pos
        #print "starting fade at: {0} -> {1}".format(y,end_pos)
        if running:
            while (y <= end_pos):
                coords = [(0,y),(self.display_width,y)]
                pygame.draw.lines(screen, color, True, coords, 2)
                pygame.display.flip()
                y += 2
                clock.tick(1250)
