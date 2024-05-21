# pyladies-datasette

## Installation

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Install plugins for geo and maps

```
datasette install datasette-cluster-map
datasette install datasette-geojson
```

## Chapter information

Take the `config.yml` from PyLadies repo. Strip data other than the chapters and save as `chapters.yml`.

Convert yaml file to a SQLite database:

    yaml-to-sqlite chapters.db sites chapters.yml

## Parse the location data

Run: `python parser.py`

## Serve chapter information with Datasette

Enter:

     datasette chapters.db

