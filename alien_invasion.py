import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色
    bg_color = (230, 230, 230)

    # 创建一艘飞船、一个子弹group和一个飞船group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的案例
    stats = GameStats(ai_settings)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
