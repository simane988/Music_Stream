import sys
import os
import colorama
from src import files_work


# Block that clear terminal and draw "hello picture"
def clear():
    os.system('clear')
    hello_pic()


# First choose block
def choose_action():
    run = True
    while run:
        print("Choose part: \n"
              "1 System\n"
              "2 Working with files\n"
              "3 Exit\n")
        flag = int(input())
        if flag == 1:
            clear()
            system_part()
            run = False
        elif flag == 2:
            clear()
            working_part()
            run = False
        elif flag == 3:
            exit_part()
            run = False
        else:
            clear()
            print("Incorrect input, try one more time!")


def system_part():
    run = True
    while run:
        print("Choose part: \n"
              "1 Start stream\n"
              "2 Config\n"
              "3 Back\n")
        flag = int(input())
        if flag == 1:
            clear()
            system_part()
            run = False
        elif flag == 2:
            clear()
            config_part()
            run = False
        elif flag == 3:
            clear()
            choose_action()
            run = False
        else:
            clear()
            print("Incorrect input, try one more time!")


def working_part():
    run = True
    while run:
        print("Choose part: \n"
              "1 Start stream\n"
              "2 Config\n"
              "3 Back\n")
        flag = int(input())
        if flag == 1:
            clear()
            system_part()
            run = False
        elif flag == 2:
            clear()
            config_part()
            run = False
        elif flag == 3:
            clear()
            choose_action()
            run = False
        else:
            clear()
            print("Incorrect input, try one more time!")


def config_part():
    run = True
    while run:
        print("Choose part: \n"
              "1 Change video config\n"
              "2 Change paths config\n"
              "3 Reset to factory settings\n"
              "4 Back\n")
        flag = int(input())
        if flag == 1:
            clear()
            system_part()
            run = False
        elif flag == 2:
            clear()
            config_part()
            run = False
        elif flag == 3:
            clear()
            config_part()
            run = False
        elif flag == 4:
            clear()
            choose_action()
            run = False
        else:
            clear()
            print("Incorrect input, try one more time!")


def start_part():
    print('Start')


def exit_part():
    os.system('clear')
    sys.exit()


def hello_pic():
    text = r"""
  __  __           _          _____ _                                _____             __ _       
 |  \/  |         (_)        / ____| |                              / ____|           / _(_)      
 | \  / |_   _ ___ _  ___   | (___ | |_ _ __ ___  __ _ _ __ ___    | |     ___  _ __ | |_ _  __ _ 
 | |\/| | | | / __| |/ __|   \___ \| __| '__/ _ \/ _` | '_ ` _ \   | |    / _ \| '_ \|  _| |/ _` |
 | |  | | |_| \__ \ | (__    ____) | |_| | |  __/ (_| | | | | | |  | |___| (_) | | | | | | | (_| |
 |_|  |_|\__,_|___/_|\___|  |_____/ \__|_|  \___|\__,_|_| |_| |_|   \_____\___/|_| |_|_| |_|\__, |
                                                                                             __/ |
                                                                                            |___/ 
    """
    print(text)


def main():
    colorama.init()
    print(colorama.Fore.GREEN)
    clear()
    choose_action()


if __name__ == "__main__":
    main()
