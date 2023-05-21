import pyautogui
import random

keyboard = "1234567890qwertyuiopasdfghjklzxcvbnm@!+=;></"
keyboard_list = list(keyboard)

password = pyautogui.password("Your Password: ")
guess_password = ''

while (guess_password != password):
    guess_password = random.choice(keyboard_list, k = len(password))
    print(str(guess_password))

    if (guess_password == list(password)):
        print("Your Password is: " + "".join(guess_password))
        