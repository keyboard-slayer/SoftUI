#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame

from pygame.locals import *
from ui.navbar import Navbar
from ui.launcher import Launcher

# ================= Config =================
RESOLUTION  = (480, 800) # Resolution de l'écran
SOFTUI_PATH = os.getcwd()
os.environ["dev"] = "dev"
# ==========================================

def call_launcher(screen: pygame.Surface, launcher: Launcher, navbar: Navbar) -> pygame.Rect:
    display.blit(launcher.get_surface(), (0, 0))
    return display.blit(navbar.get_surface(), (0, RESOLUTION[1]-50))

if __name__ == "__main__":
    pygame.init()

    os.environ["APP"] = os.path.join(SOFTUI_PATH, "apps")
    os.environ["FONT"] = os.path.join(SOFTUI_PATH, "fonts")

    display = pygame.display.set_mode(RESOLUTION)
    launcher = Launcher(RESOLUTION)
    navbar = Navbar(RESOLUTION)

    while True:
        rect_home = call_launcher(display, launcher, navbar)
        pygame.display.update()

        rect = pygame.Rect(
            navbar.get_rect().x + rect_home.x,
            navbar.get_rect().y + rect_home.y,
            navbar.get_rect().w,
            navbar.get_rect().h
        )

        for event in pygame.event.get():
            launcher.mainloop(event)
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if rect.collidepoint(event.pos):
                    launcher.closeApp()
                else:
                    launcher.handler(event.pos)
