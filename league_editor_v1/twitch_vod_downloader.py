import subprocess

def download_vod_from_twitch(vod):
    cmd =["twitch-dl",
            "download",
            "-s",
            "00:00:00",
            "-e",
            "00:05:00",
            vod,
            "-q",
            "1080p",
            "-o",
            "tw_download.mp4"
            ]
    subprocess.call(cmd)
