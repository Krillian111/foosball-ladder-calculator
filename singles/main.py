#! /usr/bin/env python3

import sys
from Parser import Parser

if len(sys.argv) < 2:
    raise Exception('input file was not provided as argument')

csvFile = sys.argv[1]
Parser().parse(csvFile)




