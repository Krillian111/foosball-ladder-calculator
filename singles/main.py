#! /usr/bin/env python3

import sys
from Parser import Parser
from Season import Season
from Ladder import Ladder

if len(sys.argv) < 2:
    raise Exception('input file was not provided as argument')

csvFile = sys.argv[1]
matches = Parser().parse(csvFile)

season = Season(matches)
ladder = Ladder(season)

print(ladder)




