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
# ==========================================

def call_launcher(screen: pygame.Surface, launcher: Launcher, navbar: Navbar):
    display.blit(launcher.get_surface(), (0, 0))
    display.blit(navbar.get_surface(), (0, RESOLUTION[1]-50))

if __name__ == "__main__":
    pygame.init()

    os.environ["APP"] = os.path.join(SOFTUI_PATH, "apps")
    os.environ["FONT"] = os.path.join(SOFTUI_PATH, "fonts")

    display = pygame.display.set_mode(RESOLUTION)
    launcher = Launcher(RESOLUTION)
    navbar = Navbar(RESOLUTION)

    call_launcher(display, launcher, navbar)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                launcher.handler(event.pos)