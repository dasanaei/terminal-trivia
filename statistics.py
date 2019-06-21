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
    def endGameRecord(self, totalScore, totalTime):
        endGameData = [totalScore, totalTime]
        with open(self.dataDir, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(endGameData)
            f.close()
    def endGameEarly():
        print("do this")
    def getHighScore(self):
        print('test')
    def writeData(self):
        print("test")
    def statScreen(self):
        print("test")
    def inDepth(self):
        print("test")
    def getGameTotals(self):
        print("test")





    def hardReset():
        f = open(str(Path.home()) + "/astral-kuarry/trivia/data/data.csv", "w+")
        f.close()