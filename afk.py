from time import sleep
import sys
import keyboard 
import random
import pyautogui 
import threading
def main():

    print('\nTo Stop AFK BOT Press Q for 3 sec')
    print('By Swe2ty')
    print()
    sleep(4)
    try:
        focusOnValorant()
        global bot_flag 
        bot_flag = True
        t1 = threading.Thread(target = no_afk ) 
        t1.start()
        while bot_flag == True:
            sleep(3)
            if keyboard.is_pressed('q'):
                bot_flag = False
                return       
    except:
        print()

    print('Bot Stoped!')

def focusOnValorant():
    list = pyautogui.getWindowsWithTitle('VALORANT')
    if len(list) == 0 :
        print('\nOpen Valorant')
        print('Bot Stoped!',end='')
        for i in range(4):
            sleep(1)
            print('. ',end='')
        sys.exit()
    else: 
        valorant = list[0]
        if valorant.isMinimized == True:
            valorant.restore()


def no_afk():
    sleep(0.5)
    while bot_flag == True:
        choice = random.randint(1,9)
        sleeptime = random.randint(1,2)
        if choice == 1:
            keyboard.press('w')
            sleep(sleeptime)
            keyboard.release('w')
        elif choice == 3:
            keyboard.press('k')
            sleep(sleeptime)
            keyboard.release('k')
        elif choice == 4:
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('a')
        elif choice == 5:
            keyboard.press('s')
            sleep(sleeptime)
            keyboard.release('s')
        elif choice == 6:
            keyboard.press('d')
            sleep(sleeptime)
            keyboard.release('d')
        elif choice == 7:
            keyboard.press('space')
            sleep(sleeptime)
            keyboard.release('space')
        elif choice == 8:
            keyboard.press('control')
            sleep(sleeptime)
            keyboard.release('control')   
        elif choice == 9:
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('a')
        elif choice == 10:
            keyboard.press('k')
            sleep(sleeptime)
            keyboard.release('k')
        elif choice == 11:
            keyboard.press('k')
            sleep(sleeptime)
            keyboard.release('k')
        elif choice == 12:
            keyboard.press_and_release('enter')
            sleep(1)
            pyautogui.typewrite(' LOL :)')
            sleep(2)
            keyboard.press_and_release('enter')
        elif choice == 13:
            keyboard.press_and_release('enter')
            sleep(1)
            pyautogui.typewrite(' LOL :)')
            sleep(2)
            keyboard.press_and_release('enter')
        elif choice == 14:
            keyboard.press_and_release('enter')
            sleep(1)
            pyautogui.typewrite('sorry am new')
            sleep(2)
            keyboard.press_and_release('enter')
        elif choice == 15:
            screen_width, screen_height = pyautogui.size()
            x_pos = random.randint(0, screen_width)
            y_pos = random.randint(0, screen_height)
            pyautogui.moveTo(x_pos, y_pos, duration=0.1)
        elif choice == 16:
            keyboard.press('e')
            sleep(sleeptime)
            keyboard.release('e')
        elif choice == 17:
            keyboard.press('e')
            sleep(sleeptime)
            keyboard.release('e')
        elif choice == 18:
            keyboard.press('r')
            sleep(sleeptime)
            keyboard.release('r')

if __name__ == "__main__":
    main()