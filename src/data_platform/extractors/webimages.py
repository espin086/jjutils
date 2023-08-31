import urllib2
import re
import os
from os.path import basename
from urlparse import urlsplit
from urlparse import urlparse
from posixpath import basename, dirname
import os
import sys
import time


def process_url(raw_url):
    if " " not in raw_url[-1]:
        raw_url = raw_url.replace(" ", "%20")
        return raw_url
    elif " " in raw_url[-1]:
        raw_url = raw_url[:-1]
        raw_url = raw_url.replace(" ", "%20")
        return raw_url


def get_images(url):
    url = url  ## give the url here
    parse_object = urlparse(url)
    urlcontent = urllib2.urlopen(url).read()
    imgurls = re.findall('img .*?src="(.*?)"', urlcontent)
    time.sleep(1)
    for imgurl in imgurls:
        print("INFO: url = {0}".format(imgurl))

        try:
            time.sleep(1)
            imgurl = process_url(imgurl)
            imgdata = urllib2.urlopen(imgurl).read()
            filname = basename(urlsplit(imgurl)[2])
            output = open(filname, "wb")
            output.write(imgdata)
            output.close()
        except Exception as e:
            print(e)
            pass


def images_to_gcs():
    os.sys("gsutil -m cp *.jpg gs://propertybot/images/raw")
    return None


if __name__ == "__main__":
    url = sys.argv[1]
    get_images(url)
    # images_to_gcs()
