"""
Scrapes job descriptions from Indeed and saves to Google Cloud

Program takes title, city as parameters and collects data
from Indeed. The raw unconsolidated data can be found
in gs://jj-projects/itsfridayclean_data; for the raw data
look in gs://jj-projects/itsfriday/raw_data
"""

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import WazeRouteCalculator
import datetime
import os
import sys
import glob

import helpers.email_util as email_util
import helpers.logger

logger = helpers.logger.set_up_logging()


def get_current_directory():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    logger.info(f"current directory: {current_directory} saved as output")
    return current_directory


def get_current_date_time():
    now = datetime.datetime.now()
    todays_date = f"{now.year}{now.month}{now.day}_{now.hour}{now.minute}"
    logger.info(f"current date: {todays_date}")
    return todays_date


def create_input_function(title, city, max_commute, max_results_per_city):
    search_criteria = {
        "title": title,
        "city": city,
        "max_results_per_city": max_results_per_city,
        "max_commute": max_commute,
    }
    inputs_for_scraping = pd.DataFrame(
        [search_criteria], columns=search_criteria.keys()
    )
    logger.info(f"created dataframe with inputs {inputs_for_scraping.head}")
    return inputs_for_scraping


def scrape_jobs_from_indeed(title, city, max_commute, max_results_per_city):
    inputs = create_input_function(
        title=title,
        city=city,
        max_commute=max_commute,
        max_results_per_city=max_results_per_city,
    )
    columns = ["city", "job_title", "company_name", "location", "summary", "salary"]
    sample_df = pd.DataFrame(columns=columns)

    for title in inputs["title"]:
        for city in inputs["city"]:
            for start in range(0, inputs["max_results_per_city"], 10):
                url = f"https://www.indeed.com/jobs?q={title}&l={city}&start={start}"
                logger.info(f"DOWNLOADING FROM: {url}")
                page = requests.get(url)
                time.sleep(1)
                soup = BeautifulSoup(page.text, "lxml")
                for div in soup.find_all(name="div", attrs={"class": "row"}):
                    num = len(sample_df) + 1
                    job_post = []
                    job_post.append(city)

                    for a in div.find_all(
                        name="a", attrs={"data-tn-element": "jobTitle"}
                    ):
                        job_post.append(a["title"])

                    company = div.find_all(name="span", attrs={"class": "company"})
                    if len(company) > 0:
                        for b in company:
                            job_post.append(b.text.strip())
                    else:
                        sec_try = div.find_all(
                            name="span", attrs={"class": "result-link-source"}
                        )
                        for span in sec_try:
                            job_post.append(span.text)

                    c = div.findAll("span", attrs={"class": "location"})
                    for span in c:
                        job_post.append(span.text)

                    d = div.findAll("span", attrs={"class": "summary"})
                    for span in d:
                        job_post.append(span.text.strip())

                    try:
                        job_post.append(div.find("nobr").text)
                    except:
                        try:
                            div_two = div.find(name="div", attrs={"class": "sjcl"})
                            div_three = div_two.find("div")
                            job_post.append(div_three.text.strip())
                        except:
                            job_post.append("Nothing_found")

                    sample_df.loc[num] = job_post
                    results = sample_df
    return results


def clean_jobs_from_indeed(indeed_results, title, city):
    for text_column in ["job_title", "company_name", "location", "summary"]:
        indeed_results[text_column] = indeed_results[text_column].str.lower()
        indeed_results.replace({r"[^\x00-\x7F]+": ""}, regex=True, inplace=True)
    indeed_results["clean_address"] = (
        indeed_results["company_name"] + " " + indeed_results["location"]
    )
    clean_indeed = indeed_results.drop_duplicates()
    clean_indeed.to_csv(
        f"../../data/raw_data/indeed_job_scraper_results_{title}_{city}_{get_current_date_time()}.csv",
        index=False,
    )
    logger.info(f"Sample of results {clean_indeed.head}")
    return clean_indeed


def main(title, city):
    current_directory = get_current_directory()
    date_time = get_current_date_time()
    jobs = scrape_jobs_from_indeed(
        title=title, city=city, max_commute=90, max_results_per_city=50
    )
    clean_jobs = clean_jobs_from
