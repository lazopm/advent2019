input = open('./input.txt','r').read()
input_ints = list(map(lambda x: int(x.strip()), input.split(',')))

# operations
ADD = 1
MUL = 2

def runProgram(ints):
	ints = ints.copy()
	cursor = 0
	while ints[cursor] != 99:
		op = ints[cursor]
		a = ints[ints[cursor+1]]
		b = ints[ints[cursor+2]]
		pos = ints[cursor+3]
		if op == ADD:
			ints[pos] = a + b
		elif op == MUL:
			ints[pos] = a * b
		else:
			raise Exeption('invalid op: ' + str(op))
		cursor += 4
	return ints[0]

def bruteForceMatch(result, ints):
	matches = []
	ints = ints.copy();
	for i in range(0,100):
		for k in range(0, 100):
			ints[1] = i
			ints[2] = k
			if (runProgram(ints) == result):
				matches.append((i, k));
	return matches


r = bruteForceMatch(19690720, input_ints)

#input_ints[1] = 82 
#input_ints[2] = 50 
#r = runProgram(input_ints);
print(runProgram([1,1,1,4,99,5,6,0,99]))
print(r)
