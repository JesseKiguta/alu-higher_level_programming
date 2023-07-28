#!/usr/bin/python3
"""Python a function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """write an object from json file
    args:
        filename (str): The name of the file.
    Results:
        returns the json
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
