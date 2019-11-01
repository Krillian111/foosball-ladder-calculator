class SinglesMatch:
    def __init__(self,playerA,playerB,scoreA,scoreB):
        self.playerA = playerA
        self.playerB = playerB
        self.scoreA = scoreA
        self.scoreB = scoreB

    def __str__(self):
        return f"[{self.playerA} vs {self.playerB} => {self.scoreA} : {self.scoreB}]"