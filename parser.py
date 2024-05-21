"""Parse the chapters' location column into latitude and logitude"""
import sqlite3

from sqlite_utils import Database


db = Database(sqlite3.connect("chapters.db"))
table = db.table("sites")

# Clean location to a new location string which only contains the two numbers
table.convert("location", lambda value: value.removeprefix('{"latitude": ').removesuffix('}').replace('"longitude": ', ''), output="new_location")

# Split the new location into a latitude value and a longitude value
table.convert("new_location", lambda value: float(value.split(',')[0]), output="latitude", output_type=float)
table.convert("new_location", lambda value: float(value.split(',')[1]), output="longitude", output_type=float)
