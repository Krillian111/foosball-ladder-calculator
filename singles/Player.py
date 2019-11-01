from Stats import Stats

class Player:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def addMatch(self, opponentName, playerScore, opponentScore):
        self.matches.append(MatchFromPlayerPerspective(opponentName, playerScore, opponentScore))
    
    def computeStats(self):
        return Stats(self.name, self.matches)

    def __str__(self):
        return f"Player({self.name}, {self.computeStats()})"

    def __eq__(self, other):
        return (type(self) is not type(other)) and (self.name is other.name)

    def __hash__(self):
        return hash(self.name)

class MatchFromPlayerPerspective:
    def __init__(self, opponentName, playerScore, opponentScore):
        self.opponentName = opponentName
        self.playerScore = playerScore
        self.opponentScore = opponentScore
    
    def isWin(self):
        return self.playerScore > self.opponentScore

    def __str__(self):
        return f"Match(vs {self.opponentName} | {self.playerScore} : {self.opponentScore})"