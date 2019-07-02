from helpers import helpers
from questions import questions
from score import score
from intro import intro 
from statistics import statistics
import time
import sys
import locale
import datetime
def getpreferredencoding(do_setlocale = True):
   return "utf-8"
locale.getpreferredencoding = getpreferredencoding
def runTrivia():
    while 1:
        choice = intro().menu()
        if (choice >= 49 and choice <= 51) or choice == 101 or choice == 113:
            break
    speedRun = False  
    if choice == 113:
        speedRun = True
    if choice == 49 or speedRun:    ## Play the game
        while 1:
            while 1:
                helpers().clearScreen()
                print("Select Category")
                print(" [1] Random Category \n [2] General Knowledge \n [3] Books \n [4] Film \n [5] Musicals/Theater \n [6] Television \n [7] Math \
                    \n [8] Geography \n [9] Sports \n [a] History \n [b] Politics \n [c] Art \n [d] Trash \n [f] Japanese Anime and Manga")
                category = ord(helpers().getchTrivia())
                if (category >= 49 and category <= 57) or (category >= 97 and category <= 100) or category == 102:
                    break
                if category == 101:
                    sys.exit()     
            while 1: 
                helpers().clearScreen()
                print("Select Difficulty")
                print(" [1] Easy \n [2] Medium \n [3] Hard")
                difficulty = ord(helpers().getchTrivia())
                if (difficulty >= 49 and difficulty <= 51):
                    break
                if difficulty == 101:
                    sys.exit()
            selectedQuestions = questions(chr(category), chr(difficulty))
            if selectedQuestions.checkAPI():
                break
            print("This category/difficulty is currently unavailable. Pick something else.")
            time.sleep(2)
        gameScore = score()
        print("Press Any Key to Start the Game")
        helpers().getchTrivia()
        helpers().clearScreen()
        gameStats = statistics(category, difficulty, True)
        for i in range(10):
            print("Q" + str(i+1) + ". " + selectedQuestions.getQuestion(i) + "\n")
            answers = selectedQuestions.getAnswers(i)
            for j in range(4):
                print(str(j+1) + ". " + answers[0][j])
            start = time.time()
            while 1:
                selectedIndexAscii = ord(helpers().getchTrivia())
                if selectedIndexAscii >= 49 and selectedIndexAscii <= 52:
                    selectedIndex = (int(chr(selectedIndexAscii)) - 1)
                    break
                if selectedIndexAscii == 101:
                    gameStats.endGameEarly(i+1)
                    sys.exit()
            end = time.time()
            speed = end - start
            correct = gameScore.getCorrect(answers[1], selectedIndex)
            currentScore = gameScore.calculateScore(correct, speed)
            gameScore.updateScore(currentScore)
            gameStats.record(correct, speed)
            if not speedRun:
                helpers().clearScreen()
                if correct:
                    print("CORRECT +" + str(currentScore) + " points")
                    print("Total Score: " + str(gameScore.getTotalScore()))
                else:
                    print("INCORRECT " + str(currentScore) + " points")
                    print("Correct Answer is: " + selectedQuestions.getCorrectAnswer(i))
                    print("Total Score: " + str(gameScore.getTotalScore()))
                #print(selectedIndex, answers, selectedQuestions.getCorrectAnswer(i))
                print("Press Any Key To Continue")
                helpers().getchTrivia()
                helpers().clearScreen()
            else:
                helpers().clearScreen()
        gameStats.endGameRecord(gameScore.getTotalScore())
        print("Your Final Score is: " + str(gameScore.getTotalScore()))
        print("High Score: " + str(gameStats.getHighScore()))
    elif choice == 50:      ## View statistics screen
        helpers().clearScreen()
        statScreen = statistics(chr(1), chr(1), False)
        if statScreen.checkForData():
            statScreen.initStatScreen()
            timePlayed = int(statScreen.getGameTotals()[0])
            print("Terminal-Trivia Statistics:\n")
            print(helpers().format_string('Current High Score: ' + str(statScreen.getHighScore()), 35) + 'Percent of Questions Correct: ' + '%.2f'%(statScreen.winLoss()) + '%')
            print('\n' + helpers().format_string('Average Response Time: ' + '%.2f'%(statScreen.getAverageses()[0]) + "s", 35) + 'Average Points Per Question: ' + '%.2f'%(statScreen.getAverageses()[1]))
            print(helpers().format_string('Average Game Time: ' +  '%.2f'%(statScreen.getAverageses()[2]) + "s", 35) + 'Average Score Per Game: ' + '%.2f'%(statScreen.getAverageses()[3]))
            print('\n' + helpers().format_string('Total Time Played: ' + str(datetime.timedelta(seconds=timePlayed)), 35) + 'Total Points Gained: ' + str(statScreen.getGameTotals()[1]))
            print(helpers().format_string('Total Questions Answered: ' + str(statScreen.getGameTotals()[2]), 35) + 'Total Games Played: ' + str(statScreen.getGameTotals()[3]))
            print('\n' + 'Most Played Category: ' +  statScreen.getFavoriteInits()[0]) 
            print('Most Played Difficulty: ' + (statScreen.getFavoriteInits()[1]))
            print("\n")
        else:
            print("No data available! Play the game then return.")
    elif choice == 51:      ## View about screen
        helpers().clearScreen()
        print("ABOUT:\n")
        print("terminal-trivia is created with python, and uses the QuizDB database API for all of its questions.")
        print("All game data is collected and stored locally in the homedirectory/astral-kuarry/trivia/data/data.csv.")
        print("Version 1.0.0\n")
    elif choice == 101:
        sys.exit()





introduction = intro()
while 1:
    print("Welcome to terminal-trivia. \n[1] Enter as Guest \n[2] Enter as Admin")
    answer = ord(helpers().getchTrivia())
    if answer == 49:
        introduction.normalIntro()
        break
    elif answer == 50:
        introduction.adminIntro()
        break
    elif answer == 101:
        sys.exit()
while 1:
    runTrivia()
    print("Press e to exit. Press any other key to continue.")
    if ord(helpers().getchTrivia()) == 101:
        break