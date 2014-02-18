#!/usr/bin/env python
#-*- coding: utf-8 -*-


import argparse
import traceback


def parser():
    """"""
    parser = argparse.ArgumentParser(description="Reverse words challenge")
    parser.add_argument("input_file", type=str, help="Input file to process")
    return parser.parse_args()


if __name__ == "__main__":

    args = parser()
    try:
        with open(args.input_file, "r") as f:
            for line in f:
                splitted = line.split()
                if splitted:
                    print(" ".join(reversed(splitted)))
    except IOError as err:
        print(traceback.format_exc())
