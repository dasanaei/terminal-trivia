from helpers import helpers
from intro import intro 
import msvcrt
from msvcrt import getch


intro.intro()
while 1:
    choice = intro.menu()
    break
    if (choice >= 49 and choice <= 51) or choice == 101:
        break
        


if choice == 49:    ## Play the game
    print("test")




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
