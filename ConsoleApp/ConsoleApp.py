import pygame
import time

import pygame

class ConsoleApp:
    def __init__(self):
        self.x = 1800
        self.y = 800

        pygame.init()
        pygame.font.init()

        self.highlighted_color = (255, 0, 0)
        self.default_color = (255, 255, 255)

        self.highlighted_index = 0
        self.chosen_index = None

        self.base_font = pygame.font.SysFont("Arial", 20)

        pygame.display.set_caption('Bank Transaction Risk & Anomaly Analyzer')
        self.screen = pygame.display.set_mode((self.x, self.y))

    # ------------------ PRIVATE METHODS ------------------ #

    def __draw_text(self, text, color, x, y):
        self.screen.blit(self.base_font.render(text, True, color), (x, y))

    def print_message(self, message, color):
        self.screen.fill((0, 0, 0))
        self.__draw_text(message, color, self.x / 2, self.y / 2)
        self.__draw_text('Press ESC to return', (255, 255, 0),
                          self.x / 2, self.y / 2 + 20)
        pygame.display.flip()
        self.__waiting_for_exit()

    def __print_menu_items(self, menu_items):
        for i, item in enumerate(menu_items):
            color = self.highlighted_color if i == self.highlighted_index else self.default_color
            self.__draw_text(item, color, self.x / 2.5, self.y / 2 + 20 * i)

    def __handle_navigation_keys(self, menu_size):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.highlighted_index = (self.highlighted_index - 1) % menu_size
                elif event.key == pygame.K_DOWN:
                    self.highlighted_index = (self.highlighted_index + 1) % menu_size
                elif event.key == pygame.K_RETURN:
                    self.chosen_index = self.highlighted_index

    def __waiting_for_exit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

    # ------------------ PUBLIC METHOD ------------------ #

    def output_screen(self, menu_items, message=None):
        self.screen.fill((0, 0, 0))
        self.highlighted_index = 0
        self.chosen_index = None
        if message is not None:
            self.__draw_text(message, (255, 255, 0),
                          self.x / 2.5, self.y / 2 - 20)

        while True:
            self.__print_menu_items(menu_items)
            self.__handle_navigation_keys(len(menu_items))

            if self.chosen_index is not None:
                return self.chosen_index

            pygame.display.flip()

