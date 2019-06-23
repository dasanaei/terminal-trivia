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
    def mostFrequent(List): 
        counter = 0
        num = List[0] 
        for i in List: 
            curr_frequency = List.count(i) 
            if(curr_frequency> counter): 
                counter = curr_frequency 
                num = i 
        return num 
    def format_string(str, min_length):
        while len(str) < min_length:
            str += " "
        return str