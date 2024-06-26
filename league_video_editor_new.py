from pydoc import cli
import cv2
import time
import os
from os.path import exists
import glob
import pytesseract
import subprocess
import number_finder

#Path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
video = "samples/az_2.mp4"
cap = cv2.VideoCapture(video)
fps = cap.get(cv2.CAP_PROP_FPS)
total_num_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
duration_of_clip_in_seconds = total_num_of_frames / fps

count = 0
frames = 120

loading_counter = 0

mode = input("--- CHOOSE MODE --- \n 1 to focus on Kills \n 2 to focus on Deaths \n 3 to focus on Assists \n 4 Smart selection (decides what is best to focus on)\n ENTER: ")
mode = int(mode)

if(mode == 1):
    print("The algorithm will focus on the Kills")
elif(mode == 2):
    print("The algorithm will focus on the Deaths")
elif(mode == 3):
    print("The algorithm will focus on the Assists")
elif(mode == 4):
    print("The algorithm will decide what is best and focus on it")
else:
    mode = 1
    print("Wrong input, mode was set to 1")
    print("The algorithm will focus on the Kills")

start = time.time()

print("READING FRAMES")
while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        cv2.imwrite('frames/frame{:d}.jpg'.format(count), frame)
        count += frames # i.e. at 30 fps, this advances one second
        cap.set(cv2.CAP_PROP_POS_FRAMES, count)
    else:
        end = time.time()
        cap.release()
        print(f"Video is done, it took: {end - start}seconds to finish !")
        splice_and_extract = True
        break

#setting up variables to check if the "change_contrast directory exists or not"
dir_name = "change_contrast"
folder_exists = os.path.isdir(f"C:\\Users\\DimitriosKasderidis\\Desktop\\Editing Software\\{dir_name}")
exist = folder_exists

picture_number= 0
file_exists = exists(f"frames/frame{picture_number}.jpg")
exist_2 = file_exists

start = time.time()
while(True):
    if(exist == False):
        print("No 'change_contrast' Folder detected, new one is being generated")
        os.mkdir(f"C:\\Users\\DimitriosKasderidis\\Desktop\\Editing Software\\{dir_name}")
        exist = True

    if(exist_2):
            image = cv2.imread(f"frames/frame{picture_number}.jpg")

            width  = image.shape[1]
            height = image.shape[0]

            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            focus_in_score = grayImage[0:25, int(width/2)+705:width-180]
            resize = cv2.resize(focus_in_score, (100,50))

            (thresh, black_and_white_image) = cv2.threshold(resize, 118, 255, cv2.THRESH_BINARY )
            cv2.imwrite(f"{dir_name}/bw_frame{picture_number}.jpg", black_and_white_image)
            picture_number = picture_number + frames
            file_exists = exists(f"frames/frame{picture_number}.jpg")
            exist_2 = file_exists


    else:
        end_2 = time.time()
        print(f"Convertion to B&W picture is done, it took: {end_2 - start}seconds to finish !")
        files = glob.glob(f"C:\\Users\\DimitriosKasderidis\\Desktop\\Editing Software\\frames\\*")
        for f in files:
            os.remove(f)
        print("Content of frames folder have been cleared")
        break


picture_number= 0
file_exists = exists(f"change_contrast/bw_frame{picture_number}.jpg")
exist_3 = file_exists
all_kills   = []
all_deaths  = []
all_assists = []


bw_cycle = 0

if(bw_cycle == 0):
    all_kills.append(0)
    all_deaths.append(0)
    all_assists.append(0)
    bw_cycle = bw_cycle + 1

positive_index_number = []
value_tmp = ""

index_counter = 0

#Getting the Kills Deaths Assists stored in arrays respectively
while(True):
    if(exist_3):
        image = cv2.imread(f"change_contrast/bw_frame{picture_number}.jpg")
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

            f = open("debug_KDA.txt" , "a")
            f.write(f"Debug; {kills}/{deaths}/{assists}\n")
            f.close()
            print("Debug: ", kills, deaths, assists)

            all_kills.append(kills)
            all_deaths.append(deaths)
            all_assists.append(assists)
            picture_number = picture_number + frames
            exist_3 = exists(f"change_contrast/bw_frame{picture_number}.jpg")
            pass
        except:
            print("entered the exception")
            all_kills.append(all_kills[-1])
            all_deaths.append(all_deaths[-1])
            all_assists.append(all_assists[-1])
            picture_number = picture_number + frames
            exist_3 = True
            continue

    else:
        print(f"All Kills:   {all_kills}")
        print(f"All Deaths:  {all_deaths}")
        print(f"All Assists: {all_assists}")
        files = glob.glob(f"C:\\Users\\DimitriosKasderidis\\Desktop\\Editing Software\\change_contrast\\*")
        for f in files:
            os.remove(f)
        print("Content of change_contrast folder have been cleared")
        break

