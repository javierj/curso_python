
ZERO = "0"
FIFTEEN = "15"
THIRTY = "30"
FORTY = "40"
ADV = "Adv"
WIN = "Win"

class Player:
	scores = [ZERO, FIFTEEN, THIRTY, FORTY, ADV, WIN]

	def __init__(self, score = ZERO):
		self.score = self.scores.index(score)

	def getScore(self):
		return self.scores[self.score]

	def winPoint(self, other):
		if other.getScore() == ADV:
			other.score -= 1
			return
		if self.getScore() == FORTY and other.getScore() != FORTY:
			self.score += 2
		else:
			self.score+=1

	def isWinner(self):
		return self.getScore() == WIN
	def hasNoPoints(self):
		return self.getScore() == ZERO


class Match:
	def __init__(self):
		pass
	def playMatch(self, playerA, playerB, scores):
		while not(playerA.isWinner()) and not(playerB.isWinner()):
			if scores.getPlayerWhoScores() == "A" :
				playerA.winPoint(playerB)
			else:
				playerB.winPoint(playerA)
	

class Play:
	def __init__(self, playerWhoScores):
		self.player = playerWhoScores
	def getPlayerWhoScores(self):
		return self.player


	
