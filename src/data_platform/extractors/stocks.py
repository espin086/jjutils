import io
import time

import pandas as pd
import requests


def google_stocks(symbol, startdate=(1, 1, 2005), enddate=None):
    startdate = str(startdate[0]) + "+" + str(startdate[1]) + "+" + str(startdate[2])

    if not enddate:
        enddate = time.strftime("%m+%d+%Y")
    else:
        enddate = str(enddate[0]) + "+" + str(enddate[1]) + "+" + str(enddate[2])

    stock_url = (
        "http://www.google.com/finance/historical?q="
        + symbol
        + "&startdate="
        + startdate
        + "&enddate="
        + enddate
        + "&output=csv"
    )

    raw_response = requests.get(stock_url).content

    stock_data = pd.read_csv(io.StringIO(raw_response.decode("utf-8")))

    return stock_data


if __name__ == "__main__":
    data = google_stocks("AAPL")
    print(data)

    data_truncated = google_stocks("AAPL", enddate=(1, 1, 2006))
    print(data_truncated)

    data.to_csv("AAPL.csv")
