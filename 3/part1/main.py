import shapely
from shapely.geometry import LineString, Point
f = open('input.txt', 'r')


points_list_first_wire = []
points_list_second_wire = []
first_wire_path = []
second_wire_path = []
distance = []


for i in f:
    if i != '\n':
        first_wire_path = i.split(',')
    else:
        for i in f:
            second_wire_path = i.split(',')

first_wire_path = [x.replace('\n', '') for x in first_wire_path]
second_wire_path = [x.replace('\n', '') for x in second_wire_path]

def path_walk(path):
    wire_point = [0,0]
    points_list = []
    for step in path:
        if 'R' in step:
            wire_point[0]+=int(step.replace('R', ''))
            points_list.append((wire_point[0],wire_point[1]))
        elif 'U' in step:
            wire_point[1]+=int(step.replace('U', ''))
            points_list.append((wire_point[0],wire_point[1]))
        elif 'L' in step:
            wire_point[0]-=int(step.replace('L', ''))
            points_list.append((wire_point[0],wire_point[1]))
        elif 'D' in step:
            wire_point[1]-=int(step.replace('D', ''))
            points_list.append((wire_point[0],wire_point[1]))
        else:
            print('Bad char, can\'t move')

    return points_list

points_list_first_wire = path_walk(first_wire_path)
points_list_second_wire = path_walk(second_wire_path)

lines1 = LineString(points_list_first_wire)
lines2 = LineString(points_list_second_wire)

int_pt = list(lines1.intersection(lines2))

for point in int_pt:
    distance.append(int(abs(point.x)) + int(abs(point.y)))

print(min(distance))
