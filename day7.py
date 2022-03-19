with open('inputs/day7.txt', 'r') as f:
    data = [line.split(",") for line in f.read().strip().split("\n")]
    crabs =  data[0]
    crabs = [int(x) for x in crabs]

def calculate_fuel(crabs: list, x: int) -> int:
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(crab - x)
    return total_fuel

def calculate_fuel2(crabs: list, x:int) -> int:
    total_fuel = 0
    for crab in crabs:
        d = abs(crab - x)
        total_fuel += (d * d + d)//2
    return(total_fuel)

def solve(crabs: list, function) -> None:
    x = 1
    maxi = max(crabs)  
    fuel_costs = []
    while x != maxi:
        fuel = function(crabs, x)
        fuel_costs.append(fuel)
        x += 1
    print(min(fuel_costs))

solve(crabs, calculate_fuel)
solve(crabs, calculate_fuel2)

        