import copy


def most_common_bit(data: list, x: int) -> str:
    ones, zeroes = 0, 0
    for element in data:
        first_element = element[x]
        if first_element:
            ones += 1
        else:
            zeroes += 1
    return '1' if zeroes <= ones else '0'


def convert_to_dec(bin_num: list) -> list:
    bin_num = [str(x) for x in bin_num]
    bin_num = "".join(bin_num)
    bin_num = int(bin_num, 2)
    return bin_num


def filter_row(data: list, copied_data: list, x: int, y: int) -> list:
    for element in data:
        if element[x] != y:
            if element in copied_data:
                copied_data.remove(element)
    return copied_data


with open('../inputs/day3.txt', 'r') as f:
    data = [list(line.strip()) for line in f]
    for i in range(len(data)):
        data[i] = [int(x) for x in data[i]]

# part one

gamma, epsilon = [], []
for i in range(len(data[0])):
    num = most_common_bit(data, i)
    gamma.append(num)
gamma = "".join(gamma)
for element in gamma:
    if element == '1':
        epsilon.append('0')
    else:
        epsilon.append('1')
epsilon = "".join(epsilon)

print(f'part one: {int(gamma, 2) * int(epsilon, 2)}')

# part two

# determine the oxygen generator rating
i = 0
copied_data = copy.deepcopy(data)

while len(copied_data) > 1:
    most_common = None
    zeroes, ones = 0, 0
    zero_list, one_list, blacklist = [], [], []
    num = most_common_bit(copied_data, i)
    copied_data = filter_row(data, copied_data, i, int(num))
    i += 1

oxgen = convert_to_dec(copied_data[0])

# determine the CO2 scrubber rating
copied_data = copy.deepcopy(data)
i = 0

while len(copied_data) > 1:
    least_common = None
    zeroes, ones = 0, 0
    num = most_common_bit(copied_data, i)
    num = 0 if num == '1' else 1
    copied_data = filter_row(data, copied_data, i, num)
    i += 1

coscrub = convert_to_dec(copied_data[0])
print(f'part two: {coscrub * oxgen}')
