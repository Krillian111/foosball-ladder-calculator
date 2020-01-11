from doubles.Stats import Stats

class Player:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def addMatch(self, parterName, opponentName1, opponentName2, playerScore, opponentScore):
        self.matches.append(MatchFromPlayerPerspective(parterName, opponentName1, opponentName2, playerScore, opponentScore))
    
    def computeStats(self):
        return Stats(self.name, self.matches)

    def __str__(self):
        return f"Player({self.name}, {self.computeStats()})"

    def __eq__(self, other):
        return (type(self) is not type(other)) and (self.name is other.name)

    def __hash__(self):
        return hash(self.name)

class MatchFromPlayerPerspective:
    def __init__(self, parterName, opponentName1, opponentName2, playerScore, opponentScore):
        self.partnerName = parterName
        self.opponentName1 = opponentName1
        self.opponentName2 = opponentName2
        self.playerScore = playerScore
        self.opponentScore = opponentScore
    
    def isWin(self):
        return self.playerScore > self.opponentScore

    def __str__(self):
        return f"Match(/w {self.partnerName} vs {self.opponentName1}/{self.opponentName2} | {self.playerScore} : {self.opponentScore})"