#! /usr/bin/env python3

"""
https://pytube.io/en/latest/
https://github.com/pytube/pytube
https://www.thepythoncode.com/article/make-a-youtube-video-downloader-in-python

só funciona até o python 3.9
colocar barra de progresso no programa na interface de CLI
Fazer uma GUI
Fazer uma interface via Web
"""

from pytube import YouTube
from sys import argv
from time import sleep


def GUI():
    # Building GUI
    pass


def set_resolution():
    pass


def L_download():
        # Donwload in list or playlist
    pass


def B_download(url_video):
    # Basic download
    yt = YouTube(url_video)
    yt.streams.get_highest_resolution().download()
    return yt.title


if __name__ == "__main__":
    try:
        # CLI (Done)
        video_d = argv[1]
        print("\n[+]:Downloading your Video, please wait.........")
        sleep(2)
        video_d2 = B_download(video_d)
        sleep(2)
        print(f'"[*]:{video_d2}" downloaded successfully!!')
    except:
        print('Use example: python3 DownTube.py "[YOUTUBE URL]"')