# -*- coding: utf-8 -*-
""" Create Video Embedding

This module downloads mp4 videos from a google cloud storage bucket, then
it creates embeddings of the videos using the Google Inception model.
The user has the option to embed all the videos or just the ones updated
in the last 24 hours. This module depends on specific lookup tables 
stored in google cloud. 

Installation: 
        This module requires the YouTube downloader and other software.
        To install this software run:

        $ sh requirements.sh

"""

import tensorflow as tf
import json
import pandas as pd
from subprocess import call
import sys
import os
from datetime import date
import argparse
import datetime
from datetime import timedelta
import numpy as np


now = datetime.datetime.now()
now = now.strftime("%Y_%m_%d_%H_%M")



CURRENT_PROJECT_DIRECTORY = os.path.abspath(".").replace('/code','')

print(CURRENT_PROJECT_DIRECTORY)


#filepath=os.path.dirname(os.path.realpath(__file__))
#helperpath = filepath.replace('video_embedding/code', 'helpers')
#sys.path.insert(0, helperpath)
import email_util
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")




def download_videos():
    """
    
    Downloads ONLY NEW Clean Videos from Storgage Bucket

    Downloads videos locally into the clean_videos directory
    then saves a csv file with the names of the videos. The videos 
    and csv are used by the YouTube inception model to create embeddings.
    This csv needs so specify the absolute file paths to the mp4 videos
    as well a 'class' so the Inception code will work.  The class has
    no bearing on the embeddings, so the row number was used as a placeholder.

    Videos are saved in the '../videos' folder
    Lookup tables are saved in the '../lookup_tables' folder

    """
    #deleting clean videos saved locally, this is important to ensure videos removed in cloud dont' stay locally
    os.system('rm ../videos/clean_videos/*')
    
    os.system('gsutil -m cp  gs://merlin-video/input/clean_videos/* ../videos/clean_videos')
    
    

    os.system('rm ../lookup_tables/vid_dataset.csv')
    os.system('ls ../videos/clean_videos >> ../lookup_tables/vid_dataset.csv')

    df = pd.read_csv('../lookup_tables/vid_dataset.csv', sep = '\t', names = ['file'])
    df['path'] = '{0}/videos/clean_videos/'.format(CURRENT_PROJECT_DIRECTORY) + df['file']
    df['class'] = df.index
    df = df.drop(['file'], axis=1)
    df.to_csv('../lookup_tables/vid_dataset.csv', header=False, index=False)
    print('INFO: all videos saved in vid_dataset can view by typing: vi ../lookup_tables/vid_dataset.csv')
    get_merlin_synopses_table()


    return df


    
def get_merlin_synopses_table():
    """
    HELPER:  Gets latest Merlin synopsis table from Google Cloud

    Saves synopses table in lookup folder for processing by other programs.


    """
    os.system('gsutil cp gs://merlin-video/input/merlin_synopses.csv ../lookup_tables/merlin_synopses.csv')
    merlin_synopses = pd.read_csv('../lookup_tables/merlin_synopses.csv')
    merlin_synopses = merlin_synopses.set_index('movie')
    return merlin_synopses


def get_trailer_tracker_table():
    """
    Saves the latest trailer tracker table to local

    Saves the latest trailer tracker table. This table is used
    to identify new trailers to restrict embeddding process
    only to new trailers

    """
    os.system('gsutil cp gs://merlin-video/input/clean_videos/tracker_new.csv ../lookup_tables/tracker_new.csv')
    tracker = pd.read_csv('../lookup_tables/tracker_new.csv')
    return tracker

def create_incremental_list(days_back):
    vid_dataset = pd.read_csv('../lookup_tables/vid_dataset.csv',names = ['paths', 'id'])
    tracker = get_trailer_tracker_table()
    tracker['latest_upload_date'] = tracker['latest_upload_date'].astype(int)
    tracker['latest_upload_date'] = pd.to_datetime(tracker['latest_upload_date'], format='%Y%m%d')
    #specifying date filters
    today = str(date.today()).replace('-','')
    today = pd.to_datetime(today, format='%Y%m%d')
    today_days_back = today - timedelta(days=days_back)

    #filtering tracker
    tracker_incremental = tracker[(tracker['latest_upload_date'] >= today_days_back) & (tracker['latest_upload_date'] <=today)]
    print("INFO: input file will embeed trailers from last {0}".format(days_back))
    print(tracker_incremental[['filename', 'latest_upload_date']])
    tracker_incremental_file = tracker_incremental[['filename']]
    
    #filtered vid dataset
    vid_dataset['temp'] = vid_dataset['paths'].str.replace('/home/jj_espinoza/cronjob/merlin_ops/video_embedding/videos/clean_videos/', '')
    #print("INFO: vid_dataset with temp variable for matching with tracker")
    #print(vid_dataset)
    incremental_vid_dataset = vid_dataset.merge(tracker_incremental_file, how = 'inner', left_on='temp', right_on='filename')
    print("INFO: FINAL VIDDATASET FILE FOR EMBEDDING")
    incremental_vid_dataset = incremental_vid_dataset[['paths','id']]
    print(incremental_vid_dataset)
    incremental_vid_dataset.to_csv('../lookup_tables/vid_dataset_incremental.csv', header=None, index=False)

    print("INFO: saved incremental file in ../lookup_tables/vid_dataset_incremental.csv")

    return incremental_vid_dataset




