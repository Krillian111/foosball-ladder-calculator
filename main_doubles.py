#! /usr/bin/env python3

import sys
from doubles.Parser import Parser
from doubles.Season import Season
from common.Ladder import Ladder

if len(sys.argv) < 2:
    raise Exception('input file was not provided as argument')

csvFile = sys.argv[1]
matches = Parser().parse(csvFile)

season = Season(matches)
ladder = Ladder(season)

print("=========================")
print(ladder)
print("=========================")
outputFileName = sys.argv[2]
print('redirecting as csv to:' + str(outputFileName))
outputFile = open(outputFileName, mode='w')
print(ladder.toCsv(), file=outputFile)
outputFile.close()




