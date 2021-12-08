filename = '/Users/alisonburgess/Documents/advent of code/2021/day4/input.txt'
all_lines = []

choosen_nums = []
first_row = True
all_grids = []
cur_grid = []
cur_matrix = []
counter = 0
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        if first_row:
            all_choosen_nums = row.split(',')
            for num in all_choosen_nums:
                choosen_nums.append(int(num))
            first_row = False
        else:
            if row != '':
                grid_nums_with_blank = row.split(" ")
                grid_nums = [x for x in grid_nums_with_blank if x]
                for num in grid_nums:
                    tupe = (int(num), False)
                    cur_grid.append(tupe)
                cur_matrix.append(cur_grid)
                cur_grid = []
                counter += 1

        if counter == 5:
            all_grids.append(cur_matrix)
            cur_matrix = []
            counter = 0

def find_winning_bingo_grid(all_grids, choosen_nums):

    bingo = False
    while not bingo:
        cur_nums = []
        cur_nums.append(choosen_nums.pop(0))
        
        # set true if part of cur_nums
        for grid in all_grids:
            for i in range(5):
                for j in range(5):
                    cur_tupe = grid[i][j]
                    if cur_tupe[0] in cur_nums:
                        new_tupe = (cur_tupe[0], True)
                        grid[i][j] = new_tupe
        
        # figure out if a bingo has been made
        bingo_streak_row = 0
        bingo_streak_col = 0
        for grid in all_grids:
            for i in range(5):
                for j in range(5):
                    cur_tupe = grid[i][j]
                    if cur_tupe[1] == True:
                        bingo_streak_row += 1
                
                for j in range(5):
                    cur_tupe = grid[j][i]
                    if cur_tupe[1] == True:
                        bingo_streak_col += 1

                if bingo_streak_row == 5 or bingo_streak_col == 5:
                    bingo = True
                    return grid, cur_nums
                else:
                    bingo_streak_row = 0
                    bingo_streak_col = 0

def find_last_winning_grid(all_grids, choosen_nums):

    completed_boards = {}
    for k in range(len(all_grids)):
        completed_boards[k] = False

    found_last = False
    while not found_last:
        cur_nums = []
        cur_nums.append(choosen_nums.pop(0))
        
        # set true if part of cur_nums
        for grid in all_grids:
            for i in range(5):
                for j in range(5):
                    cur_tupe = grid[i][j]
                    if cur_tupe[0] in cur_nums:
                        new_tupe = (cur_tupe[0], True)
                        grid[i][j] = new_tupe
        
        # figure out if a bingo has been made
        bingo_streak_row = 0
        bingo_streak_col = 0

        for k in range(len(all_grids)):
            for i in range(5):
                for j in range(5):
                    cur_tupe = all_grids[k][i][j]
                    if cur_tupe[1] == True:
                        bingo_streak_row += 1
                
                for j in range(5):
                    cur_tupe = all_grids[k][j][i]
                    if cur_tupe[1] == True:
                        bingo_streak_col += 1

                if bingo_streak_row == 5 or bingo_streak_col == 5:
                    if not completed_boards[k]:
                        cur_counter = 0
                        for grid_num, booli in completed_boards.iteritems():
                            if booli == True:
                                cur_counter += 1
                        
                        if cur_counter == len(all_grids) - 1:
                            # last one has been found
                            return all_grids[k], cur_nums

                        completed_boards[k] = True
                else:
                    bingo_streak_row = 0
                    bingo_streak_col = 0

def calculate_final_score(grid, last_num):
    sum_unmarked = 0
    for i in range(5):
        for j in range(5):
            cur_tupe = grid[i][j]
            if cur_tupe[1] == False:
                sum_unmarked += cur_tupe[0]

    print(last_num[0] * sum_unmarked)

if __name__ == "__main__":
   # winning_grid, last_num = find_winning_bingo_grid(all_grids, choosen_nums)
    last_winning_grid, last_num = find_last_winning_grid(all_grids, choosen_nums)  
    calculate_final_score(last_winning_grid, last_num)

