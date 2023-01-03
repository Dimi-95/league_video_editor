import subprocess

def download_vod_from_twitch(vod, start, end):
    cmd =["twitch-dl",
            "download",
            "-s",
            start,
            "-e",
            end,
            vod,
            "-q",
            "source",
            "-o",
            "tw_download.mp4"
            ]
    subprocess.call(cmd)