# jjutils

A small Python package of data-wrangling helpers I reuse across my other projects. It wraps pandas and a few storage backends behind classes with a consistent shape: build the object with a path or connection, call methods, get a DataFrame back. There are readers and writers for CSV, Excel, SQLite, and BigQuery, a DataFrame cleaner, a ydata-profiling wrapper, a K-Means helper with an elbow plot, and panel regression classes built on statsmodels and linearmodels. Every module logs through the standard `logging` module and swallows exceptions into log lines rather than raising, so check return values.

## Installation

Editable install from a clone:

```bash
git clone https://github.com/espin086/jjutils.git
cd jjutils
pip install -e .
```

`setup.py` reads `requirements.txt` for `install_requires`, so a plain `pip install .` pulls the pinned dependencies. The package is not published to PyPI as far as this repo shows.

Some modules need dependencies that are **not** in `requirements.txt`. Install those yourself if you use the module:

| Module | Extra dependency |
|---|---|
| `jjutils.DataExplorer` | `ydata-profiling` |
| `jjutils.bigqueryhandler` | `google-cloud-bigquery` |
| `jjutils.panel` | `linearmodels` |

## Module reference

### `jjutils.FileHandler`

Path-based file reads and writes. Text methods return `None` and log an error when the file is missing.

- `FileHandler(file_path)`
- `read_csv(sep=",") -> pd.DataFrame`
- `read_file() -> str`
- `write_file(content)` overwrites
- `append_to_file(content)`
- `delete_file()`

```python
from jjutils.FileHandler import FileHandler

df = FileHandler("data/train.csv").read_csv()
```

### `jjutils.csvhandler`

CSV reader/writer with append and full-replace semantics.

- `CSVHandler(file_path, delimiter=",")`
- `read_csv()`, `save_csv(df, index=False)`, `append_csv(df, index=False)`, `update_csv(df, index=False)`, `get_dataframe()`
- `main()` runs a demo against `data/train.csv`

```python
from jjutils.csvhandler import CSVHandler

h = CSVHandler("data/train.csv")
df = h.read_csv()
h.append_csv(df.head(1))
```

### `jjutils.Excel`

Multi-sheet Excel workbook handling through openpyxl. Keeps read sheets in an internal `dataframes` dict.

- `ExcelHandler(file_path)`
- `read_sheet(sheet_name)`, `read_all_sheets()`, `save_sheet(df, sheet_name)`, `save_all_sheets()`, `get_dataframe(sheet_name)`, `list_sheets()`

Runnable as a script: `python jjutils/Excel.py data/construction.xlsx` reads all sheets, prints the sheet names, and writes them back.

```python
from jjutils.Excel import ExcelHandler

xl = ExcelHandler("data/construction.xlsx")
print(xl.list_sheets())
df = xl.read_sheet("Sheet1")
```

### `jjutils.SQLiteCRUD`

Thin CRUD layer over `sqlite3`. Table columns are passed as a `{column: "SQL TYPE"}` dict; conditions are raw SQL strings.

- `SQLiteCRUD(db_name)`
- `connect()`, `close()`
- `create_table(table_name, columns)`
- `insert_data(table_name, data)`
- `select_data(table_name, condition=None)`
- `update_data(table_name, data, condition)`
- `delete_data(table_name, condition)`

```python
from jjutils.SQLiteCRUD import SQLiteCRUD

db = SQLiteCRUD("data/database.db")
db.connect()
db.create_table("applicants", {"id": "TEXT NOT NULL", "name": "TEXT NOT NULL"})
db.insert_data("applicants", {"id": "1", "name": "Ada"})
print(db.select_data("applicants"))
db.close()
```

See `examples/example_SQLiteCRUD.py` for a full create/insert/select/update/delete pass driven off the table definitions in `jjutils/config.py`.

### `jjutils.bigqueryhandler`

Google BigQuery operations against a project id. Query results come back as a DataFrame.

- `BigQueryHandler(project_id: str)`
- `run_bigquery(query: str)` returns a DataFrame, or `None` on error
- `create_table(dataset_name, table_name, schema: list)` where schema is a list of `bigquery.SchemaField`
- `insert_data(dataset_name, table_name, rows_to_insert: list)` list of dicts
- `update_data(query: str)` and `delete_data(query: str)` run raw SQL

```python
from jjutils.bigqueryhandler import BigQueryHandler

bq = BigQueryHandler("my-gcp-project")
df = bq.run_bigquery("SELECT 1 AS n")
```

Authentication is whatever the `google.cloud` client picks up from the environment. The module does not handle credentials itself.

### `jjutils.DataProcessor`

`DataFrameCleaner` holds a DataFrame and mutates it in place across chained calls.

