from msvcrt import getch
class score():
    def __init__(self):
        self.totalScore = 0
        self.streak = 0
    def getCorrect(self,answerIndex, selectedIndex):
        print(answerIndex, selectedIndex)
        if answerIndex == selectedIndex:
            return 1
        else:
            return 0
    def updateScore(self,score):
        self.totalScore += score
    def calculateScore(self,correct, speed):
        if speed <= .5 and correct:
            score = 1000 + self.streak
            return score
        elif speed > 20 and correct:
            return 0
        elif correct:
            return int((1000 * (1 - ((speed / (20 - speed)) / 2))) + self.streak)
        elif not correct:
            return -100
        if speed < 20 and correct and self.streak < 500:
            self.streak += 100
    def getTotalScore(self):
        return self.totalScore