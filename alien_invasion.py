import sys
import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button

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
    
    # Создания экземпляря для хранения игровой статистики
    stats = GameStats(ai_settings)
    
    # Создание групп пуль и пришельцев
    bullets = Group()
    aliens = Group()
    
    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Назначениие цвета фона.
    bg_color = (230, 230, 230)
    
    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")
    
    # Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, stats, play_button, screen, ship, aliens,
            bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, aliens, ship, bullets)
        else:
            play_button.draw_button()
        # При каждом проходе цикла перерисовывается экран.
        """Отображение последнего проприсованного экрана"""
        pygame.display.flip()

run_game()
