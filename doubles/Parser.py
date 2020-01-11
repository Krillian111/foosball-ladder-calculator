from doubles.Match import Match

class Parser:
    def parse(self, csvFileName):
        with open(csvFileName) as singlesCsvFile:
            self.skipFirstLine(singlesCsvFile)
            matches = []
            for line in singlesCsvFile:
                if line[-1] == "\n":
                    line = line[:-1]
                playerA1,playerA2,playerB1,playerB2,scoreA,scoreB = line.split(',')
                matches.append(Match(playerA1, playerA2, playerB1, playerB2, int(scoreA), int(scoreB)))
            return matches
    def skipFirstLine(self, csvFile):
        csvFile.readline()