#Event detection
seconds = frames/30 #120/30 = 4sec | user defined time = 4sec * the_amount_of_user
user_defined_time      = 5
center_point_of_clip   = 0
starting_point_of_clip = 0
end_point_of_clip      = 0

clip_container = []
begin_to_start = []
length_of_clip = 0

mode_setting = all_kills

if(mode == 1):
    mode_setting = all_kills 
elif(mode == 2):
    mode_setting = all_deaths
elif(mode == 3):
    mode_setting = all_assists
elif(mode == 4):
    if(all_kills[-1] > all_assists[-1]):
        mode_setting = all_kills
    elif(all_kills[-1] > all_assists[-1]):
        mode_setting = all_assists
    else:
        #if they equal
        mode_setting = all_kills


print("Initiating even detection !")
i = 0
condition_counter = len(mode_setting)
#print("Condition Counter: ", condition_counter)
while(True):
    #print("CONDITION COUNTER BEFORE: ", condition_counter)
    if(condition_counter -1 != 0):
        #print("CONDITION COUNTER AFTER: ", condition_counter)
        #print("DEBUG: entering PRE-comparison stage")
        #print("DEBUG: ", i)
        if(mode_setting[i] < mode_setting[i + 1]):
            print("CONDITION COUNTER after detection: ", condition_counter)
            print("DEBUG: entering comparison stage")
            #index + 1 to get the number of the element
            center_point_of_clip   = i + 1
            print("DEBUG: center point: ", center_point_of_clip)
            #the point from which the clip we want starts, defined by the user time
            if(center_point_of_clip-user_defined_time < 0):
                starting_point_of_clip = 0
            else:
                starting_point_of_clip = center_point_of_clip - user_defined_time

            print("DEBUG: starting point: ", starting_point_of_clip)

            if(center_point_of_clip + user_defined_time > len(mode_setting)):
                end_point_of_clip = len(mode_setting)
            else:
                end_point_of_clip = center_point_of_clip + user_defined_time

            print("DEBUG: end point: ", end_point_of_clip)



            #the beginning of the video up to the point the first cut happens
            first_cut = starting_point_of_clip * seconds

            begin_to_start.append(first_cut)
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
        
        #print(f"seconds: {clip_container}")
        print(f"Timestamps and amount of clips -  Timestamps: {begin_to_start} Amount: {len(begin_to_start)}")
        break

amount_of_clips = len(begin_to_start)
clip_counter = amount_of_clips
clip_index = 0
length_of_clip = seconds * user_defined_time

begin_of_game = True
end_of_game = False


print("Amount of clips: ", amount_of_clips)
while(True):
    if(clip_counter != 0):
        print("clip_index", clip_index)
        if(clip_index == 0):
            if(begin_to_start[clip_index] - length_of_clip <= 0):
                starting_time_ffmpeg = "0"
            else:
                starting_time_ffmpeg = str(begin_to_start[clip_index] - length_of_clip)
        else:
            if(begin_to_start[clip_index - 1] + length_of_clip >= (begin_to_start[clip_index] - length_of_clip)):
                starting_time_ffmpeg = str(begin_to_start[clip_index - 1] + length_of_clip)
                print("Clip index: ",clip_index,"  DEBUG IFFFF STATEMENT STARTING TIME: --------------------------- ",starting_time_ffmpeg,"------", begin_to_start[clip_index],"-----" ,length_of_clip)

            else:
                starting_time_ffmpeg = str(begin_to_start[clip_index] - length_of_clip)
            print("Clip index: ",clip_index,"  DEBUG ELSE STATEMENT STARTING TIME: --------------------------- ",starting_time_ffmpeg,"------", begin_to_start[clip_index],"-----" ,length_of_clip)

        


        if(clip_counter == 1):
            print("skip iteration")
            finish_time_ffmpeg   = str(begin_to_start[clip_index] + length_of_clip)
        else:
            finish_time_ffmpeg = str(begin_to_start[clip_index] + length_of_clip)

        times_recording = open("times.txt" , "a")
        times_recording.write(f"Length of clip: {length_of_clip} \n Starting time: {starting_time_ffmpeg}\n Ending time: {finish_time_ffmpeg} \n")
        times_recording.close()

        clip = f"samples/clips/clip_{clip_index}.mp4"
        cmd = ["ffmpeg",
                "-i",
                video,
                "-ss",
                starting_time_ffmpeg,
                "-to",
                finish_time_ffmpeg,
                "-c:v",
                "copy",
                "-c:a",
                "copy",
                clip
                ]


        subprocess.call(cmd)
        clip_index = clip_index + 1
        clip_counter = clip_counter - 1
    else:
        break

    print("break")
time.sleep(2)
os.system(f"python fill_list.py {amount_of_clips}")

final_cmd = ["ffmpeg",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            "clip_list.txt",
            "-c",
            "copy",
            "output_NOW.mp4"]

        
subprocess.call(final_cmd)

files = glob.glob('samples/clips/*')
for f in files:
    os.remove(f)