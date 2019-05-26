#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame
from typing import Tuple

class Shutdown:
    def __init__(self, size: Tuple[int, int]):
        self.screen_res = size

    def mainloop(self, event):
        if os.environ["dev"] == "dev":
            exit()
        else:
            os.system("poweroff")

    def get_surface(self) -> pygame.Surface:
        return pygame.Surface(self.screen_res)


def callObject(size: Tuple[int, int]) -> object:
    return Shutdown(size)
