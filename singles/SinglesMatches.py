class SinglesMatches:
    def __init__(self):
        self.games = []

    def addMatch(self, match):
        self.games.append(match)

    def __str__(self):
        result = []
        for index in range(len(self.games)):
            result.append(f"{index}: {self.games[index]}\n")
        return "".join(result)