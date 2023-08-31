"""
Collects leading economic indicators

This module collects leading economic indicators
and saveds them to Google Cloud Storage. It also 
contains an automated email notifier to let me 
know when any of the metrics get our of trend.
The module also contains a calendar for releases
of ecoonomic indicators.
The leaing indicators include:
    - (AWHMAN) Average weekly hours of production workers (manufacturing)
    - (IC4WSA)Initial claims for unemployment insurance
    - (DGORDER) Manufacturer's new orders
    - Fraction of companies reporting slower deliveries
    - (ANDENO) New orders for non-defense capital goods
    - (PERMIT) New private housing units authorized by local building permits
    - (T10Y2Y)Yield Curve: spread between 10-yr T-bond yields and federal funds rate (T10Y2Y)
    - (SP500) Stock prices, 500 common stock (SP500)
    - (M2)Money supply (M2) growth rate
    - (UMCSENT) Index of consumer expectations (UMCSENT')

"""
import pandas as pd
import pandas_datareader.data as web
import datetime


def economic_indicators():
    indicators = [
        "AWHMAN",
        "IC4WSA",
        "DGORDER",
        "ANDENO",
        "PERMIT",
        "SP500",
        "M2",
        "UMCSENT",
    ]
    return indicators


def get_indicators(series, start_year, end_year):
    start = datetime.datetime(start_year, 1, 1)
    end = datetime.datetime(end_year, 1, 27)
    data = web.DataReader(series, "fred", start, end)
    return data


# TODO: understand all of the metrics I am looking at, write a Medium post
# TODO: create a helper function for taking a pandas dataframe to google cloud storage bucket
# TODO: create function that stores economic indicators on google cloud storage
# TODO: create a time-series anomaly detector...
# TODO: add to cronjob with an email notification


def main():
    series = economic_indicators()
    get_indicators(series=series, start_year=1996, end_year=2018)
    return None


if __name__ == "__main__":
    main()
