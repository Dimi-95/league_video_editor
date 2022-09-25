from pydoc import cli
import cv2
import time
import os
from os.path import exists
import glob
import pytesseract
import subprocess

def choose_mode_to_let_the_algorithm_know_what_to_focus_on():
    input_mode = input("--- CHOOSE MODE --- \n 1) to focus on Kills \n 2) to focus on Deaths \n 3) to focus on Assists \n 4) Smart selection (decides what is best to focus on)\n ENTER: ")    
    choosen_mode = int(input_mode)

    if(choosen_mode == 1):
        print("\nThe algorithm will focus on the Kills")
    elif(choosen_mode == 2):
        print("\nThe algorithm will focus on the Deaths")
    elif(choosen_mode == 3):
        print("\nThe algorithm will focus on the Assists")
    elif(choosen_mode == 4):
        print("\nThe algorithm will decide what is best and focus on it")
    else:
        choosen_mode = 1
        print("Wrong input, mode was set to 1")
        print("The algorithm will focus on the Kills")


    return choosen_mode

