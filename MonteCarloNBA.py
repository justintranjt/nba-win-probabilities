import random
for i in range(10):
	consec_loss_season = 0
	n = 1000000

	for n in range(n):
		last_game = 1
		for i in range(82):
			game = random.random()
			if game < 0.80:
				last_game = 1
			elif game >= 0.80:
				if last_game == 0:
					consec_loss_season += 1
					break
				last_game = 0

	print('Probability that GSW does not lose consecutively: %s' %
		  ((n - consec_loss_season) / n))
