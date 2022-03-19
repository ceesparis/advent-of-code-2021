import math 

with open('inputs/day9.txt', 'r') as f:
    data = [line.split() for line in f.read().strip().split("\n")]
    data = [[[int(d) for d in line] for line in list] for list in data]
    data = [x for [x] in data]

class Grid:
    def __init__(self, data):
        self.data = data
        self.bassin = []
        self.bassins = []

    def find_surroundings(self, x, y):
        points2compare = []
        location_points2compare = []
        if x > 0:
            points2compare.append(self.data[y][x-1])
            location_points2compare.append((x-1, y))
        if x < (len(self.data[0])-1):
            points2compare.append(self.data[y][x+1])
            location_points2compare.append((x+1, y))
        if y > 0:
            points2compare.append(self.data[y-1][x])
            location_points2compare.append((x, y-1))
        if y < (len(self.data)-1):
            points2compare.append(self.data[y+1][x])
            location_points2compare.append((x, y+1))
        return [points2compare, location_points2compare]

    def check_abs_lows(self):
        absolute_lows = []
        low_points = []
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                point = self.data[y][x]
                surroundings = self.find_surroundings(x, y)
                lowest_surrounding_point = min(surroundings[0])
                if point < lowest_surrounding_point:
                    absolute_lows.append(point)
                    low_points.append((y, x))
        return [absolute_lows, low_points]

    def check_point(self, x, y):
        if self.data[y][x] != 9:
            return True
        return False

def dfs(grid, x, y, counter):
    n = 100
    m = 100
    if y < 0 or y >= n or x < 0 or x >= m or grid[y][x] == 'x' or grid[y][x] == 9:
        return
    else:
        counter.append(grid[y][x])
        grid[y][x] = 'x'
        dfs(grid, x, y+1, counter)
        dfs(grid, x, y-1, counter)
        dfs(grid, x+1, y, counter)
        dfs(grid, x-1, y, counter)
        
    return counter
    

def check_bassins(grid, lowest_points):
    bassins = []
    for lowest_point in lowest_points:
        counter = []
        bassin = dfs(grid, lowest_point[1], lowest_point[0], counter)
        bassins.append(bassin)
    return bassins

                                  
grid = Grid(data)
grid_full = grid.data
absolute = grid.check_abs_lows()
absolute_lows = absolute[0]
total = 0
for low in absolute_lows:
    total += low + 1
print(total)

lows_locations = absolute[1]
bassins = check_bassins(grid_full, lows_locations)
size_bassins = [len(x) for x in bassins]
size_bassins = sorted(size_bassins, reverse=True)
biggest_3 = size_bassins[:3]
print(math.prod(biggest_3))


    



