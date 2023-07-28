#!/usr/bin/python3
"""Python function that returns data structure repre by JSON"""
import json


def from_json_string(my_str):
    """Return object(data structures) represented by json"""
    return json.loads(my_str)
