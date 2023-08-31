#!/usr/bin/python


import sys  # used to facilitate arguments in terminal
import requests
from bs4 import BeautifulSoup
import wikipedia
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
from nltk.tokenize import sent_tokenize, word_tokenize

if sys.argv[1] == "--h":
    print("")
    print("***************************************")
    print("************** help menu **************")
    print("***************************************")
    print("")
    print("author: JJ Espinoza")
    print("description: Pulls data from various sources")
    print("created: 2017-12-13")
    print("")
    print("commands:                 descriptions:")
    print("_______________________________________")
    print("")
    print("--h                           help menu")
    print('--wikisearch ["keword"]       returns related wiki pages')
    print('--wikiinfo ["page"]           provides page summary')
    print('--wikiscrape ["page"]         scrapes page')
    print('--links ["url"]               scrapes hyperlinks on page')


#####################
if sys.argv[1] == "--links":
    url = sys.argv[2]
    # returns HTML content
    r = requests.get(url)
    # Converted into something useful
    soup = BeautifulSoup(r.content)
    # extract all hyperlinks for each link document
    for link in soup.find_all("a"):
        print(link.text, link.get("href"))

if sys.argv[1] == "--wikisearch":
    print(wikipedia.search(sys.argv[2]))

if sys.argv[1] == "--wikiinfo":
    print(wikipedia.summary(sys.argv[2]))

if sys.argv[1] == "--wikiscrape":
    page = wikipedia.page("Python (genus)")
    print(page.title)
    print(page.url)
    page_content = page.content
    print(page_content)
