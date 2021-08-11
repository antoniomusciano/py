from pynput.keyboard import Key, Controller
import random
import time


def auto(saying):
    keyboard = Controller()
    keyboard.type(saying)
    keyboard.press(Key.enter)
    snooze = random.randint(5, 8)
    time.sleep(snooze)


if __name__ == '__main__':
    time.sleep(10)
    while True:
        string = "$fish"
        auto(string)
