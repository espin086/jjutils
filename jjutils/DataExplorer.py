import pandas as pd
import logging
from argparse import ArgumentParser
from ydata_profiling import ProfileReport


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataFrameProfiler:
    """Class to profile a dataframe using ydata-profiling."""

    def __init__(self, dataframe: pd.DataFrame, title: str = "Data Profiling Report"):
        """
        Initializes the DataFrameProfiler with a dataframe.

        Args:
            dataframe (pd.DataFrame): The dataframe to profile.
            title (str): The title of the profiling report.
        """
        self.dataframe = dataframe
        self.title = title
        self.profile = ProfileReport(dataframe, title=title)

    def generate_report(
        self, output_format: str = "html", output_file: str = "report.html"
    ):
        """
        Generates the profiling report and saves it to a file.

        Args:
            output_format (str): The format of the output file. Valid options: 'html', 'json'.
            output_file (str): The name of the output file.
        """
        if output_format == "html":
            self.profile.to_file(output_file)
            logging.info(f"Report generated and saved to {output_file} in HTML format.")
        elif output_format == "json":
            self.profile.to_file(output_file)
            logging.info(f"Report generated and saved to {output_file} in JSON format.")
        else:
            logging.error("Unsupported output format. Use 'html' or 'json'.")

    def export_to_json(self) -> str:
        """
        Exports the profiling report to a JSON string.

        Returns:
            str: The JSON string of the profiling report.
        """
        json_data = self.profile.to_json()
        logging.info("Report exported to JSON string.")
        return json_data


def main():
    parser = ArgumentParser(description="DataFrame Profiling Application")
    parser.add_argument(
        "--csv_file", type=str, help="Path to the CSV file for profiling."
    )
    parser.add_argument(
        "--excel_file", type=str, help="Path to the Excel file for profiling."
    )
    parser.add_argument(
        "--sheet_name", type=str, help="Specific sheet name for Excel file."
    )
    parser.add_argument("--db_name", type=str, help="Name of the SQLite database.")
    parser.add_argument(
        "--table_name", type=str, help="Name of the table to read from SQLite database."
    )
    parser.add_argument(
        "--output_format",
        type=str,
        choices=["html", "json"],
        default="html",
        help="Either 'html' or 'json' format for the output report.",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="report.html",
        help="Name of the output file for the report.",
    )
    args = parser.parse_args()

    dataframe = None

    if args.csv_file:
        csv_handler = CSVHandler(args.csv_file)
        dataframe = csv_handler.read_csv()
    elif args.excel_file and args.sheet_name:
        excel_handler = ExcelHandler(args.excel_file)
        dataframe = excel_handler.read_sheet(args.sheet_name)
    elif args.db_name and args.table_name:
        db_handler = SQLiteCRUD(args.db_name)
        if db_handler.connect():
            dataframe = pd.DataFrame(db_handler.select_data(args.table_name))
            db_handler.close()

    if dataframe is not None:
        profiler = DataFrameProfiler(dataframe=dataframe, title="Data Profiling Report")
        profiler.generate_report(
            output_format=args.output_format, output_file=args.output_file
        )
    else:
        logging.error(
            "No valid data source provided. Please specify a CSV file, Excel file with sheet name, or SQLite database with table name."
        )


if __name__ == "__main__":
    main()
