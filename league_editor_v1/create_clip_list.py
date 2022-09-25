import os
import string
import sys
import tempfile
import time


path = f"{tempfile.gettempdir()}\\clips"

string_begin = "( "


def create_list_of_clips(amount):
    counter = 0
    the_list  = ""
    while(True):
        if(amount != 0):
            if(amount == 1):
                temp_string = f"echo file '{tempfile.gettempdir()}\\clips\\clip_{counter}.mp4' )>list.txt"
                the_list = the_list + temp_string
            else:
                temp_string = f"echo file {tempfile.gettempdir()}\\clips\\clip_{counter}.mp4 &"
                the_list = the_list + temp_string
                counter = counter + 1 
                amount = amount - 1
        else:
            print("Clips got generated !")
        break
    the_list = string_begin + the_list
    print(the_list, "--------------------------------------------------------------")
    return the_list

