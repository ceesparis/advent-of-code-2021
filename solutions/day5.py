import copy

with open('../inputs/day5.txt', 'r') as f:
    # data = list(f)
    data = [line.split(" -> ") for line in f.read().strip().split("\n")]
    data = [[[int(s[0]), int(s[1])] for s in (x.split(",") for x in line)] for line in data]

hor_ver_lines = []
diag_points = []
for line in data:
    begin_line = line[0]
    end_line = line[1]
    complete_line = []
    complete_line.append(copy.deepcopy(begin_line))
    if begin_line[0] != end_line[0] and begin_line[1] != end_line[1]:
        diag_points.append([begin_line, end_line])
        continue
    while begin_line != end_line:
        i = 1 if begin_line[0] == end_line[0] else 0
        nxt = []     
        if begin_line[i] < end_line[i]:
            begin_line[i] += 1
            nxt = copy.deepcopy(begin_line)
            complete_line.append(nxt)
        else:
            begin_line[i] -= 1
            nxt = copy.deepcopy(begin_line)
            complete_line.append(nxt)
    
    hor_ver_lines.append(complete_line)
print(hor_ver_lines)
flat_list = [item for sublist in hor_ver_lines for item in sublist]


danger_spots = 0
already_seen = []
for point in flat_list:
    if point in already_seen:
        print('already seen')
        continue
    if flat_list.count(point) > 1:
        danger_spots += 1
        already_seen.append(point)
print(danger_spots)

# part two 

diag_lines = []
for point in diag_points:
    begin_point = point[0]
    end_point = point[1]
    complete_line = []
    complete_line.append(copy.deepcopy(begin_point))

    while begin_point != end_point:
        nxt = []     
        if begin_point[0] < end_point[0]:
            begin_point[0] += 1
        else:
            begin_point[0] -= 1

        if begin_point[1] < end_point[1]:
            begin_point[1] += 1
        else:
            begin_point[1] -= 1

        nxt =  copy.deepcopy(begin_point)
        complete_line.append(nxt)
    
    diag_lines.append(complete_line)


flat_diag_list = [item for sublist in diag_lines for item in sublist]
all_lines = flat_list + flat_diag_list

danger_spots = 0
already_seen = []
for point in all_lines:
    if point in already_seen:
        continue
    if all_lines.count(point) > 1:
        danger_spots += 1
        already_seen.append(point)
print(danger_spots)
