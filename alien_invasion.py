import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """Инициализирует игру и создает объект экрана."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion.")
    
    #Создание экзепляра корабля
    ship = Ship(ai_settings,screen)
    # Создание группы пуль
    bullets = Group()
    
    # Назначениие цвета фона.
    bg_color = (230, 230, 230)
    
    # Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        # При каждом проходе цикла перерисовывается экран.
        gf.update_screen(ai_settings, screen, ship, bullets)
        """Отображение последнего проприсованного экрана"""
        pygame.display.flip()

run_game()
