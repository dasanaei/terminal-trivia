from msvcrt import getch
class score():
    def __init__(self):
        self.totalScore = 0
    def getCorrect(self,answerIndex, selectedIndex):
        print(answerIndex, selectedIndex)
        if answerIndex == selectedIndex:
            return 1
        else:
            return 0
    def updateScore(self,score):
        self.totalScore += score
    def calculateScore(self,correct, speed):
        print(correct) 
        #algorithm
        return 1
    def getTotalScore(self):
        return self.totalScore