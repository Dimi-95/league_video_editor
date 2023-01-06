import subprocess
import eel

@eel.expose
def download_vod_from_twitch(vod, start, end):
    cmd =["twitch-dl",
            "download",
            "-s",
            start,
            "-e",
            end,
            vod,
            "-q",
            "1080p",
            "-o",
            "tw_download.mp4"
            ]
    subprocess.call(cmd)

@eel.expose
def hello():
        print("Hello")