# pyladies-datasette

## Installation

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Chapter information

Take the `config.yml` from PyLadies repo. Strip data other than the chapters and save as `chapters.yml`.

Convert yaml file to a SQLite database:

    yaml-to-sqlite chapters.db sites chapters.yml

## Serve chapter information with Datasette

Enter:

     datasette chapters.db
