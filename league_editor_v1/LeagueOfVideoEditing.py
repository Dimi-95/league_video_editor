#external libraries
import cv2
import time
import os
from os.path import exists
import customtkinter
from customtkinter import filedialog
from tkinter import filedialog as fidia

#setting the appearance of the window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("700x500")


#internal libraries
import mode
import frame_editor
import logic
import convert_video_codec
import twitch_vod_downloader

#globald variables for ctk
frames                        = 120
seconds_between_clip_points   = 15 #length of clip is double the amount of this
filename                      = "Select a file"

#Setting up CTkinter
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="League Of Video Editing", font=("Roboto", 24))
label.pack(pady=12, padx=10)

#functions
def browseFiles():
    global filename
    tmp = []
    
    filename = filedialog.askopenfilename()
    filename_for_this_function = filename
    filename = '"' + filename + '"'

    for i in range(len(filename_for_this_function)-1, -1, -1):
        if filename_for_this_function[i] == "/":
            break
        else:
            tmp.append(filename_for_this_function[i])

    filename_for_this_function = ''.join(tmp[::-1])

    text_1.configure(state = "normal")
    text_1.insert("0.0", filename_for_this_function)
    text_1.configure(state = "disable")
    
    # Debug:
    # print("This 1: " + filename_for_this_function)
    # print("This 2: " + filename)

def retrieve_input():
    global input
    input = text_2.get("1.0", "end")
    twitch_vod_downloader.download_vod_from_twitch(input)
    #add the functionality of checking if the output file already exists
    
    print(input)


#Buttons
button = customtkinter.CTkButton(master=frame, text="Select MP4 File", command=browseFiles)
button.pack(pady=12, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame, width=200, height=20)
text_1.pack(pady=10, padx=10)

text_2 = customtkinter.CTkTextbox(master=frame, width=500, height=20)
text_2.pack(pady=10, padx=10)

button_tw = customtkinter.CTkButton(master=frame, text="Parse the above text", command=retrieve_input)
button_tw.pack(pady=12, padx=10)

# vod     = "https://www.twitch.tv/videos/1689730808"
# start   = "00:09:10"
# end     = "00:45:15"
# #twitch_vod_downloader.download_vod_from_twitch(vod)

# frame_editor.creating_folders_in_temp()
# the_mode = mode.choose_mode_to_let_the_algorithm_know_what_to_focus_on()
# frame_editor.read_video_and_create_frames(video, frames)
# frame_editor.create_blk_and_wht_images_of_score(frames)

# logic.getting_the_KDAs_and_store_them_in_array(frames)
# logic.event_detection(frames, seconds_between_clip_points, the_mode)
# logic.editing_and_rendering(frames, seconds_between_clip_points, video)
# convert_video_codec.convert_video_to_new_mp4_container()
# frame_editor.removing_folders_and_files_in_temp()
    

 #video = convert_video_codec.convert_video_codec()

root.mainloop()


    







