filename = '/Users/alisonburgess/Documents/advent of code/2021/day12/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)



def build_graph(all_lines):
    path_map = {}
    for line in all_lines:
        points = line.split("-")

        if points[0] not in path_map:
            path_map[points[0]] = [points[1]]
        else:
            cur_list = path_map[points[0]]
            cur_list.append(points[1])
            path_map[points[0]] = cur_list
        
        # make sure the second point maps back to the first one
        if points[1] not in path_map:
            path_map[points[1]] = [points[0]]
        else:
            cur_list = path_map[points[1]]
            cur_list.append(points[0])
            path_map[points[1]] = cur_list

    return path_map


def find_paths_pt1(path_map, start, end, path=[]):
    newpaths = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []

    for node in path_map[start]:
        if node not in path or node.isupper():
            newpaths = find_paths_pt1(path_map, node, end, path)
        
        for newpath in newpaths:
            if newpath not in paths:
                paths.append(newpath)
    return paths


def setup_small_caves(path_map):
    small_caves = []
    for letter, paths in path_map.iteritems():
        if letter not in small_caves and letter.islower() and letter!='start' and letter!='end':
            small_caves.append(letter)
    
    return small_caves


def find_paths_pt2(path_map, start, end, small_caves, path = []):
    newpaths = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []

    for node in path_map[start]:
        # see if an existing small cave already exists twice
        small_node = False
        if node != 'start' and node != 'end' and node.islower():
            for letter in small_caves:
                if (letter == node and path.count(letter) < 2):
                    small_node = True
            
            for letter in small_caves:
                if letter != node and path.count(letter) == 2:
                    small_node = False

        if node not in path or node.isupper() or small_node:
            newpaths = find_paths_pt2(path_map, node, end, small_caves, path)

        for newpath in newpaths:
            if newpath not in paths:
                paths.append(newpath)

    return paths


def part1(all_lines):
    path_map = build_graph(all_lines)
    all_paths = find_paths_pt1(path_map, 'start', 'end')
    print(len(all_paths))

def part2(all_lines):
    path_map = build_graph(all_lines)
    small_caves = setup_small_caves(path_map)
    all_paths = find_paths_pt2(path_map, 'start', 'end', small_caves)
    print(len(all_paths))


if __name__ == "__main__":
    # part1(all_lines)
    part2(all_lines)
