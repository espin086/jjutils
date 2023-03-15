
from fredapi import Fred
import os 
import sys
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('propertybot')
print(bucket)


fred = Fred(api_key='xxxxxxxxxxxxx')



def get_fred_to_gcs(series):
    df = fred.get_series('{0}'.format(series))
    if series == 'CPIAUCSL':
        df[[0]] = df[[0]].diff().shift(-1)

    df.to_csv('{0}.csv'.format(series))
    blob = bucket.blob('national_economics_trends/{0}.csv'.format(series))
    blob.upload_from_filename('{0}.csv'.format(series))
    return None


def main():
    indicators = ['CPIAUCSL','MORTGAGE30US', 'A191RL1Q225SBEA', 'UNRATE']
    for metric in indicators:
        print("INFO: uploading {0} to gcs".format(metric))
        get_fred_to_gcs(metric)
    return None



if __name__=="__main__":
    main()
