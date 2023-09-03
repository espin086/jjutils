"""
This module scrapes listings from Zillow of houses for sale.

Use: python2 zillow_scraper.py 90670 newest

TODO: Add logging and unit testing to this module
TODO: Find out why Zillow Scraper isn't working
TODO: Create data studio dashboard of listings
"""

import requests
import urllib3
from lxml import html

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def parse(zipcode, filter=None):
    if filter == "newest":
        url = f"https://www.zillow.com/homes/for_sale/{zipcode}/0_singlestory/days_sort"
    elif filter == "cheapest":
        url = f"https://www.zillow.com/homes/for_sale/{zipcode}/0_singlestory/pricea_sort/"
    else:
        url = f"https://www.zillow.com/homes/for_sale/{zipcode}_rb/?fromHomePage=true&shouldFireSellPageImplicitClaimGA=false&fromHomePageTab=buy"

    for _ in range(5):
        try:
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, sdch, br",
                "accept-language": "en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            }
            response = requests.get(url, headers=headers, verify=False)
            parser = html.fromstring(response.text)
            search_results = parser.xpath("//div[@id='search-results']//article")
            properties_list = []

            for properties in search_results:
                raw_address = properties.xpath(
                    ".//span[@itemprop='address']//span[@itemprop='streetAddress']//text()"
                )
                raw_city = properties.xpath(
                    ".//span[@itemprop='address']//span[@itemprop='addressLocality']//text()"
                )
                raw_state = properties.xpath(
                    ".//span[@itemprop='address']//span[@itemprop='addressRegion']//text()"
                )
                raw_postal_code = properties.xpath(
                    ".//span[@itemprop='address']//span[@itemprop='postalCode']//text()"
                )
                raw_price = properties.xpath(
                    ".//span[@class='zsg-photo-card-price']//text()"
                )
                raw_info = properties.xpath(
                    ".//span[@class='zsg-photo-card-info']//text()"
                )
                raw_broker_name = properties.xpath(
                    ".//span[@class='zsg-photo-card-broker-name']//text()"
                )
                url = properties.xpath(".//a[contains(@class,'overlay-link')]/@href")
                raw_title = properties.xpath(".//h4//text()")

                address = (
                    " ".join(" ".join(raw_address).split()) if raw_address else None
                )
                city = "".join(raw_city).strip() if raw_city else None
                state = "".join(raw_state).strip() if raw_state else None
                postal_code = (
                    "".join(raw_postal_code).strip() if raw_postal_code else None
                )
                price = "".join(raw_price).strip() if raw_price else None
                info = " ".join(" ".join(raw_info).split()).replace("\xb7", ",")
                broker = "".join(raw_broker_name).strip() if raw_broker_name else None
                title = "".join(raw_title) if raw_title else None
                property_url = f"https://www.zillow.com{url[0]}" if url else None
                is_forsale = properties.xpath('.//span[@class="zsg-icon-for-sale"]')

                properties = {
                    "address": address,
                    "city": city,
                    "state": state,
                    "postal_code": postal_code,
                    "price": price,
                    "facts and features": info,
                    "real estate provider": broker,
                    "url": property_url,
                    "title": title,
                }
                if is_forsale:
                    properties_list.append(properties)
            return properties_list
        except Exception:
            print(f"Failed to process the page {url}")


if __name__ == "__main__":
    print(parse(zipcode="90670", filter="newest"))
