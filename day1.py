
with open("inputs/day1.txt", "r") as f:
    data = [int(line) for line in f]

increasments = 0
for i in range(len(data)):
    if data[i] > data[i-1]:
        increasments += 1
print(increasments)

triples = []


def three_seg(x: int, number_list: list) -> None:
    if x+2 < len(number_list):
        new_segment = [number_list[x], number_list[x+1], number_list[x+2]]
        triples.append(new_segment)


file_content = [three_seg(x, data) for x in range(len(data))]

triples = [sum(x) for x in triples]

increasments = 0
for i in range(len(triples)):
    if triples[i] > triples[i-1]:
        increasments += 1
print(increasments)
