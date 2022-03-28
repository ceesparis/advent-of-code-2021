import copy

with open('../inputs/day11.txt', 'r') as f: 
    data = [line.split() for line in f.read().strip().split("\n")]
    data = [[[int(d) for d in line] for line in list] for list in data]
    data = [x for [x] in data]


class School:

    def __init__(self, data):
        self.grid = data
        self.flashes = 0
        self.new_zeroes = []
        self.total_flash = False


    def get_surroundings(self, y: int, x:int) -> list:
        location_points2compare = []
        if x > 0 and y > 0:
            location_points2compare.append((y-1, x-1))
        if x < (len(self.grid[0])-1) and y < (len(self.grid)-1):
            location_points2compare.append((y+1, x+1))
        if x > 0 and y < (len(self.grid)-1):
            location_points2compare.append((y+1, x-1))
        if x < (len(self.grid[0])-1) and y > 0:
            location_points2compare.append((y-1, x+1))
        if x > 0:
            location_points2compare.append((y, x-1))
        if x < (len(self.grid[0])-1):
            location_points2compare.append((y, x+1))
        if y > 0:
            location_points2compare.append((y-1, x))
        if y < (len(self.grid)-1):
            location_points2compare.append((y+1, x))
        return location_points2compare
    
    def check_all(self) -> None:
        total = 0
        for line in self.grid:
            total += sum(line)
            if total > 0:
                break
        if total == 0:
            self.total_flash = True


    def update(self, y: int, x: int) -> None:
        if (y, x) in self.new_zeroes:
            pass
        elif self.grid[y][x] != 9:
            self.grid[y][x] += 1
        else:
            self.flashes += 1
            self.grid[y][x] = 0
            self.check_all()
            self.new_zeroes.append((y, x))
            surroundings = self.get_surroundings(y, x)
            for point in surroundings:
                self.update(point[0], point[1])


    def new_step(self) -> None:
        self.new_zeroes = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                self.update(y, x)
    

    def visualize(self) -> None:
        print('\n')
        for line in self.grid:
            print(f'{line}\n')
        print('\n')

changed_data = copy.deepcopy(data)
octos = School(changed_data)

for i in range(100):
    octos.new_step()
print(octos.flashes)

steps = 0
octos = School(data)
while octos.total_flash == False:
    octos.new_step()
    steps += 1

print(steps)

