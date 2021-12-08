filename = '/Users/alisonburgess/Documents/advent of code/2021/day5/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)


coordinates = []
all_x_cords = []
all_y_cords = []
for line in all_lines:
    split = line.split(",")
    x1 = int(split[0])
    y2 = int(split[2])

    split_2 = split[1].split(" ")
    y1 = int(split_2[0])
    x2 = int(split_2[2]) 

    coord1 = (x1, y1)
    coord2 = (x2, y2)
    coordinates.append((coord1, coord2))
    all_x_cords.append(x1)
    all_x_cords.append(x2)
    all_y_cords.append(y1)
    all_y_cords.append(y2)


max_y = max(all_y_cords) + 2
max_x = max(all_x_cords) + 2

grid = []
for i in range(max_x):
    grid.append([])
    for j in range(max_y):
        grid[i].append(0)

for coord in coordinates:
    starting_cord = coord[0]
    ending_cord = coord[1]

    all_found = False
    x1 = starting_cord[0]
    y1 = starting_cord[1]
    x2 = ending_cord[0]
    y2 = ending_cord[1]
    starting_x = 0
    starting_y = 0
    end_x = 0
    end_y = 0
    if x1 == x2:
        if y1 < y2:
            starting_y = y1
            end_y = y2
        else:
            starting_y = y2
            end_y  = y1

        for i in range(starting_y, end_y+1):
            val = grid[i][x1]
            grid[i][x1] = val + 1

    elif y2 == y1:
        if x1 < x2:
            starting_x = x1
            end_x = x2
        else:
            starting_x = x2
            end_x  = x1
    
        for i in range(starting_x, end_x+1):
            try:
                val = grid[y1][i]
                grid[y1][i] = val + 1
            except Exception:
                import pdb; pdb.set_trace()
                c = 1010101

    else:
        
        # find the highest point = lowest x highest y
        # 8,0 -> 0,8
        # 0,0 -> 8,8
        # 6,4 -> 2,0 
        # 5,5 -> 8,2
        if y1 < y2:
            highest_pair = (x1, y1)
            lowest_pair = (x2, y2)
        else:
            highest_pair = (x2, y2)
            lowest_pair = (x1, y1)

        '''
        8,0 -> 0,8 move left
        2,0 -> 6,4
        '''

        if highest_pair[0] > lowest_pair[0]:  # move left
            num_move = highest_pair[0] - lowest_pair[0]
            counter_x = highest_pair[0] # 8
            counter_y = highest_pair[1] # 0
            for i in range(num_move +1):
                val = grid[counter_y][counter_x]
                grid[counter_y][counter_x] = val + 1
                counter_x -= 1
                counter_y += 1
        elif highest_pair[1] < lowest_pair[1]: # move right
            num_move = lowest_pair[0] - highest_pair[0]
            counter_x = highest_pair[0] # 2
            counter_y = highest_pair[1] # 0
            for i in range(num_move +1):
                val = grid[counter_y][counter_x]
                grid[counter_y][counter_x] = val + 1
                counter_x += 1
                counter_y += 1
        else:
            print("we have a problem???")

counter = 0
for i_c in range(max_x):
    for j_c in range(max_y):
        if grid[i_c][j_c] >= 2:
            counter += 1


print(counter)
