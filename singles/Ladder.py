from multiStageSort import multiStageSort

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
        return "\n".join(map(lambda stats: str(stats), self.orderedPlayerStats))
