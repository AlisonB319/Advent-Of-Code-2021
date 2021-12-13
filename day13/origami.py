import numpy as np
filename = '/Users/alisonburgess/Documents/advent of code/2021/day13/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)

coords = []
fold_instr = []
for line in all_lines:
    if line == '':
        continue
    if 'fold' in line:
        all_words = line.split(' ')
        flip_on = all_words[-1]
        info = flip_on.split("=")
        fold_instr.append((info[0], info[1]))
    else:
        both_coords = line.split(',')
        coords.append((int(both_coords[0]), int(both_coords[1])))


def make_map(coords):
    max_y = max(coords, key=lambda item:item[0])[0] + 1
    max_x = max(coords, key=lambda item:item[1])[1] + 1

    full_map = []
    for i in range(max_x):
        new_row = []
        for j in range(max_y):
            new_row.append(".")
        full_map.append(new_row)

    # populate the grid
    for coord in coords:
        y = coord[0]
        x = coord[1]
        full_map[x][y] = "#"

    return full_map

def fold(full_map, fold_instr, max_x, max_y):

    coords = []
    for i in range(max_x): 
        for j in range(max_y):
            if full_map[i][j] == '#':
                coords.append((j, i))

    new_map = []
    fold_along = int(fold_instr[1])
    if fold_instr[0] == 'y':
        for coord in coords:
            x = int(coord[0])  
            y = int(coord[1]) 

            if y > fold_along:
                spaces_up = fold_along - (y - fold_along)
                full_map[spaces_up][x] = '#'
        
        for i in range(len(full_map)):
            if i < fold_along:
                new_map.append(full_map[i])
            else:
                break

    elif fold_instr[0] == 'x':
        for coord in coords:
            x = int(coord[0])  # 0
            y = int(coord[1])  # 14

            if x > fold_along:
                spaces_left = fold_along - (x - fold_along)
                full_map[y][spaces_left] = '#'

        y_range = max_y-fold_along + 1
        for j in range(max_x):
            new_row = []
            for i in range(y_range):
                if i < fold_along:
                    new_row.append(full_map[j][i])
                else:
                    break
            new_map.append(new_row)
        
    return new_map, len(new_map), len(new_map[0])


def count_folds(full_map):
    total = 0
    for x in range(len(full_map[0])):
        for y in range(len(full_map)):
            if full_map[y][x] == '#':
                total += 1
    return total


def run(coords, fold_instrs):
    total = 0
    full_map = make_map(coords)
    max_y = max(coords, key=lambda item:item[0])[0] + 1
    max_x = max(coords, key=lambda item:item[1])[1] + 1
    for fold_ins in fold_instrs:
        full_map, max_x, max_y = fold(full_map, fold_ins, max_x, max_y)
        '''
        part1
        #total = count_folds(full_map)
        #print(total)
        #import pdb; pdb.set_trace() # stops after the first fold
        '''

    for x in range(len(full_map)):
        print(full_map[x])  # open terminal wide to see the letters printed out


if __name__ == "__main__":
    run(coords, fold_instr)
