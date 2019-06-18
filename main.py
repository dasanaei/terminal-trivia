from helpers import helpers
from questions import questions
from score import score
from intro import intro 
import msvcrt
from msvcrt import getch
import time


intro.intro()
while 1:
    choice = intro.menu()
    if (choice >= 49 and choice <= 51) or choice == 101:
        break

speedRun = False  
if choice == 113:
    speedRun = True

if choice == 49 or speedRun:    ## Play the game

    while 1:
        helpers.clearScreen()
        print("Select Category")
        print(" [1] Random Category \n [2] General Knowledge \n [3] Books \n [4] Film \n [5] Musicals/Theater \n [6] Television \n [7] Math \
            \n [8] Geography \n [9] Sports \n [a] History \n [b] Politics \n [c] Art \n [d] Trash \n [f] Japanese Anime and Manga")
        category = ord(getch())
        if (category >= 49 and category <= 57) or (category >= 97 and category <= 100) or category == 102:
            break
        if category == 101:
            quit()
            
    while 1: 
        helpers.clearScreen()
        print("Select Difficulty")
        print(" [1] Easy \n [2] Medium \n [3] Hard")
        difficulty = ord(getch())
        if (difficulty >= 49 and difficulty <= 51):
            break
        if difficulty == 101:
            quit()

    selectedQuestions = questions(chr(category), chr(difficulty))
    gameScore = score()
    print("Press Any Key to Start the Game")
    getch()
    helpers.clearScreen()
    for i in range(10):
        print(selectedQuestions.getQuestion(i))
        answers = selectedQuestions.getAnswers(i)
        for j in range(4):
           print(str(j+1) + ". " + answers[0][j])
        start = time.time()
        while 1:
            selectedIndexAscii = ord(getch())
            if selectedIndexAscii >= 49 and selectedIndexAscii <= 52:
                selectedIndex = int(chr(selectedIndexAscii))
                break
            if selectedIndexAscii == 101:
                quit()
        end = time.time()
        answerTime = end - start
        correct = gameScore.getCorrect(answers[1], selectedIndex)
        currentScore = gameScore.calculateScore(correct, answerTime)
        gameScore.updateScore(currentScore)
        if not speedRun:
            helpers.clearScreen()
            if correct:
                print("CORRECT +" + str(currentScore) + " points")
                print("Total Score: " + str(gameScore.getTotalScore()))
            else:
                print("INCORRECT " + str(currentScore) + " points")
                print("Correct Answer is: " + selectedQuestions.getCorrectAnswer(i))
                print("Total Score: " + str(gameScore.getTotalScore()))
            time.sleep(1)
            helpers.clearScreen()

elif choice == 50:      ## View statistics screen
    print("test1")




elif choice == 51:      ## View about screen
    print("test2")




elif choice == 101:
    quit()































'''
test = msvcrt.getch()
print(test)
'''
