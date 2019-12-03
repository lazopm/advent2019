input_lines = open('./input.txt','r').readlines()

def getPoints(wire_line):
    wire = wire_line.strip().split(',')
    length = 0
    last_point = (0,0)
    points = {}
    for instruction in wire:
        direction = instruction[0]
        for _ in range(int(instruction[1:])):
            x, y = last_point
            if direction == 'U':
                point = (x, y+1)
            elif direction == 'D':
                point = (x, y-1)
            elif direction == 'R':
                point = (x+1, y)
            elif direction == 'L':
                point = (x-1, y)
            length+=1
            last_point = point
            if point not in points:
                points[point] = length
    return points


pointMaps = list(map(getPoints, input_lines))
intersections = set.intersection(*[set(m.keys()) for m in pointMaps])
# part 1
min_distance = min([sum([abs(n) for n in i]) for i in intersections])
# part 2
min_length = min([sum([m[i] for m in pointMaps]) for i in intersections])

print(min_distance)
print(min_length)
