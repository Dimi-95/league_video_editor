import subprocess

def download_vod_from_twitch(vod):
    cmd =["twitch-dl",
            "download",
            vod,
            "-q",
            "source",
            "-o",
            "tw_download.mp4"
            ]
    subprocess.call(cmd)