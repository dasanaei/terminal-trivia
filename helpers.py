import time
import os
import platform
class helpers():
    def clearScrean():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
