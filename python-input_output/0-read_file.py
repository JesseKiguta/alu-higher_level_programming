#!/usr/bin/python3
"""Defining a func tha read a text"""


def read_file(filename=""):
    """Opening a file using with"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
