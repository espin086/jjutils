#!/usr/bin/env bash
import glob
# import email_util
import json
import os
import sys


def download_playlist(playlists, mydirectory):
    """
    Downloads playlist from YouTube and saves them in a specified directory

    Creates a folder with the name of the playlist and saves videos from playlist there.
    Also has built in command that skips unavailable videos so program doesn't crash,
    or other errors in downloading the file, can use logging to mine this data for pattersn.

    ARGS:
        playlists (list): a list of playlist urls from YouTube
        mydirectory (string): a string representing a local direcotry to download files, must end in backslash

    RETURNS:
        None

    EXAMPLE

    urls = ['https://www.youtube.com/myplaylist']
    download_playlist(urls, '../videos/raw_videos')

    """

    for videos in playlists:
        directory = "{0}%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s".format(
            mydirectory
        )
        os.system(
            'youtube-dl --format mp4 --ignore-errors --write-info-json --download-archive ../logs/archive.txt -o "{0}" {1}'.format(
                directory, videos
            )
        )

    # deleting last logfile so new one can be created

    return None


def gcs_uploader():
    """
    Uploads latest trailer videos to Google Cloud

    """
    # copying only updated folder from these buckets into the raw folder
    for folder in [
        "20th\ Century\ Fox\ Trailers",
        "HOT\ New\ Trailers\ \&\ Movieclips\ Exclusives",
        "Sony\ Pictures\ -\ Official\ Trailers",
        "TRAILERS",
        "Universal\ Pictures\ -\ Trailers",
        "Uploads\ from\ Paramount\ Pictures",
        "Uploads\ from\ Walt\ Disney\ Studios",
    ]:
        print("INFO: folder to move data from {0}".format(folder))
        # --update only copies latest files
        os.system(
            "cp --update ~/cronjob/merlin_ops/video_embedding/videos/raw_videos/{0}/* ~/cronjob/merlin_ops/video_embedding/videos/raw_videos/raw_videos".format(
                folder
            )
        )
    # copy all files in raw videos to raw_video in cloud storage
    os.system(
        "gsutil -m cp -n ~/cronjob/merlin_ops/video_embedding/videos/raw_videos/raw_videos/* gs://merlin-video/input/raw_videos"
    )

    return None


if __name__ == "__main__":
    # this changes the current file path the the file path of the python package, makes it easier to run CRONJOBS
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    urls = {
        "official_fox": "https://www.youtube.com/playlist?list=PLfPBohF1uFwoO5wBnYD67i0pbZ6GqrGEd",
        "official_disney": "https://www.youtube.com/playlist?list=UUuaFvcY4MhZY3U43mMt1dYQ",
        "official_warner": "https://www.youtube.com/playlist?list=PLVfin74Qx3tV8bgAhzbfDpnfPoGmJWAcn",
        "official_universal": "https://www.youtube.com/playlist?list=PLuq_rgCzEP_NBRjFMklzlMaFajjyV-OoL",
        "official_paramount": "https://www.youtube.com/playlist?list=UUF9imwPMSGz4Vq1NiTWCC7g",
        "official_sony": "https://www.youtube.com/playlist?list=PLYeOyMz9C9kYmnPHfw5-ItOxYBiMG4amq",
        "official_fandando": "https://www.youtube.com/playlist?list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-",
    }

    urls_list = list(urls.values())
    download_playlist(urls_list, "../videos/raw_videos/")
    gcs_uploader()
