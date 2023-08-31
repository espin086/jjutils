"""
This script reads data from a CSV file and uses the dedupe library to find and cluster duplicate entries.

The script does the following:
    1. It reads data from a CSV file and pre-processes it.
    2. It checks if a settings file exists. If it does, it loads the settings and skips training. If not, it trains the dedupe model using specified fields and saves the trained model.
    3. It performs active learning, asking the user to label pairs of records as duplicates or not.
    4. After active learning and training, the script clusters the data and prints the number of duplicate sets found.
    5. Finally, it writes out the original data with an additional column indicating cluster membership for each record.

Usage: 
    Run from the command line as follows:
        python <script_name.py> --input <input_csv_file> --output <output_csv_file> --settings <settings_file> --training <training_file> --fields <field1> <field2> ...

    -v or --verbose option can be used to increase verbosity level. It can be specified multiple times for more verbosity.

Required Libraries: 
    Python Standard Library, dedupe, unidecode
"""


import os
import csv
import re
import logging
import json
import argparse

import dedupe
from unidecode import unidecode


def preProcess(column):
    column = unidecode(column)
    column = re.sub("  +", " ", column)
    column = re.sub("\n", " ", column)
    column = column.strip().strip('"').strip("'").lower().strip()
    if not column:
        column = None
    return column


def readData(filename):
    data_d = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_row = [(k, preProcess(v)) for (k, v) in row.items()]
            row_id = row["ID"]
            data_d[row_id] = dict(clean_row)
    return data_d


def defineFields(fields):
    return [{"field": field, "type": "String", "has missing": True} for field in fields]


def setup(input_file, output_file, settings_file, training_file, fields):
    data_d = readData(input_file)
    if os.path.exists(settings_file):
        print("reading from", settings_file)
        with open(settings_file, "rb") as f:
            deduper = dedupe.StaticDedupe(f)
    else:
        deduper = dedupe.Dedupe(fields)
        if os.path.exists(training_file):
            print("reading labeled examples from ", training_file)
            with open(training_file, "rb") as f:
                deduper.prepare_training(data_d, f)
        else:
            deduper.prepare_training(data_d)

        dedupe.consoleLabel(deduper)

        deduper.train()

        with open(training_file, "w") as tf:
            deduper.writeTraining(tf)

        with open(settings_file, "wb") as sf:
            deduper.writeSettings(sf)

    clustered_dupes = deduper.match(data_d, 0.5)
    return clustered_dupes


def writeResults(clustered_dupes, output_file):
    cluster_membership = {}
    for cluster_id, (records, scores) in enumerate(clustered_dupes):
        for record_id, score in zip(records, scores):
            cluster_membership[record_id] = {
                "Cluster ID": cluster_id,
                "confidence_score": score,
            }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(str(cluster_membership), f, ensure_ascii=False, indent=4)


def main(args):
    input_file = args.input
    output_file = args.output
    settings_file = args.settings
    training_file = args.training
    fields = args.fields

    logging.getLogger().setLevel(logging.DEBUG if args.verbose else logging.WARNING)

    print("importing data ...")
    fields = defineFields(fields)

    clustered_dupes = setup(
        input_file, output_file, settings_file, training_file, fields
    )
    print("# duplicate sets", len(clustered_dupes))

    writeResults(clustered_dupes, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="count")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--settings", "-s", required=True)
    parser.add_argument("--training", "-t", required=True)
    parser.add_argument("--fields", "-f", required=True, nargs="+")
    args = parser.parse_args()

    main(args)
