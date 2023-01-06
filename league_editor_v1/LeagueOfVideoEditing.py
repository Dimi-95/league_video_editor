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
import convert_video_codec
import eel
import twitch_vod_downloader

frames                        = 120
seconds_between_clip_points = 15
#video = fidia.askopenfilename(title="L.O.V.E. (beta version) Choose your VOD")


vod     = "https://www.twitch.tv/videos/1689730808"
start   = "00:09:10"
end     = "00:45:15"

@eel.expose
def download_tw_clip():
    twitch_vod_downloader.download_vod_from_twitch(vod, start, end,)

eel.init(".")
eel.start("main.html", size=(700, 700))


# #FRAME EDITOR
# frame_editor.creating_folders_in_temp()

# #video = convert_video_codec.convert_video_codec()

# #MODE
# mode = mode.choose_mode_to_let_the_algorithm_know_what_to_focus_on()

# frame_editor.read_video_and_create_frames(video, frames)
# frame_editor.create_blk_and_wht_images_of_score(frames)

# logic.getting_the_KDAs_and_store_them_in_array(frames)
# logic.event_detection(frames, seconds_between_clip_points, mode)
# logic.editing_and_rendering(frames, seconds_between_clip_points, video)
# convert_video_codec.convert_video_to_new_mp4_container()
# frame_editor.removing_folders_and_files_in_temp()


    







