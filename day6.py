import copy 

with open('inputs/day6.txt', 'r') as f:
    data = []
    for line in f:
        line = line.split(',')
        data.append(line)
    data = [int(x) for x in data[0]]

def check_schools(schools) -> bool:
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

        
    

# def merge_schools(school, schools: list) -> list:
#     copy_schools = copy.deepcopy(schools)
#     for i in range(len(copy_schools)):
#         print(schools[i].age)
#     print('\n')
    

class Fish:
    def __init__(self, age):
        self.age = age

    def create_fish(self):
        new_fish = Fish(8)
        return(new_fish)

    def get_older(self):
        if self.age == 0:
            new_fish = self.create_fish()
            self.age = 6
            return new_fish
        self.age -= 1

class School:
    def __init__(self, size, age):
        self.size = size
        self.age = age
    
    def create_new_school(self):
        new_school = School(self.size, 8)
        return new_school

    def get_older(self):
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
    # new_ages = [x.age for x in new_fishes]
    # old_ages = [x.age for x in fishes]
    return(fishes + new_fishes)

def merge_schools(schools: list) -> list:
    copy_schools = copy.deepcopy(schools)
    for i in range(len(copy_schools)):
        pass



# fishes =  [Fish(x) for x in data]
# for _ in range(80):
#     fishes = new_day(fishes)
# print(len(fishes))

fish_groups_sizes = [data.count(x) for x in range(9)]
print(fish_groups_sizes)
fish_groups_age =  [i for i in range(len(fish_groups_sizes))]

fish_groups = dict(zip(fish_groups_age, fish_groups_sizes))
print(fish_groups)

fishes = [data.count(x) for x in range(9)]
for _ in range(256):
    # tmp=fishes[0]
    # fishes = fishes[1:] + [tmp]
    # fishes[6] += tmp
    birth = copy.deepcopy(fish_groups[0])
    for x in range(len(fish_groups)-1):
        fish_groups[x] = fish_groups[x+1]
    fish_groups[6] += birth
    fish_groups[8] = birth

total = 0
# for i in range(len(fishes)):
#     total += fishes[i]
# print(total)    

for i in range(len(fish_groups)):
    total += fish_groups[i]

print(total)

# for age in fish_groups_ages:
#     if age == 0:
#         fish_groups_sizes[age]

# fish_groups = [data.count(x) for x in range(9)]

# schools = []



# for i in range(len(fish_groups)):
#     if fish_groups[i] != 0:
#         new_school = School(fish_groups[i], i)
#         schools.append(new_school)

# for _ in range((4)):
#     schools = new_day(schools)
#     dupes = check_schools(schools)
#     schools = remove_dupes(schools, dupes)
#     # print([x.size for x in schools])






