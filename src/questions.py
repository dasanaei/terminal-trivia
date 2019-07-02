from helpers import helpers
import random, time
import sys, json
from urllib.request import urlopen

class questions:
    def __init__(self, category, difficulty):
        self.questionArry = []
        self.correctAnswerArry = []
        self.wrongAnswerArry = []
        self.valid = True
        helpers().clearScreen()
        print("Initializing Game...\n")
        print("Warning: exiting console without pressing [e] during game will currupt data.")
        if difficulty == '1':
            newDiff = "easy"
        elif difficulty == '2':
            newDiff = "medium"
        elif difficulty == '3':
            newDiff = "hard"
        if category == '1':
            interval = random.randint(1,2)
            if interval == 1:
                randomCatNum = random.randint(50,57)
            else:
                while 1:
                    randomCatNum = random.randint(97,102)
                    if randomCatNum != 101:
                        break
            category = chr(randomCatNum)
        if category == '2':
            newCat = '9'
        if category == '3':
            newCat = '10'
        if category == '4':
            newCat = '11'
        if category == '5':
            newCat = '13'
        if category == '6':
            newCat = '14'
        if category == '7':
            newCat = '19'
        if category == '8':
            newCat = '22'
        if category == '9':
            newCat = '21'
        if category == 'a':
            newCat = '23'
        if category == 'b':
            newCat = '24'
        if category == 'c':
            newCat = '25'
        if category == 'd':
            newCat = '26'
        if category == 'f':
            newCat = '31'
        #print(newCat, newDiff)
        api = "https://opentdb.com/api.php?amount=10&category=" + newCat + "&difficulty=" + newDiff + "&type=multiple"
        jsonurl = urlopen(api)
        data = json.loads(jsonurl.read()) # <-- read from it
        #print(data)
        if data['response_code'] == 1:
            self.valid = False
            return
        for question in data['results']:
            self.questionArry.append(helpers().replaceHTML(question['question']))
       # print("\n", self.questionArry)

        for correctAnswer in data['results']:
            self.correctAnswerArry.append(helpers().replaceHTML(correctAnswer['correct_answer']))
        #print("\n", self.correctAnswerArry)

        for wrongAnswer in data['results']:
            self.wrongAnswerArry.append(wrongAnswer['incorrect_answers'])

        for i in range(len(self.wrongAnswerArry)):
            for j in range(len(self.wrongAnswerArry[i])):
                self.wrongAnswerArry[i][j] = helpers().replaceHTML(self.wrongAnswerArry[i][j])

       # print("\n", self.wrongAnswerArry)
        time.sleep(2)
    def getQuestion(self,i):
        return self.questionArry[i] 

    def getCorrectAnswer(self,i):
        return self.correctAnswerArry[i]

    def getAnswers(self,i):
        randIndex = random.randint(0,3)
        answerArry = self.wrongAnswerArry[i]
        insertAnswer = self.correctAnswerArry[i]
        answerArry.insert(randIndex, insertAnswer)
        return [answerArry, randIndex]
    def checkAPI(self):
        return self.valid
        
