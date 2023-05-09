import pandas as pd
import yaml
from google.cloud import bigquery

with open ("../config.yaml") as yaml_file:
    config = yaml.safe_load(yaml_file)

CENSUS_YEARS = config['CENSUS_YEARS']


client = bigquery.Client()

def create_census_queries():
    queries = {}
    for year in CENSUS_YEARS:
        query = f"""
            SELECT
        geo_id,
        employed_pop,
        median_income,
        bachelors_degree_or_higher_25_64,
        housing_units_renter_occupied,
        commuters_by_public_transportation
        FROM
        `bigquery-public-data.census_bureau_acs.censustract_{year}_5yr`
        """
        queries[year] = query
    return queries


def queries_to_df_list(queries):
    dfs = []
    for k,v in queries.items():
        df = client.query(v).to_dataframe()
        df['year'] = k
        dfs.append(df)

    return dfs

def concat_list_of_dfs(list_of_dfs):
    df = pd.concat(list_of_dfs)
    return df


queries = create_census_queries()
list_of_dfs = queries_to_df_list(queries=queries)
df = concat_list_of_dfs(list_of_dfs=list_of_dfs)








