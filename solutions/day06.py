import copy 

with open('../inputs/day6.txt', 'r') as f:
    data = []
    for line in f:
        line = line.split(',')
        data.append(line)
    data = [int(x) for x in data[0]]


def grow(fish_groups: dict, days: int) -> int:
    for _ in range(days):
        birth = copy.deepcopy(fish_groups[0])
        for x in range(len(fish_groups)-1):
            fish_groups[x] = fish_groups[x+1]
        fish_groups[6] += birth
        fish_groups[8] = birth

    total = 0   

    for i in range(len(fish_groups)):
        total += fish_groups[i]
    return total
        

fish_groups_sizes = [data.count(x) for x in range(9)]
fish_groups_age =  [i for i in range(len(fish_groups_sizes))]
fish_groups = dict(zip(fish_groups_age, fish_groups_sizes))
fish_groups2 = copy.deepcopy(fish_groups)

total1 = grow(fish_groups, 80)
total2 = grow(fish_groups2, 256)

print(total1, total2)