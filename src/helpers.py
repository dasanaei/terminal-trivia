import platform, sys, tty, termios, os, time

class helpers():
    def macGetch(self, char_width=1):
        '''get a fixed number of typed characters from the terminal.
            Linux / Mac only'''
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(char_width)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def getchTrivia(self):
        if platform.system() == 'Windows':
            import msvcrt  # pylint: disable=import-error
            from msvcrt import getch # pylint: disable=import-error
            return getch()
        else:
            return self.macGetch()
    def clearScreen(self):
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
    def getInput(self):
        return chr(ord(self.getchTrivia()))
    def replaceHTML(self, string):
        return string.replace("&quot;", "").replace("&#039;", "'").replace("&shy;;", "-").replace("&ldquo;", "\"").replace("&rdquo;", "\"")
    def mostFrequent(self, List): 
        counter = 0
        num = List[0] 
        for i in List: 
            curr_frequency = List.count(i) 
            if(curr_frequency> counter): 
                counter = curr_frequency 
                num = i 
        return num 
    def format_string(self, str, min_length):
        while len(str) < min_length:
            str += " "
        return str

