filename = '/Users/alisonburgess/Documents/advent of code/2021/day3/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)

# find the most common number at each position, put them into one string or something, convert that into decimal
most_common_digits = ''
dict_pos_val = {}

def part1()
    for i in range(len(all_lines[0])):  # 5
        dict_pos_val[i] = (0, 0)
        for line in all_lines:
            cur_0 = dict_pos_val[i][0]
            cur_1 = dict_pos_val[i][1]
            if line[i] == "0":
                cur_0 += 1
            elif line[i] == "1":
                cur_1 +=1
            else:
                print("invalid value")
                break

            dict_pos_val[i] = (cur_0, cur_1)

    gamma_string = ''
    epsilon_string = ''
    for key, value in dict_pos_val.iteritems():
        if value[0] > value[1]:
            gamma_string += "0"
        else:
            epsilon_string += "0"
        
        if value[1] > value[0]:
            gamma_string += "1"
        else:
            epsilon_string += "1"
        

    gamma_rate = int(gamma_string, 2)
    epsilon_rate = int(epsilon_string, 2)
    power_consumption = gamma_rate * epsilon_rate

    print(power_consumption)


# part 2
def find_value(priority_num, minority_num):
    finished = False
    num_len = len(all_lines[0])  # 5

    valid_nums = []
    for num in all_lines:
        valid_nums.append(num)


    while(not finished):
        for i in range(num_len):
            dict_pos_val[i] = (0, 0)
            for line in valid_nums:
                cur_0 = dict_pos_val[i][0]
                cur_1 = dict_pos_val[i][1]
                if line[i] == "0":
                    cur_0 += 1
                elif line[i] == "1":
                    cur_1 += 1
                else:
                    break
                dict_pos_val[i] = (cur_0, cur_1)

            # see which number is the highest and pop from valid_nums if it is not the hights
            num_to_remove = ''
            tupe = dict_pos_val[i]
            if tupe[0] > tupe[1]:
                num_to_remove = minority_num
            elif tupe[1] > tupe[0]:
                num_to_remove = priority_num
            else:
                num_to_remove = priority_num

            new_valid_nums = []
            for line in valid_nums:
                if line[i] != num_to_remove:
                    new_valid_nums.append(line)
            
            valid_nums = new_valid_nums
            if len(valid_nums) == 1:
                finished = True
                return valid_nums[0]


c02_str = find_value("1", "0")
oxygen_gene_str = find_value("0", "1")
print(c02_str)
print(oxygen_gene_str)


oxy_num = int(oxygen_gene_str, 2)
c02_num = int(c02_str, 2)

print(oxy_num * c02_num)
