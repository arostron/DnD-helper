from random import randint as r

def rollDice(d=6):
    return r(1,d)

def genStat(n=4, d=6):
    # roll and sum n dice then subtract minimum
    total = 0
    rolls = []
    for i in range(n):
        r = rollDice(d);
        total += r
        rolls.append(r)
    #print("Rolled: ", rolls)
    total-= min(rolls)
    return total

def genStats(n=6):
    stats = []
    for i in range(n):
        stats.append(genStat())
    return sorted(stats,reverse=True)


print("Here are your standard DnD stats")
print(genStats())
