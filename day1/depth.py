# part 1
filename = '/Users/alisonburgess/Documents/advent of code/2021/day1/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        num = int(row)
        all_lines.append(num)


counter = 0
cur_line = all_lines[0]
for line in all_lines:
    if line > cur_line:
        counter +=1
    cur_line = line

print(counter)
