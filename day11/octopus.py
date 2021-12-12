filename = '/Users/alisonburgess/Documents/advent of code/2021/day11/input.txt'
oct_grid = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        cur_row = []
        for letter in row:
            cur_row.append(int(letter))
        oct_grid.append(cur_row)



def increment_adjacent_spots(oct_grid, cur_col, cur_row, already_touced):
    col_length = len(oct_grid)
    row_length = len(oct_grid[0])

    top_coord = (cur_col -1, cur_row)
    down_coord = (cur_col +1, cur_row)
    right_coord = (cur_col, cur_row +1)
    left_cord = (cur_col, cur_row-1)
    up_right_diag = (cur_col -1, cur_row +1)
    up_left_diag = (cur_col -1, cur_row -1)
    down_right_diag = (cur_col +1, cur_row +1)
    down_left_diag = (cur_col +1, cur_row -1)
    all_coords = [top_coord, down_coord, right_coord, left_cord, up_right_diag, up_left_diag, down_right_diag, down_left_diag]

    for coord in all_coords:
        if coord[0] >= 0 and coord[0] < col_length and coord[1] >= 0 and coord[1] < row_length:
            oct_grid[coord[0]][coord[1]] += 1
            if (coord[0], coord[1]) in already_touced and oct_grid[coord[0]][coord[1]] == 10:
                oct_grid = increment_adjacent_spots(oct_grid, coord[0], coord[1], already_touced)

    return oct_grid

def increment_all_oct(oct_grid, flashes):
    cur_flashes = 0
    col_length = len(oct_grid)
    row_length = len(oct_grid[0])
    already_touced = []

    for i in range(col_length):
        for j in range(row_length):
            oct_grid[i][j] += 1
            already_touced.append((i, j))

            if oct_grid[i][j] >= 10:
                oct_grid = increment_adjacent_spots(oct_grid, i, j, already_touced)
    
    for i in range(col_length):
        for j in range(row_length):
            if oct_grid[i][j] >= 10:
                oct_grid[i][j] = 0
                flashes += 1
                cur_flashes += 1

    return oct_grid, flashes, cur_flashes


def run(num_rounds, oct_grid):

    flashes = 0
    for i in range(num_rounds):
        oct_grid, flashes, cur_flashes = increment_all_oct(oct_grid, flashes)

        if cur_flashes == 100:
            print(i +1)


if __name__ == "__main__":
    run(300, oct_grid)
