from collections import deque 
input_lines = open('./input.txt','r').readlines()

class Wire:
    def __init__(self, wire_line):
        # key is the pont, value is a set of connected points 
        self.points = {} 

        # add initial point
        self.points[(0,0)] = set() 
        self.last_point = (0,0) 

        instructions = wire_line.strip().split(',')
        for instruction in instructions:
            direction = instruction[0]
            distance = int(instruction[1:])
            for _ in range(distance):
                self.add_point(direction)

    def add_point(self, direction):
        x,y = self.last_point 

        if direction == 'U':
            point = (x, y+1)
        elif direction == 'D':
            point = (x, y-1)
        elif direction == 'R':
            point = (x+1, y)
        elif direction == 'L':
            point = (x-1, y)

        # if we are crossing an existing point add edge to last point  
        if point in self.points:
            self.points[point].add(self.last_point)
        else:
            # add new point with an edge to last point
            self.points[point] = set([self.last_point])

        # we want to connect point both ways, so add a backwards edge to new point
        self.points[self.last_point].add(point)

        self.last_point = point

    def to_set(self):
        return set(self.points.keys())

    def shortest_path_search(self, search_points):
        found_distances = {}
        seen = set()

        # start our queue at 0,0 
        queue = deque()
        queue.append(((0,0), 0))

        while len(queue) > 0 and len(search_points) > len(found_distances):
            # pull next item from the queue
            (point, depth) = queue.popleft()
            # out points connect both ways so we need to keep track of visited points
            # to prevent going backwards and infinite loops 
            seen.add(point)

            # save depth if we are searching for this point
            if point in search_points:
                found_distances[point] = depth

            # add all connected points to the queue
            for edge_point in self.points[point]
                if edge_point not in seen:
                    queue.append((edge_point, depth + 1))
        return found_distances;




wire_a = Wire(input_lines[0])
wire_b = Wire(input_lines[1])

intersections = wire_a.to_set().intersection(wire_b.to_set())

# remove start position
intersections.remove((0,0))
intersections = list(intersections)

# part 1
print('closest intersection:')
print(min([abs(i[0])+abs(i[1]) for i in intersections]))

# search for shortest paths to intersections 
wire_a_distances = wire_a.shortest_path_search(intersections)
wire_b_distances = wire_b.shortest_path_search(intersections)

sums = [wire_a_distances[i] + wire_b_distances[i] for i in intersections]
min_sum = min(sums)
p = intersections[sums.index(min_sum)]

print('shortest path:')
print(p)
print(min_sum)


