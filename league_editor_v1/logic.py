from ctypes import resize
from pydoc import cli
from turtle import width
import cv2
import time
import os
from os.path import exists
import glob
import pytesseract
import subprocess
import tempfile

all_kills   = []
all_deaths  = []
all_assists = []

def debug_kda_to_txt_file(kills, deaths, assists):
    f = open("debug_KDA.txt" , "a")
    f.write(f"Debug: {kills}/{deaths}/{assists}\n")
    f.close()
    print("Debug: ", kills, deaths, assists)


def getting_the_KDAs_and_store_them_in_array(frames):
    pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"
    image_number = 0
    bw_image_exists = exists(f"{tempfile.gettempdir()}\\bw_frames\\bw_frame_{image_number}.jpg")
    bw_image_check  = bw_image_exists

    cycle       = 0

    if(cycle == 0):
        all_kills.append(0)
        all_deaths.append(0)
        all_assists.append(0)
        cycle = cycle + 1

    while(True):
        if(bw_image_check):
            image = cv2.imread(f"{tempfile.gettempdir()}\\bw_frames\\bw_frame_{image_number}.jpg")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            data = pytesseract.image_to_data(image)

            for x,b in enumerate(data.splitlines()):
                if x != 0:
                    b = b.split()
                    if len(b) == 12:
                        #value is a string
                        value = b[11]
                        value = value.split("/")

            try: 
                if(all_kills[-1] > int(value[0])):
                    kills = all_kills[-1]
                else:
                    kills = int(value[0])

                if(all_deaths[-1] > int(value[1])):
                    deaths = all_deaths[-1]
                else:
                    deaths = int(value[1])

                if(all_assists[-1] > int(value[2])):
                    assists = all_assists[-1]
                else:
                    assists = int(value[2])

                debug_kda_to_txt_file(kills, deaths, assists)

                all_kills.append(kills)
                all_deaths.append(deaths)
                all_assists.append(assists)
                image_number = image_number + frames
                bw_image_check = exists(f"change_contrast/bw_frame{image_number}.jpg")
                pass
            except:
                print("Faulty Image Detected and Ignored")
                all_kills.append(all_kills[-1])
                all_deaths.append(all_deaths[-1])
                all_assists.append(all_assists[-1])
                image_number = image_number + frames
                bw_image_check = True
                continue
        else:
            print(f"All Kills:   {all_kills}")
            print(f"All Deaths:  {all_deaths}")
            print(f"All Assists: {all_assists}")
            break

def event_detection(frames, interval_of_seconds, mode):
    seconds         = frames/30
    center_of_clip  = 0
    start_of_clip   = 0
    end_of_clip     = 0

    clip_timestamps = []
    clip_length     = []

    set_mode = mode
    i = 0

    if(mode == 1):
        set_mode = all_kills 
    elif(mode == 2):
        set_mode = all_deaths
    elif(mode == 3):
        set_mode = all_assists
    elif(mode == 4):
        if(all_kills[-1] > all_assists[-1]):
            set_mode = all_kills
        elif(all_kills[-1] > all_assists[-1]):
            set_mode = all_assists
        else:
            set_mode = all_kills

    condition_counter = len(set_mode)
    while(True):
        if(condition_counter -1 !=0):

            if(set_mode[i] < set_mode[i + 1]):
                center_of_clip   = i + 1
                if(center_of_clip - interval_of_seconds < 0):
                    start_of_clip = 0
                else:
                    start_of_clip = center_of_clip - interval_of_seconds

                print("DEBUG: starting point: ", start_of_clip)

                if(center_of_clip + interval_of_seconds > len(set_mode)):
                    end_of_clip = len(set_mode)
                else:
                    end_of_clip = center_of_clip + interval_of_seconds

                print("DEBUG: end point: ", end_of_clip)



                #the beginning of the video up to the point the first cut happens
                first_cut = start_of_clip * seconds

                clip_timestamps.append(first_cut)
                c = open("first_cut.txt", "a")
                c.write(f"--- {first_cut} ---\n")
                c.close()


                i = i + 1
                condition_counter = condition_counter - 1


            else:
                i = i + 1
                condition_counter = condition_counter - 1
        else:
                print("event detection over")
                print(f"Timestamps and amount of clips -  Timestamps: {clip_timestamps} Amount: {len(clip_timestamps)}")
                break



