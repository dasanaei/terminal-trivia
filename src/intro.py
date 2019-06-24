from helpers import helpers
import time


class intro():
    def intro(self):
        helpers().clearScreen()
        print("                                                           ")
        print("                                                           ")
        print("                                                           ")
        print("                      ``........``                         ")
        print("                   `.---------------.`                     ")
        print("                `.------..`.o``..------.`                  ")
        print("              `.----.`    `dMy     `.----.                 ")
        print("             `----.      .mMMMh`     `.----`               ")
        print("            `----`      .mMm/NMd`      .----               ")
        print("            ----`      -NMh` .mMd`      .---.              ")
        print("           `----      :NMy    `dMm.      ----              ")
        print("           `---.     /MMo      `hMN-     ----`             ")
        print("           `----    +MM/         sMN:    ----              ")
        print("            ----`  oMMy///////////dMM/  .---.              ")
        print("            `----`sMMMMMMMMMMMMMMMMMMM/.----``````         ")
        print("             `----.                   .sMMMMMMMMM/         ")
        print("              `-----.`             `.---/mMo +MM:          ")
        print("                `------..```````..-----.``yMmMN:           ")
        print("                  `.----------------..`    /NN-            ")
        print("                      ``....-....``         ..             ")
        print("                                                           ")      
        print("                                                           ")
        print("                                                           ")
        print("                WELCOME TO TERMINAL TRIVIA                 ")
        time.sleep(2)

    def menu(self):
        helpers().clearScreen()
        print("Please select one of the following options:")
        print("[1] Start Trivia")
        print("[2] View Statistics")
        print("[3] About")
        print("[q] Speed Run")
        print("[e] Exit")
        return ord(helpers().getchTrivia())
        