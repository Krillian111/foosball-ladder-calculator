from doubles.Player import Player
from operator import attrgetter

class Season:
    def __init__(self, matches):
        self.createPlayers(matches)
        self.updatePlayersWithResults(matches)

    def createPlayers(self, matches):
        self.players = dict()
        for match in matches:
            playerNames = [match.playerNameA1,match.playerNameA2,match.playerNameB1,match.playerNameB2]
            for playerName in playerNames:
                if playerName not in self.players:
                    self.players[playerName] = Player(playerName)

    def updatePlayersWithResults(self, matches):
        for match in matches:
            playerNameA1 = match.playerNameA1
            playerNameA2 = match.playerNameA2
            playerNameB1 = match.playerNameB1
            playerNameB2 = match.playerNameB2
            scoreA = match.scoreA
            scoreB = match.scoreB

            self.updatePlayer(playerNameA1, playerNameA2, playerNameB1, playerNameB2, scoreA, scoreB)
            self.updatePlayer(playerNameA2, playerNameA1, playerNameB1, playerNameB2, scoreA, scoreB)
            self.updatePlayer(playerNameB1, playerNameB2, playerNameA1, playerNameA2, scoreB, scoreA)
            self.updatePlayer(playerNameB2, playerNameB1, playerNameA1, playerNameA2, scoreB, scoreA)

    
    def updatePlayer(self, playerName, partnerName, opponentName1, opponentName2, playerScore, opponentScore):
        player = self.players.get(playerName)
        player.addMatch(partnerName, opponentName1, opponentName2, playerScore, opponentScore)

    def __str__(self):
        result = []
        for player in self.players.values():
            result.append(str(player))
        return "\n".join(result)
