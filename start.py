import time
import colorama


def choose_action():
    run = True
    while run:
        colorama.init()
        print(colorama.Fore.GREEN)
        print("Choose part: \n"
              "1 Working with files \n"
              "2 Config \n"
              "0 System")
        flag = int(input())
        if flag == 1:
            working_part()
            run = False
        elif flag == 2:
            config_part()
            run = False
        elif flag == 0:
            system_part()
            run = False
        else:
            print("Incorrect input, try one more time!")
    print(colorama.Style.RESET_ALL)


def working_part():
    pass


def config_part():
    pass


def system_part():
    pass


def hello_pic():
    colorama.init()
    time.sleep(0.2)
    print(colorama.Fore.GREEN)
    print(r" _        __ _         _                                                 __ _       ")
    time.sleep(0.2)
    print(r"| |      / _(_)       | |                                               / _(_)      ")
    time.sleep(0.2)
    print(r"| | ___ | |_ _     ___| |_ _ __ ___  __ _ _ __ ___       ___ ___  _ __ | |_ _  __ _ ")
    time.sleep(0.2)
    print(r"| |/ _ \|  _| |   / __| __| '__/ _ \/ _` | '_ ` _ \     / __/ _ \| '_ \|  _| |/ _` |")
    time.sleep(0.2)
    print(r"| | (_) | | | |   \__ \ |_| | |  __/ (_| | | | | | |   | (_| (_) | | | | | | | (_| |")
    time.sleep(0.2)
    print(r"|_|\___/|_| |_|   |___/\__|_|  \___|\__,_|_| |_| |_|    \___\___/|_| |_|_| |_|\__, |")
    time.sleep(0.2)
    print(r"                                                                               __/ |")
    time.sleep(0.2)
    print(r"                                                                              |___/ ")
    time.sleep(0.2)
    print(colorama.Style.RESET_ALL)


def main():
    hello_pic()
    choose_action()


if __name__ == "__main__":
    main()
