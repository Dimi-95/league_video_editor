from ctypes import resize
from pydoc import cli
from turtle import width
import cv2
import time
import os
from os.path import exists
import glob
from numpy import concatenate
import pytesseract
import subprocess
import tempfile
import create_clip_list



all_kills   = []
all_deaths  = []
all_assists = []
center_of_clip  = 0
start_of_clip   = 0
end_of_clip     = 0


clip_timestamps = []

def run_ffmpeg_through_cmd(video, starting_time_ffmpeg, finish_time_ffmpeg, clip):
    cmd = ["ffmpeg",
                "-ss",
                starting_time_ffmpeg,
                "-to",
                finish_time_ffmpeg,
                "-i",
                video,
                "-c",
                "copy",
                clip
                ]
    subprocess.call(cmd)


        
def run_ffmpge_through_final_cmd():
    final_cmd_call = ["ffmpeg",
                        "-f",
                        "concat",
                        "-safe",
                        "0",
                        "-i",
                        "clip_list.txt",
                        "-c",
                        "copy",
                        "output.mp4"]

    subprocess.call(final_cmd_call)


def getting_the_KDAs_and_store_them_in_array(frames):
    pytesseract.pytesseract.tesseract_cmd = r'dependencies\Tesseract-OCR\tesseract.exe'
    image_number = 0
    bw_image_exists = exists(f"wip\\bw_frames\\bw_frame_{image_number}.jpg")
    bw_image_check  = bw_image_exists

    cycle            = 0
    new_game_counter = 0

    if(cycle == 0):
        all_kills.append(0)
        all_deaths.append(0)
        all_assists.append(0)
        cycle = cycle + 1

    while(True):
        if(bw_image_check):
            image = cv2.imread(f"wip\\bw_frames\\bw_frame_{image_number}.jpg")
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

                #debug_kda_to_txt_file(kills, deaths, assists)

                all_kills.append(kills)
                all_deaths.append(deaths)
                all_assists.append(assists)
                image_number = image_number + frames
                bw_image_check = exists(f"wip\\bw_frames\\bw_frame_{image_number}.jpg")
                pass
            except:
                #if(new_game_counter == 30):
                all_kills.append(0)
                all_deaths.append(0)
                all_assists.append(0)
                #new_game_counter = 0

                print("Debug: Faulty Image Detected and Ignored")
                all_kills.append(all_kills[-1])
                all_deaths.append(all_deaths[-1])
                all_assists.append(all_assists[-1])
                image_number = image_number + frames
                bw_image_check = True
                #new_game_counter = new_game_counter + 1
                continue
        else:
            print(f"All Kills:   {all_kills}")
            print(f"All Deaths:  {all_deaths}")
            print(f"All Assists: {all_assists}")
            break

def event_detection(frames, interval_of_seconds, mode):
    seconds         = frames/30
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
                if((center_of_clip * seconds) - interval_of_seconds < 0):
                    start_of_clip = 0
                else:
                    start_of_clip = (center_of_clip * seconds) - interval_of_seconds

                #print("DEBUG: starting point: ", start_of_clip)



                #the beginning of the video up to the point the first cut happens
                first_cut = start_of_clip + interval_of_seconds

                clip_timestamps.append(first_cut)
                
                i = i + 1
                condition_counter = condition_counter - 1


            else:
                i = i + 1
                condition_counter = condition_counter - 1
        else:
                print("event detection over")
                print(f"Timestamps and amount of clips -  Timestamps: {clip_timestamps} Amount: {len(clip_timestamps)}")
                break


def editing_and_rendering(frames, interval_of_seconds, video):
    seconds      = frames/30
    clip_counter = len(clip_timestamps)
    clip_index   = 0
    final_render = False

    print(f"Amount of existing clips: {clip_counter}")

    finish_time_fmpeg = "0"

    while(True):
        #Starting Clip
        if(clip_counter != 0):
            if(clip_index == 0):
                    starting_time_ffmpeg = "0"
            else:
                if(float(finish_time_fmpeg) >= (clip_timestamps[clip_index] - interval_of_seconds)):
                    starting_time_ffmpeg = finish_time_fmpeg
                else:
                    starting_time_ffmpeg = str(clip_timestamps[clip_index] - interval_of_seconds)

            #Finishing Clip
            if(clip_index == 0):
                finish_time_fmpeg = "15"
            else:
                finish_time_fmpeg = str(clip_timestamps[clip_index] + interval_of_seconds)
                    
            
            #debug_times_recording_to_txt_file(clip_length, starting_time_ffmpeg, finish_time_fmpeg)

            clip = f"wip/clips/clip_{clip_index}.mp4"

            run_ffmpeg_through_cmd(video, starting_time_ffmpeg, finish_time_fmpeg, clip)
            clip_index   = clip_index + 1
            clip_counter = clip_counter - 1
        else:
            break

    final_render = True
    create_clip_list.create_list_of_clips(len(clip_timestamps))
    run_ffmpge_through_final_cmd()