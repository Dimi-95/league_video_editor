import subprocess
from tkinter import filedialog as fidia




def convert_video_codec ():

    video = fidia.askopenfilename(title="L.O.V.E. (beta version) Choose your VOD")
    print("Would you like to convert your Video file to ffmpegs Video Codec ? \n This is not a necessity but solves incompatibility issues")

    check = int(input("Enter 1 for 'yes' 2 for 'no': "))

    if( check == 1):
        cmd = ["ffmpeg",
                    "-i",
                    video,
                    "-preset",
                    "ultrafast",
                    "wip/clips/converted_video.mp4"
                    ]
        subprocess.call(cmd)
        video = "wip/clips/converted_video.mp4"
        return video
    else:
        return video