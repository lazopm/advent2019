from math import floor

def calcFuel(weight):
	total = 0
	lastFuel = floor(weight/3) - 2
	while lastFuel > 0:
		total += lastFuel
		lastFuel = floor(lastFuel/3) - 2
	return total


total = 0;
f = open('./input.txt', 'r')
for line in f: 
	line = line.strip();
	if len(line) > 0:
		total += calcFuel(int(line))

print(total)


