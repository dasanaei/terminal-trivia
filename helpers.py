import time
import os
import platform
from msvcrt import getch
class helpers():
    def clearScreen():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
    def getInput():
        return chr(ord(getch()))
    def replaceHTML(string):
        return string.replace("&quot;", "").replace("&#039;", "'").replace("&shy;;", "-").replace("&ldquo;", "\"").replace("&rdquo;", "\"")
