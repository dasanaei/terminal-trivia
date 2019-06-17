from helpers import helpers
from questions import questions
from intro import intro 
import msvcrt, time
from msvcrt import getch


intro.intro()
while 1:
    choice = intro.menu()
    if (choice >= 49 and choice <= 51) or choice == 101:
        break
        


if choice == 49:    ## Play the game

    while 1:
        helpers.clearScreen()
        print("Select Category")
        print(" [1] Random Category \n [2] General Knowledge \n [3] Books \n [4] Film \n [5] Musicals/Theater \n [6] Television \n [7] Math \n [8] Geography \n [9] Sports \n [a] History \n [b] Politics \n [c] Art \n [d] Trash \n [f] Japanese Anime and Manga")
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
