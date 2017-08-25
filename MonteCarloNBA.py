import random

consec_loss_season = 0  # Seasons where there are consecutive losses
n = 1000000  # Number of seasons to simulate

for n in range(n):
	last_game = 1  # Result of the last game "played". 1 = win, 0 = loss.
	for i in range(82):  # Simulating each game in a season
		game = random.random()
		if game < 0.80:  # Win and continue to next game
			last_game = 1
		elif game >= 0.80:  # Lose and check if previous game was a loss
			if last_game == 0:  # If last game was lost, count as a loss season
				consec_loss_season += 1
				break
			last_game = 0

print('Probability that GSW does not lose consecutively: %s' %
	  ((n - consec_loss_season) / n))
