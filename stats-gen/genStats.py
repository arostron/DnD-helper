from random import randint
import argparse

roll_d = lambda x: randint(1,x)

def top_3_of_4_d6():
	rolls = [roll_d(6) for i in range(4)]
	return sum(rolls) - min(rolls)

def player_stats():
	return sorted([ top_3_of_4_d6() for i in range(6)], reverse=True)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', help='Output filename', type=str, default="stats.txt")
	parser.add_argument('-n', type=int, default=1, help='How many player stats to generate')
	args = parser.parse_args()

	with open(args.f, 'a') as f:
		for i in range(args.n):
			stats = player_stats()
			f.write("{}\n".format(stats))
			print("Stats: ", stats)
