#external libraries
from pydoc import cli
import cv2
import time
import os
from os.path import exists
import glob
import pytesseract
import subprocess

#internal libraries
import mode
import frame_editor
import logic


if __name__ == "__main__":
    ##MODE
    # mode = mode.choose_mode_to_let_the_algorithm_know_what_to_focus_on()
    # print(mode)

    #FRAME EDITOR
    frame_editor.creating_folders_in_temp()
    #frame_editor.removing_folders_in_temp()

    frame_editor.read_video_and_create_frames("video_sample_folder\\small_test.mp4", 30)
    frame_editor.create_blk_and_wht_images_of_score(30)

    logic.getting_the_KDAs_and_store_them_in_array(30)








