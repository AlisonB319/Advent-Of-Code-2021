filename = '/Users/alisonburgess/Documents/advent of code/2021/day9/input.txt'
heightmap = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        heightmap.append(row)

def coords_of_lowpoints(heightmap):
    lowest_nums = []
    col_length = len(heightmap) 
    row_length = len(heightmap[0]) 
    # total = 0 part 1
    low_point_coords = []


    for col in range(col_length):
        for row in range(row_length):
            directions = [1000000000] * 4 # up down left right

            if col - 1 >= 0:  # up 
                directions[0] = int(heightmap[col-1][row])
            if col + 1 < col_length:  # down
                directions[1] = int(heightmap[col+1][row])
            if row + 1 < row_length:  #right
                directions[2] = int(heightmap[col][row+1])
            if row - 1 >= 0:  # left
                directions[3] = int(heightmap[col][row-1])
        
            cur_num = int(heightmap[col][row])

            if cur_num < min(directions):
                # total += cur_num + 1 # part1
                low_point_coords.append((col, row))
    
    return low_point_coords
    #print(total)

num_occur = 0

def is_stopped_by_nine(col, row, int_map, found_points):
    # print("col {0} row {1}".format(col, row))
    col_length = len(heightmap) 
    row_length = len(heightmap[0])

    if col >= 0 and row >= 0 and row < row_length and col < col_length:
        if int_map[col][row] != 9:
            if (col, row) not in found_points:
                found_points.append((col, row))

            int_map[col][row] = 9 # fill what I just looked at so recu can end
            is_stopped_by_nine(col, row + 1, int_map, found_points) # right
            is_stopped_by_nine(col, row - 1, int_map, found_points) # left
            is_stopped_by_nine(col + 1, row, int_map, found_points) # down
            is_stopped_by_nine(col -1, row, int_map, found_points) # up

    return found_points
        

def part2():
    all_low_points = coords_of_lowpoints(heightmap)
    col_length = len(heightmap) 
    row_length = len(heightmap[0]) 
    all_sizes = []

    for point in all_low_points:
        int_map = []
        for col in range(col_length):
            int_row = []
            for row in range(row_length):
                int_row.append(int(heightmap[col][row]))
            int_map.append(int_row)
        
        found_points = []

        check = is_stopped_by_nine(point[0], point[1], int_map, found_points)
        all_sizes.append(len(check))
    
    all_sizes.sort()
    print(all_sizes[-1] * all_sizes[-2] * all_sizes[-3])
        

if __name__ == "__main__":
    # part1(heightmap)
    part2()
    
