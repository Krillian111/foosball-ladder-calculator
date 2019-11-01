from Player import Player
from operator import attrgetter

class Season:
    def __init__(self, matches):
        self.createPlayers(matches)
        self.updatePlayersWithResults(matches)

    def createPlayers(self, matches):
        self.players = dict()
        for match in matches:
            playerNameA = match.playerNameA
            playerNameB = match.playerNameB
            if playerNameA not in self.players:
                self.players[playerNameA] = Player(playerNameA)
            if playerNameB not in self.players:
                self.players[playerNameB] = Player(playerNameB)

    def updatePlayersWithResults(self, matches):
        for match in matches:
            playerNameA = match.playerNameA
            playerNameB = match.playerNameB
            scoreA = match.scoreA
            scoreB = match.scoreB

            self.updatePlayer(playerNameA, playerNameB, scoreA, scoreB)
            self.updatePlayer(playerNameB, playerNameA, scoreB, scoreA)
    
    def updatePlayer(self, playerName, opponentName, playerScore, opponentScore):
        player = self.players.get(playerName)
        player.addMatch(opponentName, playerScore, opponentScore)

    def __str__(self):
        result = []
        for player in self.players.values():
            result.append(str(player))
        return "\n".join(result)
