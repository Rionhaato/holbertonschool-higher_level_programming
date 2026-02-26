#!/usr/bin/python3
"""Task 02: Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data into JSON and write it to data.json.

    Args:
        csv_filename (str): Path to the source CSV file.

    Returns:
        bool: True on success, False if an error occurs.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8-sig", newline="") as csv_file:
            rows = list(csv.DictReader(csv_file))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file, indent=4)

        return True
    except (OSError, csv.Error, TypeError, ValueError):
        return False
