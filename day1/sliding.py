# part 2
filename = '/Users/alisonburgess/Documents/advent of code/2021/day1/input2.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        num = int(row)
        all_lines.append(num)

cur_sum = all_lines[0] + all_lines[1] + all_lines[2] # letter A

counter = 0
total_lines = len(all_lines)
for i in range(total_lines):
    if i + 3 > total_lines:
        break
    num1 = all_lines[i]
    num2 = all_lines[i+1]
    num3 = all_lines[i+2]
    total = num1 + num2 + num3

    if total > cur_sum:
        counter += 1
    
    cur_sum = total

print(counter)
