from lib2to3.pygram import pattern_grammar


with open('inputs/day8.txt', 'r') as f:
    data = [line.strip().split(" ") for line in f.read().strip().split("\n")]
    data = [[line[:10], line[11:]] for line in data]

# part one 
outputs = [line[1] for line in data]
outputs_lengths = [[len(x) for x in line] for line in outputs]
looked_for = [2, 3, 4, 7]
x = 0
for output in outputs_lengths:
    for number in output:
        if number in looked_for:
            x += 1
print(x)

# part two 
signal_patterns = [(line[0]) for line in data]
signal_patterns = [[set(x) for x in line] for line in signal_patterns]
outputs = [[set(x) for x in line] for line in outputs]
# print(signal_patterns[0])

 
def get_known(signal_pattern):
    four, one, seven, eight = set, set, set, set
    for pattern in signal_pattern:
        if len(pattern) == 4:
            four = pattern
        elif len(pattern) == 2:
            one = pattern
        elif len(pattern) == 3:
            seven = pattern
        elif len(pattern) == 7:
            eight = pattern
    return [one, four, seven, eight]

def get_unkown(signal_pattern: list, known_nums: list) -> list:
    zero, two, three, five, six, nine = set, set, set, set, set, set 
    unknown_numbers = [x for x in signal_pattern if x not in known_nums]
    one = known_nums[0]
    four = known_nums[1]
    seven = known_nums[2]
    for pattern in unknown_numbers:
        if four.issubset(pattern):
            nine = pattern
    for pattern in unknown_numbers:
        if len(pattern) == 5:
            if seven.issubset(pattern):
                three = pattern
            elif pattern.issubset(nine):
                 five = pattern
            else:
                two = pattern
    unknown_numbers = [x for x in unknown_numbers if x not in [two, five, three, nine]]
    for pattern in unknown_numbers:
        if one.issubset(pattern):
            zero = pattern
        else:
            six = pattern

    return([zero, known_nums[0], two, three, known_nums[1], five, six, known_nums[2], known_nums[3], nine])
    
numbers = []
for i in range(len(signal_patterns)):
    number = []
    known_numbers = get_known(signal_patterns[i])
    total = get_unkown(signal_patterns[i], known_numbers)
    for output in outputs[i]:
        display = total.index(output)
        number.append(str(display))
    numbers.append(number)
    new_numbers = [int("".join(sequence)) for sequence in numbers]
print(sum(new_numbers))
    
        





    

