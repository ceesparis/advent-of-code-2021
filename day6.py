import copy 

with open('inputs/day6.txt', 'r') as f:
    data = []
    for line in f:
        line = line.split(',')
        data.append(line)
    data = [int(x) for x in data[0]]

def check_schools(schools: list) -> list:
    ages = [school.age for school in schools]
    seen = set()
    dupes = [x for x in ages if x in seen or seen.add(x)]
    return dupes

def remove_dupes(schools: list, dupes:list) -> list:
    schools_copy = copy.deepcopy(schools)
    if dupes:
        for dupe in dupes:
            size = 0
            for i in range(len(schools)):
                if schools[i].age == dupe:
                    size += schools[i].size
                    schools[i].size = size
            new_school = School(size, dupe)
            schools_copy.append(new_school)
    return(schools_copy)

    
class Fish:
    def __init__(self, age):
        self.age = age

    def create_fish(self):
        new_fish = Fish(8)
        return(new_fish)

    def get_older(self) -> None:
        if self.age == 0:
            new_fish = self.create_fish()
            self.age = 6
            return new_fish
        self.age -= 1

class School:
    def __init__(self, size, age):
        self.size = size
        self.age = age
    
    def create_new_school(self) -> object:
        new_school = School(self.size, 8)
        return new_school

    def get_older(self) -> None:
        if self.age == 0:
            new_school = self.create_new_school()
            self.age = 6
            return new_school
        self.age -= 1
    

def new_day(fishes: list) -> list:
    new_fishes = []
    for fish in fishes:
        new_fish = fish.get_older()
        if new_fish:
            new_fishes.append(new_fish)
    return(fishes + new_fishes)

fish_groups_sizes = [data.count(x) for x in range(9)]
fish_groups_age =  [i for i in range(len(fish_groups_sizes))]
fish_groups = dict(zip(fish_groups_age, fish_groups_sizes))

fishes = [data.count(x) for x in range(9)]
for _ in range(256):
    birth = copy.deepcopy(fish_groups[0])
    for x in range(len(fish_groups)-1):
        fish_groups[x] = fish_groups[x+1]
    fish_groups[6] += birth
    fish_groups[8] = birth

total = 0   

for i in range(len(fish_groups)):
    total += fish_groups[i]

print(total)
