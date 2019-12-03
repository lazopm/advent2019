input_lines = open('./input.txt','r').readlines()

def getPointSet(wire_line):
    wire = wire_line.strip().split(',')
        x = 0
        y = 0
        points = set()
        for instruction in wire:
            direction = instruction[0]
                distance = int(instruction[1:])
                if direction == 'U':
                    for py in range(y+1, y+1+distance):
                        points.add((x, py))
                        y+=distance
                elif direction == 'D':
                    for py in range(y-distance, y):
                        points.add((x, py))
                        y-=distance
                elif direction == 'R':
                    for px in range(x+1, x+1+distance):
                        points.add((px, y))
                        x+=distance
                elif direction == 'L':
                    for px in range(x-distance, x):
                        points.add((px, y))
                        x-=distance
        return points


pointSets = map(getPointSet, input_lines)
intersections = set.intersection(*pointSets)
min_distance = min(map(lambda p: abs(p[0]) + abs(p[1]), intersections))

print(min_distance)
