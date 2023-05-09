import pandas as pd
import yaml
from google.cloud import bigquery

with open("../config.yaml") as yaml_file:
    config = yaml.safe_load(yaml_file)

CENSUS_YEARS = config["CENSUS_YEARS"]


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
    for k, v in queries.items():
        df = client.query(v).to_dataframe()
        df["year"] = k
        dfs.append(df)

    return dfs


def concat_list_of_dfs(list_of_dfs):
    df = pd.concat(list_of_dfs)
    return df


def upload_dataframe_to_bigquery(
    df, project_id, dataset_id, table_id, if_exists="fail"
):
    """
    Upload a Pandas DataFrame to BigQuery.

    Args:
    df (pd.DataFrame): The DataFrame to upload.
    project_id (str): The project ID of the BigQuery project.
    dataset_id (str): The dataset ID where the table will be created.
    table_id (str): The table ID for the new table.
    if_exists (str): The behavior if the table already exists. Options: 'fail', 'replace', 'append'. Default: 'fail'.
    """
    client = bigquery.Client(project=project_id)

    # Configure the destination table
    table_ref = bigquery.TableReference.from_string(
        f"{project_id}.{dataset_id}.{table_id}"
    )

    # Write the DataFrame to BigQuery
    job_config = bigquery.LoadJobConfig(
        schema=bigquery.Schema.from_dataframe(df),
        write_disposition=if_exists.upper(),
    )
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Wait for the job to complete
    print(f"Data uploaded to BigQuery table {project_id}.{dataset_id}.{table_id}")


queries = create_census_queries()
list_of_dfs = queries_to_df_list(queries=queries)
df = concat_list_of_dfs(list_of_dfs=list_of_dfs)

# Upload the final DataFrame to BigQuery
project_id = "your_project_id"
dataset_id = "your_dataset_id"
table_id = "your_table_id"
upload_dataframe_to_bigquery(df, project_id, dataset_id, table_id, if_exists="replace")
