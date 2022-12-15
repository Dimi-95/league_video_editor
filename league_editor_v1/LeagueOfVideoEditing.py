#external libraries
import cv2
import time
import os
from os.path import exists
import glob
import pytesseract
import subprocess
from tkinter import filedialog as fidia

#internal libraries
import mode
import frame_editor
import logic

frames                        = 120
video                         =  fidia.askopenfilename(title="L.O.V.E. (beta version) Choose your VOD")
seconds_between_clip_points = 15

if __name__ == "__main__":
    #FRAME EDITOR
    frame_editor.creating_folders_in_temp()
    
    
    #MODE
    mode = mode.choose_mode_to_let_the_algorithm_know_what_to_focus_on()

    frame_editor.read_video_and_create_frames(video, frames)
    frame_editor.create_blk_and_wht_images_of_score(frames)

    logic.getting_the_KDAs_and_store_them_in_array(frames)
    logic.event_detection(frames, seconds_between_clip_points, mode)
    logic.editing_and_rendering(frames, seconds_between_clip_points, video)
    frame_editor.removing_folders_in_temp()







