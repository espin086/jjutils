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
    CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    logger.info('current directory: {} saved as output'.format(CURRENT_DIRECTORY))
    return CURRENT_DIRECTORY

def get_current_date_time():
    #TODO: create  as helper function, currently saves current date to be used when saving files
    now = datetime.datetime.now()
    todays_date = str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour) + str(now.minute)
    logger.info('current date: {}'.format(todays_date))
    return todays_date

def create_input_function(title, city, max_commute, max_results_per_city):
    """ HELPER FUNCTION:  Creates a dataframe for jobs search criteria
    
    Takes in various factors for a job search and creates
    a pandas dataframe that can be feed as input into a jobs scraper
    
    """
    search_criteria = {}
    search_criteria['title'] = title
    search_criteria['city'] = city
    search_criteria['max_results_per_city'] = max_results_per_city
    search_criteria['max_commute'] = max_commute
    inputs_for_scraping = pd.DataFrame([search_criteria], columns=search_criteria.keys()) 
    logger.info('created dataframe with inputs {}'.format(inputs_for_scraping.head))
    return inputs_for_scraping

def scrape_jobs_from_indeed(title, city, max_commute, max_results_per_city):
    #setting up inputs
    inputs = create_input_function(title=title, city=city, max_commute=max_commute, max_results_per_city=max_results_per_city)
    #setting up structure of outputs
    columns = ['city', 'job_title', 'company_name', 'location', 'summary', 'salary']
    sample_df = pd.DataFrame(columns = columns)
    
    for title in inputs['title']:
        for city in inputs['city']:
            for start in range(0, inputs['max_results_per_city'], 10): 
                url = 'https://www.indeed.com/jobs?q={0}&l={1}&start={2}'.format(str(title), str(city), str(start))
                logger.info('DOWNLOADING FROM: {}'.format(url))
                page = requests.get(url)
                time.sleep(1)  #ensuring at least 1 second between page grab
                soup = BeautifulSoup(page.text, 'lxml')
                for div in soup.find_all(name='div', attrs={'class':'row'}): 
                    #specifying row num for index of job posting in dataframe
                    num = (len(sample_df) + 1) 
                    #creating an empty list to hold the data for each posting
                    job_post = [] 
                    #append city name
                    job_post.append(city) 
                
                     #grabbing job title
                    for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
                        job_post.append(a['title']) 
                    #grabbing company name
                    company = div.find_all(name='span', attrs={'class':'company'}) 
                    if len(company) > 0: 
                        for b in company:
                            job_post.append(b.text.strip()) 
                    else: 
                        sec_try = div.find_all(name='span', attrs={'class':'result-link-source'})
                        for span in sec_try:
                            job_post.append(span.text) 
                    #grabbing location name
                    c = div.findAll('span', attrs={'class': 'location'})
                    for span in c: 
                        job_post.append(span.text) 
                
                    #grabbing summary text
                    d = div.findAll('span', attrs={'class': 'summary'}) 
                    for span in d:
                        job_post.append(span.text.strip()) 
                
                    #grabbing salary
                    try:
                        job_post.append(div.find('nobr').text) 
                    except:
                        try:
                            div_two = div.find(name='div', attrs={'class':'sjcl'}) 
                            div_three = div_two.find('div') 
                            job_post.append(div_three.text.strip())
                        except:
                            job_post.append('Nothing_found') 
                    #appending list of job post info to dataframe at index num
                    sample_df.loc[num] = job_post
                    results = sample_df
    return results
    
def clean_jobs_from_indeed(indeed_results, title, city):
    for text_column in ['job_title', 'company_name', 'location', 'summary']:
        indeed_results[text_column] = indeed_results[text_column].str.lower()
        #replaces non-ascii text
        indeed_results.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
    indeed_results["clean_address"] = indeed_results["company_name"] + ' ' + indeed_results["location"]
    clean_indeed = indeed_results.drop_duplicates()
    clean_indeed.to_csv('../../data/raw_data/indeed_job_scraper_results_{0}_{1}_{2}.csv'.format(title, city, get_current_date_time()), index=False)
    logger.info('Sample of results {}'.format(clean_indeed.head))
    return clean_indeed


# In[14]:

#TODO: add commute time to jobs saved after deduplicating
def calculate_commute_with_waze(from_address, to_address):
    commute = []
    from_address = from_address
    region = 'US'
    try:
        to_address = address
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region )
        commutes.append(route.calc_route_info(real_time=False))
    except:
        commutes.append((0,0))
    return commutes
    
def local_to_gcs():
    #saving to cloud and deleting local copies to save space
    os.system('gsutil -m cp ../../data/raw_data/* gs://jj-projects-bucket/itsfriday/raw_data/')
    #saving collection of today's jobs
    allFiles = glob.glob("../../data/raw_data/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        list_.append(df)
        frame = pd.concat(list_)

    #drops city search before removing duplicates to get truly unique results
    frame = frame.drop(['city'], axis=1)
    frame = frame.drop_duplicates()
    frame.to_csv('../../data/clean_data/indeed_job_scraper_results_{0}.csv'.format(get_current_date_time()),index=False)
    os.system('gsutil -m cp ../../data/clean_data/* gs://jj-projects-bucket/itsfriday/clean_data/')


    #deleting all local data
    os.system('rm ../../data/raw_data/*')
    os.system('rm ../../data/clean_data/*')


#MAIN FUNTION
def main(title, city):
    current_directory = get_current_directory()
    date_time = get_current_date_time()
    jobs = scrape_jobs_from_indeed(title=title, city=city, max_commute=90, max_results_per_city=50)
    clean_jobs = clean_jobs_from_indeed(indeed_results=jobs, title=title, city=city)
    return clean_jobs


if __name__ == "__main__":
    #defining cities to scrape
    city_set = ['Los+Angeles', 'Los+Angeles+County', 'Orange+County']
    title_set = ['chief+data+officer','Senior+Vice+President','Vice+President', 'director+data+science', 'director+analytics', 'vice+president+analytics', 'vice+president+data+science','chief+analytics+officer']
    #running MAIN function
    for city in city_set:
        for title in title_set:
            try:
                main(title=title, city=city)
            except Exception,e:
                print(e)
    #saving local results to the cloud
    local_to_gcs()
    email_util.send_email(
            subject='AUTOMATED: Indeed Job Scraper Collecting Jobs', 
            body='Your indeed.com job scraper is collecting job descriptions: gs://jj-projects-bucket/itsfriday/clean_data/')
