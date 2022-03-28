
from tracemalloc import start


with open('inputs/day12.txt', 'r') as f:
    cave_system = [set(line.split('-')) for line in f.read().strip().split("\n")]

start_points = [x for x in cave_system if 'start' in x]
outer = {'end', 'start'}

def find_next(connect, cave_system):
    return [x for x in cave_system if len(x.intersection(connect)) == 1 and x.intersection(connect).issubset(outer) == False]


def dfs(connect, cave_system, routes, route):
    if 'end' in connect:
        route.append(connect)
        print(route)
        routes.append(route)
        # route = []
        return routes
    else:
        route.append(connect)
        connect = find_next(connect, cave_system)
        connect = [x for x in connect if x not in route]
        connect = connect[0]
        dfs(connect, cave_system, routes, route)


for start_point  in start_points:
    routes = []
    route = []
    current = start_point
    routes = dfs(current, cave_system, routes, route)
    print(routes)


















# def get_routes(start, cave_system):
#     prev_point = 'start'
#     possible_routes = []
#     pos_route = [start]
#     for connect in cave_system:
#         if len(connect.intersection(start)) != 0 and prev_point not in connect:
#             pos_route.append(connect)
#             prev_point = connect.intersection(start)
#         if 'end' in connect:
#             possible_routes.append(pos_route)
#             pos_route = [start]
#     return possible_routes


    


# for connect in cave_system:
#     if 'start' in connect:
#         routes_from_start = get_routes(connect, cave_system)
#         print(routes_from_start)