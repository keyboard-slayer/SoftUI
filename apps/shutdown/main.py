#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from template.AppTemplate import *

class Shutdown(AppTemplate):
    def __init__(self):
        AppTemplate.__init__(self)

    def mainloop(self):
        if os.environ["dev"] == "dev":
            exit()
        else:
            os.system("poweroff")


def callObject() -> object:
    return Shutdown()