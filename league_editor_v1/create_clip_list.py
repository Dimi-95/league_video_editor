import os
import string
import sys
import tempfile
import time

def create_list_of_clips(amount):
    counter = 0

    while(True):
        if(amount != 0):
            f = open(f"clip_list.txt", "a")
            f.write(f"\nfile 'wip/clips/clip_{counter}.mp4'")
            f.close()
            counter = counter + 1 
            amount = amount - 1
        else:
            print("Clip list got generated !")
            break


