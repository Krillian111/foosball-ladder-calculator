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
        return f"{self.playerName}\t| {self.wins+self.losses}\t| {self.wins}\t| {self.losses}\t |{self.goalsShot}\t| {self.goalsReceived}\t | {round(self.wins/(self.wins+self.losses), 3)}"

    def toCsv(self):
        return ",".join(map(lambda value: str(value), [self.playerName,(self.wins+self.losses),self.wins,self.losses,self.goalsShot,self.goalsReceived, round(self.wins/(self.wins+self.losses), 2)]))