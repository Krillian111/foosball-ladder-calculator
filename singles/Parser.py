from SinglesMatches import SinglesMatches
from SinglesMatch import SinglesMatch

class Parser:
    def parse(self, csvFileName):
        with open(csvFileName) as singlesCsvFile:
            self.skipFirstLine(singlesCsvFile)
            matches = SinglesMatches()
            for line in singlesCsvFile:
                playerA,playerB,scoreA,scoreB = line[:-1].split(',')
                matches.addMatch(SinglesMatch(playerA, playerB, scoreA, scoreB))
            print(matches)
            # for each result
            # add win for winner with score
            # add loss for loser with score
            
            # sort players for table
            # print table
    def skipFirstLine(self, csvFile):
        csvFile.readline()