filename = '/Users/alisonburgess/Documents/advent of code/2021/day2/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        all_lines.append(row)

horiz = 0
depth = 0
aim = 0
for full_data in all_lines:
    data = full_data.split(' ')
    instruction = data[0]
    num = int(data[1])

    if instruction == 'forward':
        horiz += num
        depth += aim * num 
    elif instruction == 'down':
        #depth += num # part 1
        aim += num # part 2
    elif instruction == 'up':
        #depth -= num # part 1
        aim -= num # part 2
    else:
        print("unknown string")

total = horiz * depth
print(total)

    
