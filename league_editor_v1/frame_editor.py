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


def creating_folders_in_temp():
    frames_existence    = os.path.isdir(f"frames")
    bw_frames_existence = os.path.isdir(f"bw_frames")
    clips_existence     = os.path.isdir(f"clips")


    print("---")
    if(bw_frames_existence == False):
        print(f"Folder 'bw_frames' has been created.")
        os.mkdir(f"bw_frames")
    else:
        print(f"Folder 'bw_frames' exists already.")

    if(frames_existence == False):
        print(f"Folder 'frames' has been created.")
        os.mkdir(f"frames")
    else:
        print(f"Folder 'frames' exists already.")

    if(clips_existence == False):
        print(f"Folder 'clips' has been created.")
        os.mkdir(f"clips")
    else:
        print(f"Folder 'clips' exists already.")
    print("---")
    print("\n")


def removing_folders_in_temp():
        print("---")
        files = glob.glob(f"frames\\*")
        for f in files:
            os.remove(f)
        os.rmdir(f"frames")
        print("Folder 'frames' has been removed")

        files = glob.glob(f"bw_frames\\*")
        for f in files:
            os.remove(f)
        os.rmdir(f"bw_frames")
        print("Folder 'bw_frames' has been removed")

        files = glob.glob(f"clips\\*")
        for f in files:
            os.remove(f)
        os.rmdir(f"clips")
        print("Folder 'clips' has been removed")

        os.remove("clip_list.txt")
        

def read_video_and_create_frames(video_path, frames):
    cap = cv2.VideoCapture(video_path)
    count = 0
    print("Frames are being generated... please wait")

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            cv2.imwrite(f"frames\\frame_{count}.jpg", frame)
            count += frames
            cap.set(cv2.CAP_PROP_POS_FRAMES, count)
        else:
            print("Frames have been generated successfully")
            break

def create_blk_and_wht_images_of_score(frames):
    image_number = 0
    keep_going   = True
    print("Black and White images of the score are being generated... please wait")

    while(True):

        if(keep_going):        
            image = cv2.imread(f"frames\\frame_{image_number}.jpg")
            
            width  = image.shape[1]
            height = image.shape[0]


            gray_image      = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            focus_on_score  = gray_image[0:25, int(width/2)+705:width-180]
            resize          = cv2.resize(focus_on_score, (100,50))

            (thresh, black_and_white_image) = cv2.threshold(resize, 118, 255, cv2.THRESH_BINARY )
            cv2.imwrite(f"bw_frames\\bw_frame_{image_number}.jpg", black_and_white_image)
            image_number                    = image_number + frames
            keep_going_check                = exists(f"frames\\frame_{image_number}.jpg")
            keep_going                      = keep_going_check
        else:
            print("Black and White images of the score have been generated")
            break






    