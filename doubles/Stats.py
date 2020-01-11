class Stats:
    def __init__(self, playerName, matchesFromPlayerPerspective):
        self.playerName = playerName
        self.wins = 0
        self.losses = 0
        self.goalsShot = 0
        self.goalsReceived = 0
        self.updateStatsFromMatches(matchesFromPlayerPerspective)

    def updateStatsFromMatches(self, matchesFromPlayerPerspective):
        for match in matchesFromPlayerPerspective:
            self.goalsShot += match.playerScore
            self.goalsReceived += match.opponentScore
            if match.isWin():
                self.wins += 1
            else:
                self.losses += 1

    def __str__(self):
        return f"{self.playerName}\t(G: {self.wins+self.losses} | W:{self.wins} | L: {self.losses} | G(shot): {self.goalsShot} | G(rec): {self.goalsReceived})"