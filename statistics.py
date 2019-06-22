import csv
from pathlib import Path
import os.path
from os import path

class statistics:
    def __init__(self, cat, diff):
        self.totalGameNum = 0 
        self.category = cat
        self.difficulty = diff
        self.dataDir = str(Path.home()) + "/astral-kuarry/trivia/data/data.csv"
        print(self.dataDir)
        with open(self.dataDir) as csvfile:
            dataArry = csv.reader(csvfile, delimiter=',')
            for row in dataArry:
                #print(row)
                if len(row) != 0 and row[0] == '~':
                    self.totalGameNum = self.totalGameNum + 1
        identifyer = ["~", self.totalGameNum + 1]
        init = [cat, diff]
        with open(self.dataDir, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(identifyer)
            writer.writerow(init)
            f.close()
    def record(self, correct, speed):
        questionData = [correct, speed]
        with open(self.dataDir, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(questionData) 
            f.close()
    def endGameRecord(self, totalScore):
        with open(self.dataDir) as csvfile:
            dataArry = csv.reader(csvfile, delimiter=',')
            rows = list(dataArry)
            gameData = [float(rows[len(rows) - 10][1])]
            for i in range(len(rows) - 9, len(rows)):
                gameData.append(float(rows[i][1]))  
        totalTime = sum(gameData)    
        endGameData = [totalScore, totalTime]
        with open(self.dataDir, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(endGameData)
            f.close()
    def endGameEarly(self, questionNum):
        fillInNum = 10 - (questionNum - 1)
        with open(self.dataDir, 'a', newline='') as f:
            writer = csv.writer(f)
            for i in range(fillInNum):
                writer.writerow(["XXX","XXX"])
            writer.writerow(["DNF","DNF"])
    def getHighScore(self):
        with open(self.dataDir) as csvfile:
            dataArry = csv.reader(csvfile, delimiter=',')
            highScore = 0
            rows = list(dataArry)
            for i in range(len(rows)):
                if rows[i][0] == '~' and rows[i+12][0] != "DNF" and int(rows[i+12][0]) > highScore:
                    highScore = int(rows[i+12][0])
        return highScore
    def getAveragese(self):
        print("test")
    def getFavoriteInits(self):
        print("test")
    def winLoss(self):
        print("test")
    def statScreen(self):
        print("test")
    def inDepth(self):
        print("test")
    def getGameTotals(self): #total time, questions, and points
        print("test")





    def hardReset():
        f = open(str(Path.home()) + "/astral-kuarry/trivia/data/data.csv", "w+")
        f.close()