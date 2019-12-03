from collections import OrderedDict
input_lines = open('./input.txt','r').readlines()

class Wire:
    def __init__(self, wire_line):
        self.last_point = (0,0)
        self.points = OrderedDict() 
        instructions = wire_line.strip().split(',')
        for instruction in instructions:
            direction = instruction[0]
            distance = int(instruction[1:])
            for _ in range(distance):
                self.addPoint(direction)

    def addPoint(self, direction):
        x,y = self.last_point
        if direction == 'U':
            self.last_point = (x, y+1)
        elif direction == 'D':
            self.last_point = (x, y-1)
        elif direction == 'R':
            self.last_point = (x+1, y)
        elif direction == 'L':
            self.last_point = (x-1, y)

        self.points[self.last_point] = 0

    def toSet(self):
        return set(self.points.keys())

wires = map(Wire, input_lines)
intersections = set.intersection(*map(lambda wire:  wire.toSet(), wires))
min_distance = min(map(lambda p: abs(p[0]) + abs(p[1]), intersections))

print(min_distance)