def create_video_embeddings(timeframe):
    """
    Creates video embeddings using Google Inception Model 
    
    ARGS: 
        timeframe(string- all or last24hours): selects videos to embed, all historical or last 24 hours

    """

    if timeframe == 'incremental':
        time = '_incremental'
    elif timeframe =='all':
        time = ''
    
    os.system('python {0}/youtube-8m/feature_extractor/extract_tfrecords_main.py \
            --input_videos_csv {0}/lookup_tables/vid_dataset{1}.csv \
            --output_tfrecords_file {0}/tfrecords/video_embedding{1}.tfrecord'.format(CURRENT_PROJECT_DIRECTORY,time))
    return None

def parse_video_embeddings(file):
    """
    Parses tfrecord video embedding into CSV file for model consumption
    
    This is a helper fucntion to the tf_records_to_csv fnction below

    """
    result = []
    for example in tf.python_io.tf_record_iterator(file):
        result.append(tf.train.Example.FromString(example))

    result_dfs = []
    for r in result:
        embeddings = list(r.features.feature['mean_rgb'].float_list.value)
        video = list(r.features.feature['id'].bytes_list.value)[0]
        video = video.replace('{0}/videos/clean_videos/'.format(CURRENT_PROJECT_DIRECTORY),'')
        video = video.replace('.mp4','')

        df = pd.DataFrame({'embedding':embeddings}).T
        df['movie'] = video
        df = df.set_index('movie')
        
        column_names = ['X' + str(name) for name in list(df)]
        df.columns = [
                column_names
        ]
        
        result_dfs.append(df)
        final_df = pd.concat(result_dfs)     
    return final_df

def tf_records_to_csv(timeframe):
    """
    Save TF records to CSV, either all of them or just add the lastest trailers
    """
    
    if timeframe == 'all':
        time = ''
    elif timeframe == 'incremental':
        time = '_incremental'

    final_df = parse_video_embeddings('../tfrecords/video_embedding{0}.tfrecord'.format(time))
    
    merlin_synopses = get_merlin_synopses_table()
    merged = pd.merge(final_df, merlin_synopses, left_index=True, right_index=True, how='left')
    X_cols = [col for col in merged.columns if 'X' in col]
    X_cols.insert(0, 'movie_id')
    print(X_cols)
    merged = merged[X_cols]
    #TODO: change back to movie_id, but warn data scientist working on deep model first
    merged = merged.rename(columns={'movie_id': 'movie'})
    merged.movie = merged.movie.round() #rounding to convert to integer
    merged = merged[np.isfinite(merged['movie'])]#this drops NA where movie ID doesn't exits
    

    merged.to_csv('../embeddings/merlin_video_movie_id{0}.csv'.format(time), index=False)
    print(merged.head)
    #saving existing file to archive to keep a running record of saved, also saving a local copy for comparision
    os.system('gsutil cp gs://merlin-video/input/merlin_video_movie_id{0}.csv ../embeddings/merlin_video_movie_id_{0}previous.csv')
    os.system('gsutil cp gs://merlin-video/input/merlin_video_movie_id{0}.csv gs://merlin-video/input/archives/merlin_video_movie_id{0}_{1}.csv'.format(time, now))
    #saving old and new file in temporatory auditing file on Cloud for easier auditing
    os.system('gsutil cp ../embeddings/* gs://merlin-video/input/audit_folder_holding_temp_data')
    return None


def incremental_consolidation_with_existing(timeframe):
    if timeframe == 'incremental':
        historical = pd.read_csv('../embeddings/merlin_video_movie_id.csv')
        incremental = pd.read_csv('../embeddings/merlin_video_movie_id_incremental.csv')
        #updating existing trailers if new ones are availalble, by keeping last record if there is a duplicate
        updated = pd.concat([historical,incremental]).drop_duplicates(['movie'],keep='last').sort_values('movie')
        #appending only new dataframes
        common = historical.merge(incremental,on=['movie'])
        new = incremental[(~incremental.movie.isin(common.movie))]
        final = updated.append(new)
    elif timeframe == 'all':
        final = pd.read_csv('../embeddings/merlin_video_movie_id.csv')

    #saving final embedding (all or incremental to embeddings file
    final.to_csv('../embeddings/merlin_video_id_final.csv', index=False)
    #adding final embedding to audit folder in google cloud
    os.system('gsutil cp ../embeddings/merlin_video_movie_id_final.csv gs://merlin-video/input/audit_folder_holding_temp_data')
    #combining tfrecords locally so incremental is part of historical record of tfrecords
    os.system('cat ../tfrecords/video_embedding.tfrecord ../tfrecords/video_embedding_incremental.tfrecord > ../tfrecords/video_embedding_final.tfrecord')
    return None

def save_audited_embeddings_to_gcs():
    #saving audited file from audit folder to folder where Merlin Model can handle
    os.system('gsutil cp gs://merlin-video/input/audit_folder_holding_temp_data/merlin_video_movie_id_final.csv gs://merlin-video/input/merlin_video_movie_id.csv')
    #saving final audited file locally as well
    os.system('gsutil cp gs://merlin-video/input/merlin_video_movie_id.csv ../embeddings/merlin_video_movie_id_final.csv')

def main(timeframe,stage):
    if stage == 'download_videos':
        download_videos()

    elif stage == 'embeed':
        create_incremental_list(8)
        create_video_embeddings(timeframe)
        tf_records_to_csv(timeframe)
        incremental_consolidation_with_existing(timeframe)
    
    elif stage == 'publish':
        save_audited_embeddings_to_gcs()



if __name__ == "__main__":
    #defining argparser - includes moduel docstring in the help menu
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    #adding arguments to parser for the main function, will appear in help
    parser.add_argument('timeframe', help="use 'incremental' for latest or 'all' for all trailers")
    parser.add_argument('stage', help='the state of the process: download_videos, embeed, or publish')
    #parsing arguments
    args = parser.parse_args()
    
    #MAIN FUNCTION
    main(timeframe=args.timeframe, stage=args.stage)
