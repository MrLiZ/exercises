#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import os


if __name__ == "__main__":

    arg = sys.argv[1]
    print(os.path.getsize(arg))
    
