#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import subprocess
import collections

import pygame
from pygame.locals import *

from typing import (
    Tuple,
    Dict
)

from string import (
    ascii_lowercase,
    digits
)

class Py64:
    def __init__(self, size: Tuple[int, int]):
        self.size = size
        self.visualLine = []
        self.codeLines = {}
        self.currentLine = ""

        self.surface = pygame.Surface(size)
        self.smallSurface = pygame.Surface((size[0] * 0.85, size[1] * 0.85))
        self.font = pygame.font.Font(os.path.join(os.environ["APP"], "py64/font/c64.ttf"), 15)
        self.blinkRect = None
        self.lineRect = None

        self.tick = time.time()
        #self.mem = subprocess.check_output(["free"]).decode().split('\n')[1].split(' ')[7]
        self.mem = "UNDEFINED"

    def execute_python(self, command: str) -> str:
        try:
            return subprocess.check_output(["python", "-c", command]).decode()[:-1]
        except subprocess.CalledProcessError:
            return "?SYNTAX ERROR"


    def draw(self):
        self.surface.fill((95, 83, 254))
        self.smallSurface.fill((33, 27, 174))

        title = self.font.render(" **** PY 64 PYTHON V1 **** ", True, (148, 163, 244))
        mem = self.font.render(f"{self.mem} Ki RAM SYSTEM", True, (148, 163, 244))
        ready = self.font.render("READY.", True, (148, 163, 244))

        for index, txt in enumerate(self.visualLine):
            line = self.font.render(txt, True, (148, 163, 244))
            self.smallSurface.blit(line, (10, 20*index + 100))

        line = self.font.render(self.currentLine, True, (148, 163, 244))
        self.smallSurface.blit(ready, (10, 80))
        self.blinkRect = pygame.Rect((10, 20*len(self.visualLine)+100, 12, 20))
        self.lineRect = self.smallSurface.blit(line, (10, 20*len(self.visualLine)+100))

        if not self.smallSurface.get_rect().colliderect(self.lineRect):
            self.visualLine = self.visualLine[2:]

        self.smallSurface.blit(title, (self.surface.get_width() // 10, 10))
        self.smallSurface.blit(mem, (10, 40))

        if 0.3 < time.time() - self.tick < 0.8:
            while self.lineRect.colliderect(self.blinkRect):
                self.blinkRect = self.blinkRect.move(1, 0)

            self.drawBlink()

        if time.time() - self.tick > 0.8:
            self.tick = time.time()

        pygame.display.flip()

    def drawBlink(self):
        pygame.draw.rect(
            self.smallSurface,
            (148, 163, 244),
            self.blinkRect
        )


    def sort_dico(self, dico: Dict[int, str]):
        return collections.OrderedDict(sorted(dico.items()))

    def mainloop(self, event):
        if event.type == KEYDOWN:
            need_ready = True

            keyname = pygame.key.name(event.key)
            special_key = ["\"", "\'", "(", ")", "=", ":", "[", "]", ";", "+"]
            key_nbr = ["world 64", "&","world 73", "\"", "\'", "(", "world 7", "world 72", "!", "world 71", "world 64"]

            if keyname == "space":
                self.currentLine += " "

            if keyname == "backspace":
                self.currentLine = self.currentLine[:-1]
                self.blinkRect = pygame.Rect((10, 100, 12, 20))
                self.drawBlink()

            if keyname[1:-1] in digits or keyname == "[.]":
                self.currentLine += keyname[1:-1]

            if keyname == "return":
                self.visualLine.append(self.currentLine)

                if self.currentLine.split(" ")[0].isdigit():
                    need_ready = False
                    self.codeLines[int(self.currentLine.split(" ")[0])] = " ".join(self.currentLine.split(" ")[1:])
                    self.codeLines = self.sort_dico(self.codeLines)

                elif self.currentLine == "list":
                    self.visualLine.append("")
                    for nbr, line in self.codeLines.items():
                        self.visualLine.append(f"{nbr} {line}")

                elif self.currentLine.split(" ")[0] == "del":
                    os.system("rm -rf {}".format(os.path.join(os.environ["APP"], "py64/scripts/{}.py".format(self.currentLine.split(" ")[1]))))

                elif self.currentLine == "clear":
                    self.visualLine = []
                    need_ready = False

                elif self.currentLine == "listing":
                    for script in os.listdir(os.path.join(os.environ["APP"], "py64/scripts")):
                        self.visualLine.append(".".join(script.split(".")[:-1]))

                elif self.currentLine.split(" ")[0] == "save":
                    with open(os.path.join(os.environ["APP"], f"py64/scripts/{self.currentLine.split(' ')[1]}.py"), "w") as script:
                        for line in self.codeLines.values():
                            script.write(f"{line}\n")

                elif self.currentLine.split(" ")[0] == "load":
                    with open(os.path.join(os.environ["APP"], f"py64/scripts/{self.currentLine.split(' ')[1]}.py"), "r") as script:
                        for nbr, line in enumerate(script.readlines()):
                            self.codeLines[10+(nbr*10)] = line[:-1]

                elif self.currentLine == "run":
                    with open("tmp.py", "w") as script:
                        for line in self.codeLines.values():
                            script.write(f"{line}\n")

                    self.visualLine.append("")
                    for line in subprocess.check_output(["python", "tmp.py"]).decode().split("\n"):
                        if line:
                            self.visualLine.append(line)
                    os.system("rm -rf tmp.py")


                else:
                    self.visualLine.append(self.execute_python(self.currentLine))
                    self.currentLine = ""


                self.currentLine = ""

                if need_ready:
                    self.visualLine.append("")
                    self.visualLine.append("READY")

            if keyname == ";" and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                self.currentLine += "."

            elif keyname in special_key:
                self.currentLine += keyname




            if keyname in ascii_lowercase and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                self.currentLine += keyname.upper()

            elif keyname in ascii_lowercase:
                self.currentLine += keyname

    def get_surface(self) -> pygame.Surface:
        self.draw()
        self.surface.blit(self.smallSurface, (self.size[0] * 0.07, self.size[1] * 0.05))
        return self.surface

def callObject(size: Tuple[int, int]) -> object:
    return Py64(size)
