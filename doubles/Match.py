class Match:
    def __init__(self,playerNameA1,playerNameA2,playerNameB1,playerNameB2,scoreA,scoreB):
        self.playerNameA1 = playerNameA1
        self.playerNameA2 = playerNameA2
        self.playerNameB1 = playerNameB1
        self.playerNameB2 = playerNameB2
        self.scoreA = scoreA
        self.scoreB = scoreB

    def __str__(self):
        return f"[{self.playerNameA1}/{self.playerNameA2} vs {self.playerNameB1}/{self.playerNameB2} => {self.scoreA} : {self.scoreB}]"