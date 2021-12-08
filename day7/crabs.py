filename = '/Users/alisonburgess/Documents/advent of code/2021/day7/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)

all_pos_str = all_lines[0].split(',')
all_pos = []
for pos in all_pos_str:
    all_pos.append(int(pos))

def find_cheapest_move_pt1():
    cost_to_move_to_index = {}
    for pos in all_pos:
        cost_to_move_to_index[pos] = 0

    for cur_val in all_pos:
        total_cost = 0
        for check_val in all_pos:
            cost_to_move = abs(check_val - cur_val)
            total_cost += cost_to_move
        cost_to_move_to_index[cur_val] = total_cost

    least_cost = 1000000
    cur_val = -1
    for target, total_cost in cost_to_move_to_index.iteritems():
        if total_cost < least_cost:
            least_cost = total_cost
            cur_val = target
    
    print(cur_val, least_cost)

def find_cheapest_move_pt2():
    cost_to_move_to_index = {} 
    for i in range(len(all_pos)):
        cost_to_move_to_index[i] = 0

    for cur_val in all_pos: # [16,1,2,0,4,2,7,1,2,14]
        cur_cost = 0
        total_cost = 0
        for i in range(len(all_pos)):
            val_to_move = abs(i - cur_val) 
            cost_to_move = ((val_to_move*val_to_move)+val_to_move) / 2  # (n2 + n) / 2 
            cur_cost = cost_to_move_to_index[i]
            cost_to_move_to_index[i] = cur_cost + cost_to_move

    least_cost = 1000000000000000000
    cur_val = -1
    for target, total_cost in cost_to_move_to_index.iteritems():
        if total_cost < least_cost:
            least_cost = total_cost
            cur_val = target
    
    print(cur_val, least_cost)


if __name__ == "__main__":
    find_cheapest_move_pt1()
    find_cheapest_move_pt2()
