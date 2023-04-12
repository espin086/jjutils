"""
SUMMARY: Creates frame level embeddings of mp4 videos

Author: JJ Espinoza
Created: 2018/08/24

Last Modified: 2018/09/10
Modified By: JJ Espinoza


This code incrementally embeeds videos at the frame level.
Either one frame per second or every frame. 


Example 1: this will create a 1-frame-per-second embedding ('1)
    after downloading the latest mp4 files.

    $ python create_frame_embeddings.py 1 yes

Example 2: same as example 1, but will use existing mp4 files.
    $ python create_frame_embeddings.py 1 no




"""




import sys
import os
import os.path
import numpy
import pandas as pd
import cv2
from PIL import Image, ImageFile
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import create_video_embeddings
from feature_extractor import YouTube8MFeatureExtractor
import argparse
import warnings
import frame_labeler

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

extractor = YouTube8MFeatureExtractor()


#os.chdir("~/source-repository/merlin_video/video_embedding/code")

print('Current Working Directory: {}'.format(os.getcwd()))
def extract_frames(video):
    vidcap = cv2.VideoCapture('../videos/clean_videos/{}.mp4'.format(video))
    print(type(vidcap))
    success, image = vidcap.read()
    print('First success: {}'.format(success))
    count = 0
    success = True

    directory = '../frames/{0}'.format(video)
    os.makedirs(directory)
    while success:
        cv2.imwrite('../frames/{0}/frame{1}.jpg'.format(video, count), image)
        success, image = vidcap.read()
        print('Extracting frame {0}: {1}'.format(count, video))
        count += 1
    return None

#downloads latest Merlin synopses lookup table
def download_lookup_tables(timeframe):
    """
    Downloadas latest lookup table 

    Can download the entire table or a shortened list
    based off of the incremetnal formula.

    Args:
    -----------------------------------------
    timeframe (string): 'all' or 'incremental'

    Returns:
    ----------------------------------------
    look_up_dict (dictionary): a dictionary of movie(key) and movie_id(value)

    """
    #Tables that need to be downloaded regardless of the filtering happening
    create_video_embeddings.get_merlin_synopses_table()
    look_up_df = pd.read_csv('../lookup_tables/merlin_synopses.csv')
    trailer_tracker = create_video_embeddings.get_trailer_tracker_table()
    incremental = pd.read_csv('../lookup_tables/vid_dataset_incremental.csv')
    incremental.columns = ['file_path', 'id_for_embedding']
    incremental = incremental['file_path'].str.replace('/home/jj_espinoza/cronjob/merlin_ops/video_embedding/videos/clean_videos/','')
    incremental = list(incremental.str.replace('.mp4',''))

    look_up_dict = dict(zip(list(look_up_df['movie']),list(look_up_df['movie_id'])))

    if timeframe == 'incremental':
        look_up_dict = dict((k, look_up_dict[k]) for k in incremental if k in look_up_dict)
    elif timeframe == 'all':
        look_up_dict = look_up_dict

    return look_up_dict

def embed_frames(video, frames_per_second, lookup):
    directory = '../frames/{0}'.format(video)
    print("INFO: trying to embeed ferames located in: {0}".format(directory))
    #counting the total number of frame in a directory and saving as a number called 'frames'
    frames = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
    print("INFO: number of frames in directory is {0}".format(frames))
    embedded_video = [] 
    
    if frames_per_second == 1:
        modulo = 24
        frame_directory = 'one_frame_per_second'
    elif frames_per_second == 24:
        modulo = 1
        frame_directory = 'every_frame'
    for frame in range(0, frames):
        if frame % modulo == 0:
            image = r'{0}/frame{1}.jpg'.format(directory, frame)
            im = numpy.array(Image.open(image))
            features = extractor.extract_rgb_frame_features(im)
            print("INFO: embedded frame {0} for video {1}".format(frame, video))
            embedded_video.append(features)
    
    embedded_df = pd.DataFrame(embedded_video)
    embedded_df.to_csv('../embeddings/{0}/{1}.csv'.format(frame_directory, lookup[video]), header = False, index = False)
    return embedded_df

def label_frames(video,frames_per_second,lookup):
    """
    This function creates labels for frames in video
    """
    print("INFO: Labeling video: {0}".format(video))
    print("INFO: At {0} frames per second".format(frames_per_second))

    directory = '../frames/{0}'.format(video)
    print("INFO: going to directory {0}".format(directory))
    frames = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory,name))])
    print("INFO: number of frames in directory {0}".format(frames))
    labeled_video = []

    if frames_per_second == 1:
        modulo = 24
        frame_directory = 'one_frame_per_second'
    elif frames_per_second == 24:
        modulo = 1
        frame_directory = 'every_frame'

    for frame in range(0,frames):
        if frame % modulo == 0:
            print("INFO: labeling frame {0} for {1}".format(frame, video))
            image = r'{0}/frame{1}.jpg'.format(directory, frame)
            #imported from another module that uses Google Vision API
            labels = frame_labeler.annotate_frame(image)
            print(labels)
            labeled_video.append(labels)
    labeled_df = pd.DataFrame(labeled_video)
    labeled_df = labeled_df.fillna('n/a')
    labeled_df.to_csv('../labels/{0}/{1}.csv'.format(frame_directory,lookup[video]),header=False,index=False)
    print("INFO: saved labeled files to ../labels/{0}/{1}.csv".format(frame_directory, lookup[video]))
    
    return None



def main(frames_per_second, timeframe, process):
    #TODO: find out why I can can't use os.sys to run these commands, very weird
    #removing existing frames and embeddings ensures that new embeddigns are created from fresh
    #os.sys('rm -r /home/jj_espinoza/source-repository/merlin_ops/video_embedding/frames/*')
    #os.sys('rm -r /hoome/jj_espinoza/source-repository/merlin_ops/video_embedding/every_frame/*')
    #os.sys('rm ../embeddings/one_frame_per_second/*.csv')
    #os.sys('em ../embeddings/every_frame/*.csv')
    look_up_dict = download_lookup_tables(timeframe)
    for key in look_up_dict:
        try:
            extract_frames(video=key)
            #Embedding or labeling frames
            if process == 'embeed':
                embed_frames(video=key, frames_per_second=frames_per_second, lookup=look_up_dict)
            elif process =='label':
                #TODO: create a label_frames functions that mirrors the embeed_frames function and add here
                label_frames(video=key,frames_per_second=frames_per_second, lookup=look_up_dict)
        except Exception,e:
            print('ERROR:frame level embeddings did not complete for:{0} - ended with {1}'.format(key, e))
            continue
    #os.sys("gsutil -m cp ../embeddings/one_frame_per_second/*.csv gs://merlin-video/input/audit_folder_holding_temp_data/frame_embeddings")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('frames_per_second', help="1 frame per second OR 24 frames per second to extract every frame")
    parser.add_argument('timeframe', help=' "all" or "incremental" where incremental will do new videos in last 30 days')
    parser.add_argument('process', help='"embeed" or "label" the first returns embeddings and the second returns labels for images')
    args = parser.parse_args()
    frames_per_second = int(args.frames_per_second)

    main(frames_per_second=frames_per_second, timeframe = args.timeframe, process=args.process)
    
