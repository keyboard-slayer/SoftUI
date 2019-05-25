#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame
from typing import Tuple

class Shutdown:
    def __init__(self, size: Tuple[int, int]):
        self.screen_res = size

    def mainloop(self):
        if os.environ["dev"] == "dev":
            exit()
        else:
            os.system("poweroff")

    def get_surface() -> pygame.Surface:
        return pygame.Display(self.screen_res)


def callObject(size) -> object:
    return Shutdown(size)
