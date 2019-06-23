import csv
from pathlib import Path
import os.path
from os import path
from score import score

class statistics:
    def __init__(self, cat, diff, newGame):
        self.totalGameNum = 0 
        self.category = cat
        self.difficulty = diff
        self.dataDir = str(Path.home()) + "/astral-kuarry/trivia/data/data.csv"
        print(self.dataDir)
        if newGame:
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
        else:
            with open(self.dataDir) as csvfile:
                dataArry = csv.reader(csvfile, delimiter=',')
                self.rows = list(dataArry)
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
    def checkForData(self):
        if len(self.rows) < 5:
            return False
        return True
    def getAverageses(self): #average time, points per question, average score per game
        times = []
        pointsPerQuestionn= []
        self.scorePerGame= []
        self.timePerGame = []
        self.totalQuestions = 0
        self.totalGames = 0
        statScore = score()
        for i in range(len(self.rows)):
            #print(self.rows[i][0])
            if (self.rows[i][0] == '~' or self.rows[i][0] == 'ï»¿~') and self.rows[i+12][0] != "DNF":
                self.totalGames = self.totalGames + 1
                for j in range(10):
                    times.append(float(self.rows[(i+2)+j][1]))
                    pointsPerQuestionn.append(float(statScore.calculateScore(int(self.rows[(i+2)+j][0]), float(self.rows[(i+2)+j][1]))))
                    self.totalQuestions = self.totalQuestions + 1
                self.scorePerGame.append(int(self.rows[(i+12)][0]))
                self.timePerGame.append(float(self.rows[(i+12)][1]))
        averagePointsPerQuestion = sum(pointsPerQuestionn) / len(pointsPerQuestionn)
        averageTimes = sum(times) / len(times)
        averageScorePerGame = sum(self.scorePerGame) / len(self.scorePerGame)
        averageTimePerGame = sum(self.timePerGame) / len(self.timePerGame)
        return [averageTimes, averagePointsPerQuestion, averageTimePerGame, averageScorePerGame]
    def getFavoriteInits(self): #get favorite category, get favorite difficultry
        print("work in progress")
    def winLoss(self): # Get wins, losses, and WL ratio
        correct = 0
        incorrect = 0
        for i in range(len(self.rows)):
            #print(self.rows[i][0])
            if (self.rows[i][0] == '~' or self.rows[i][0] == 'ï»¿~') and self.rows[i+12][0] != "DNF":
                for j in range(10):
                    #print(self.rows[(i+2)+j][0])
                    if int(self.rows[(i+2)+j][0]) == 1:
                        correct = correct + 1
                    if int(self.rows[(i+2)+j][0]) == 0:
                        incorrect = incorrect + 1
        return [correct, incorrect]
    def getGameTotals(self): #total time, total points, total questions answered, total games played
        return [sum(self.timePerGame), sum(self.scorePerGame), self.totalQuestions, self.totalGames]
    def inDepth(self):
        print("test")
        ##TODO






    def hardReset():
        f = open(str(Path.home()) + "/astral-kuarry/trivia/data/data.csv", "w+")
        f.close()