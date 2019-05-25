#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from typing import Tuple

class Navbar:
    def __init__(self, screen_res: Tuple[int, int]):
        self.surface = pygame.Surface((screen_res[0], 50))
        self.home_btn_rect = pygame.draw.circle(
            self.surface,
            (255,255,255),
            (screen_res[0]//2, 25),
            15,
            1
        )

    def get_surface(self) -> pygame.Surface:
        return self.surface

    def get_rect(self) -> pygame.Rect:
        return self.home_btn_rect
