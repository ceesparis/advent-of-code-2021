with open('inputs/day10.txt', 'r') as f:
    data = [line for line in f.read().strip().split("\n")]


def check_if_corrupt(line: str):
    openers = ['(', '<', '[', '{']
    cur_op = []
    cur_clos= []
    for element in line:
        if element in openers:
            cur_op.append(element)
        else:
            cur_clos.append(element)
            if ord(cur_clos[-1]) - 1 == ord(cur_op[-1]):
                cur_op.pop()
                continue
            elif ord(cur_clos[-1]) - 2 == ord(cur_op[-1]):
                cur_op.pop()
                continue
            else:
                return cur_clos[-1]

def complete(line: str) -> str:
    openers = ['(', '<', '[', '{']
    cur_op = []
    cur_clos= []
    for element in line:
        if element in openers:
            cur_op.append(element)
        else:
            cur_clos.append(element)
            if cur_clos[-1] == ')' and ord(cur_clos[-1]) - 1 == ord(cur_op[-1]):
                cur_op.pop()
                continue
            elif ord(cur_clos[-1]) - 2 == ord(cur_op[-1]):
                cur_op.pop()
                continue
    return cur_op

def calc_score(line: list) -> int:
    score = 0
    while line:
        x = line.pop()
        score = score * 5
        if x == '(':
            score += 1
        elif x == '[':
            score += 2
        elif x == '{':
            score += 3
        else:
            score += 4
    return score
        
corrupt_data = []
black_list = []
for line in data:
    corrupt_line = check_if_corrupt(line)
    if corrupt_line:
        corrupt_data.append(corrupt_line)
        black_list.append(line)
total = 0

for closer in corrupt_data:
    if closer == ')':
        total += 3
    elif closer == ']':
        total += 57
    elif closer == '}':
        total += 1197
    else:
        total += 25137

print(total)

incomplete_data = [x for x in data if x not in black_list]
missing_parts = []
for line in incomplete_data:
    missing = complete(line)
    missing_parts.append(missing)

scores = []
for part in missing_parts:
    score = calc_score(part)
    scores.append(score)
scores = sorted(scores)
middle = len(scores)//2
print(scores[middle])









