from random import randint

d = lambda x: randint(1,x)


def great_weapon(modifier=3):
	damage = 0
	for i in range(2):
		roll = d(6)
		if roll in [1,2]:
			roll = d(6)
		damage += roll
	damage += modifier
	return damage



# source https://realpython.com/python-histograms/
def count_elements(seq) -> dict:
    """Tally elements from `seq`."""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = count_elements(seq)
    for k in sorted(counted):
        print('{0:5d} {1}'.format(k, '+' * counted[k]))


def bunch_calls(func, x):
	return [func() for i in range(x)]


def histo(x):
	ascii_histogram(bunch_calls(great_weapon, x))


if __name__ == "__main__":
	# display a greate_weapon damage histogram over 200 rolls
	ascii_histogram(bunch_calls(great_weapon, 200))

