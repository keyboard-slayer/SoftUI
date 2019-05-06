#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class Shutdown:
    def __init__(self):
        self = self

    def mainloop(self):
        if os.environ["dev"] == "dev":
            exit()
        else:
            os.system("poweroff")


def callObject() -> object:
    return Shutdown()
