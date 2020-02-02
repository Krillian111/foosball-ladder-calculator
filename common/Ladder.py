from common.multiStageSort import multiStageSort

class Ladder:
    def __init__(self, season):
        playerStats = self.computePlayerStats(season.players)
        self.orderedPlayerStats = self.orderStats(playerStats)
    
    def computePlayerStats(self, players):
        stats = []
        for player in players.values():
            stats.append(player.computeStats())
        return stats

    def orderStats(self, playerStats):
        return multiStageSort(playerStats, (("wins", "desc"), ("goalsShot", "desc"), ("goalsReceived", "asc")))

    def __str__(self):
        header = "NAME\t\t| GAMES\t| WON\t| LOST\t| SHOT\t| RECV\n"
        ladderRows = "\n".join(map(lambda stats: str(stats), self.orderedPlayerStats))
        return header+ladderRows

    def toCsv(self):
        header = "Rank,Name,Games,Wins,Losses,Goals shot,Goals received,%WIN\n"
        ladderRows = "\n".join(map(lambda statsWithIndex: f"{statsWithIndex[0]+1},{statsWithIndex[1].toCsv()}", enumerate(self.orderedPlayerStats)))
        return header+ladderRows