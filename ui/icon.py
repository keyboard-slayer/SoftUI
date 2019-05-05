#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class Icon:
    def __init__(self, Appath: str, iconPath: str):
        img = pygame.image.load(iconPath).convert_alpha()
        self.surface = pygame.transform.scale(img, (50, 50))
        self.path = Appath

    def get_surface(self) -> pygame.Surface:
        return self.surface

    def get_app_path(self) -> str:
        return self.path