- `DataFrameCleaner(dataframe)`
- `change_index(column)`, `remove_duplicates()`, `remove_missing_values()`
- `remove_outliers(column, threshold)`
- `convert_data_types(column, new_type)`
- `remove_columns(columns)`
- `lower_case_column(column)`, `remove_white_spaces(column)`, `remove_special_characters(column)`, `clean_text_column(column)`
- `get_cleaned_dataframe()`

```python
from jjutils.DataProcessor import DataFrameCleaner

cleaner = DataFrameCleaner(df)
cleaner.convert_data_types("Pclass", "category")
cleaner.remove_duplicates()
cleaner.clean_text_column("Name")
clean = cleaner.get_cleaned_dataframe()
```

### `jjutils.DataExplorer`

Wrapper over `ydata_profiling.ProfileReport`.

- `DataFrameProfiler(dataframe, title="Data Profiling Report")`
- `generate_report(output_format="html", output_file="report.html")`
- `export_to_json() -> str`

```python
from jjutils.DataExplorer import DataFrameProfiler

DataFrameProfiler(df).generate_report(output_file="report.html")
```

The module also defines a `main()` with an argparse CLI (`--csv_file`, `--excel_file`, `--sheet_name`, `--db_name`, `--table_name`, `--output_format`, `--output_file`). That `main()` calls `CSVHandler`, `ExcelHandler`, and `SQLiteCRUD` without importing them, so running the module as a script raises `NameError` on those branches. `examples/example_DataExplorer.py` has the same problem in reverse: it imports `DataFrameExplorer`, a name this module does not define. Use the `DataFrameProfiler` class directly.

### `jjutils.kmeans`

K-Means clustering on numeric columns, with standard scaling applied first.

- `KMeansClustering(data: pd.DataFrame)`
- `scale_data()`
- `elbow_plot(max_clusters: int)` computes WCSS in a `ThreadPoolExecutor` and plots it with matplotlib
- `calculate_wcss(num_clusters: int) -> float`
- `cluster_data(num_clusters: int) -> pd.DataFrame` returns the data with a `Cluster` column added

```python
from jjutils.kmeans import KMeansClustering

km = KMeansClustering(df)
km.elbow_plot(10)
labeled = km.cluster_data(4)
```

`examples/example_KMeansAnalysis.ipynb` walks through this.

### `base_regression.py` and `jjutils.panel`

`base_regression.BaseRegression` is the shared base: it stores the data, dependent variable, independent variables, and panel variable, exposes an abstract `fit()`, and a `print_report()` that raises `ValueError` until `fit()` has run.

`jjutils/panel.py` subclasses it three ways:

- `OLSRegression` via `statsmodels`
- `FixedEffectsRegression` via `linearmodels.panel.PanelOLS`
- `RandomEffectsRegression` via `linearmodels.panel.RandomEffects`

Each implements `fit()` and extends `print_report()`.

Note that `base_regression.py` sits at the repo root, not inside the `jjutils/` package, and `panel.py` imports it as `from base_regression import BaseRegression`. That import only resolves when the repo root is on `sys.path`, so `import jjutils.panel` from an installed copy will fail.

### `jjutils.config`

Module-level constants used by the examples: `LOGGING_LEVEL`, `CWD_PATH`, `CSV_PATH` (`data/train.csv`), `DATABASE_PATH` (`data/database.db`), and the `TABLE_APPLICANTS` / `TABLE_JOBS` table definitions. Paths are built off `os.getcwd()`, so they resolve relative to wherever you run from.

## Requirements

Pinned in `requirements.txt`:

```
matplotlib==3.8.0
pandas==1.5.3
seaborn==0.13.0
scikit-learn
statsmodels==0.12.2
openpyxl==3.0.7
```

Plus the per-module extras listed under Installation. `numpy` is imported by `DataProcessor` and `kmeans` and comes in transitively with pandas.

## Development

`Makefile` targets:

```bash
make build    # python3 -m build --sdist --wheel ./
make test     # pytest
make deploy   # twine upload dist/*
make clean    # rm -r build dist
```

CI is `.github/workflows/python_application.yml`: black, pylint, pytest, and isort on push and pull request. It triggers on the `master` branch, but the repo's default branch is `main`, so it does not currently run on pushes to the default branch. There are no test files in the repo, so `make test` collects nothing.

Runnable examples live in `examples/`, and sample data (`train.csv`, `construction.xlsx`, `database.db`) in `data/`.

## Repo hygiene note

Git tracks about 1,045 files, and roughly 1,016 of them are a committed virtual environment / `site-packages` tree. The real source is the 12 or so files listed above. `.gitignore` covers `.venv/` but not whatever directory name the committed env uses. Not changed here, just recorded.

## License

No LICENSE file in the repo.
