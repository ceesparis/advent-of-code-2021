with open('inputs/day2.txt', 'r') as f: 
    data = [line.strip('\n').split() for line in f]

for element in data: 
    element[1]=int(element[1])

x, y, y1 = 0, 0, 0

for direction, units in data: 
    if direction == 'forward':
        x += units
        y1 += y * units
    elif direction == 'up':
        y -= units
    else: 
        y += units

print(x * y)
print(x * y1)
