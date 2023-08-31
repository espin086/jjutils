import os
import sys
import email_util
import glob
import pandas as pd
import numpy as np
import datetime

# Running R scraper and saving to Google Cloud
os.system("/usr/bin/Rscript truecar.R")
os.system(
    "gsutil -m  cp ../data/truecar/* gs://jj-projects-bucket/cruisin64/truecar/raw/"
)
os.system("rm ../data/truecar/*")


# consolidating and deplicating raw csv into a master csv
os.system(
    "gsutil -m cp gs://jj-projects-bucket/cruisin64/truecar/raw/* ../data/truecar/"
)
allFiles = glob.glob("../data/truecar/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)
frame = frame.drop_duplicates(subset="vin")


# saving clean file to clean foler in google cloud
frame.to_csv("../data/truecar/clean/truecar.csv", index=False)
num_of_cars = frame.vin.count()
print("INFO: Number of Unique Cars: {0}".format(num_of_cars))
os.system(
    "gsutil -m cp ../data/truecar/clean/truecar.csv gs://jj-projects-bucket/cruisin64/truecar/clean/"
)
os.system("rm ../data/truecar/*.csv")
os.system("rm ../data/truecar/clean/*")


day_of_week = datetime.datetime.today().weekday()
hour_of_day = datetime.datetime.now().hour
# Email notifications
print("DAY OF WEEK: {0} & HOUR OF DAY: {1}".format(day_of_week, hour_of_day))
if day_of_week == 4 and hour_of_day == 6:
    email_util.send_email(
        subject="AUTOMATED EMAIL: {0} Hondas Scraped from Truecar".format(num_of_cars),
        body="check for latest data in: gs://jj-projects-bucket/cruisin64/truecar/clean/",
        user="jj.espinoza.la",
        pwd="",
        recipient="",
    )
