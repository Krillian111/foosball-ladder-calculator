class SinglesMatch:
    def __init__(self,playerNameA,playerNameB,scoreA,scoreB):
        self.playerNameA = playerNameA
        self.playerNameB = playerNameB
        self.scoreA = scoreA
        self.scoreB = scoreB

    def __str__(self):
        return f"[{self.playerNameA} vs {self.playerNameB} => {self.scoreA} : {self.scoreB}]"