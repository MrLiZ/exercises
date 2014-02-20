#!/usr/bin/env python
#-*- coding: utf-8 -*-


import json
import argparse 
import traceback


def parser():
    """"""
    parser = argparse.ArgumentParser(description="JSON menu ids")
    parser.add_argument("input_file", type=str, help="Test file to load")
    return parser.parse_args()


def count_ids(menu):
    """"""
    total = 0
    items = menu.get("items", None)
    if items:
        for item in items:
            if item and "label" in item and "id" in item:
                total += item["id"]
    return total


if __name__ == "__main__":

    args = parser()
    try:
        with open(args.input_file, "r") as f:
            for line in f:
                while True:
                    try:
                        menu = json.loads(line)
                        print(count_ids(menu.get("menu", [])))
                        break
                    except ValueError:
                        line += next(f)
    except IOError:
        print(traceback.format_exc())
