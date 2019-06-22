from helpers import helpers
from questions import questions
from score import score
from intro import intro 
from statistics import statistics
import msvcrt
from msvcrt import getch
import time
import sys


def runTrivia():
    while 1:
        choice = intro.menu()
        if (choice >= 49 and choice <= 51) or choice == 101 or choice == 113:
            break
    speedRun = False  
    if choice == 113:
        speedRun = True
    if choice == 49 or speedRun:    ## Play the game
        while 1:
            while 1:
                helpers.clearScreen()
                print("Select Category")
                print(" [1] Random Category \n [2] General Knowledge \n [3] Books \n [4] Film \n [5] Musicals/Theater \n [6] Television \n [7] Math \
                    \n [8] Geography \n [9] Sports \n [a] History \n [b] Politics \n [c] Art \n [d] Trash \n [f] Japanese Anime and Manga")
                category = ord(getch())
                if (category >= 49 and category <= 57) or (category >= 97 and category <= 100) or category == 102:
                    break
                if category == 101:
                    sys.exit()     
            while 1: 
                helpers.clearScreen()
                print("Select Difficulty")
                print(" [1] Easy \n [2] Medium \n [3] Hard")
                difficulty = ord(getch())
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
        getch()
        helpers.clearScreen()
        gameStats = statistics(chr(category), chr(difficulty))
        for i in range(10):
            print("Q" + str(i+1) + ". " + selectedQuestions.getQuestion(i) + "\n")
            answers = selectedQuestions.getAnswers(i)
            for j in range(4):
                print(str(j+1) + ". " + answers[0][j])
            start = time.time()
            while 1:
                selectedIndexAscii = ord(getch())
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
                helpers.clearScreen()
                if correct:
                    print("CORRECT +" + str(currentScore) + " points")
                    print("Total Score: " + str(gameScore.getTotalScore()))
                else:
                    print("INCORRECT " + str(currentScore) + " points")
                    print("Correct Answer is: " + selectedQuestions.getCorrectAnswer(i))
                    print("Total Score: " + str(gameScore.getTotalScore()))
                #print(selectedIndex, answers, selectedQuestions.getCorrectAnswer(i))
                print("Press Any Key To Continue")
                getch()
                helpers.clearScreen()
            else:
                helpers.clearScreen()
        gameStats.endGameRecord(gameScore.getTotalScore())
        print("Your Final Score is: " + str(gameScore.getTotalScore()))
        print("High Score: " + str(gameStats.getHighScore()))
        

    elif choice == 50:      ## View statistics screen
        print("test1")




    elif choice == 51:      ## View about screen
        print("test2")




    elif choice == 101:
        sys.exit()






intro.intro()
while 1:
    runTrivia()
    print("Press e to exit. Press any other key to continue.")
    if ord(getch()) == 101:
        break