#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from typing import Tuple

class Calculator:
    def __init__(self, size: Tuple[int, int]):
        self.surface = pygame.Surface(size)
        self.size = size
        
    def get_surface(self) -> pygame.Surface:
        self.surface.fill((0, 0, 0))
        self.draw()
        return self.surface

    def mainloop(self):
        print("MAINLOOP")

def callObject(size: Tuple[int, int]) -> object:
    return Calculator(size)
