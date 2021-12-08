filename = '/Users/alisonburgess/Documents/advent of code/2021/day6/test_input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)


all_values = all_lines[0].split(',')
all_nums = []
for val in all_values:
    all_nums.append(int(val))

def slow_way(all_nums):
    num_days = 0
    while(num_days != 16):
        for i in range(len(all_nums)):
            cur_val = all_nums[i]
            
            if cur_val != 0:
                cur_val -= 1
            else:
                cur_val = 6
                all_nums.append(8)
            all_nums[i] = cur_val

        num_days += 1
    print(sum(all_nums))

def life_cycle(days):
    birth = days.pop(0) # fish giving birth
    days[6] += birth # add newly-given-birth fish back to 6
    days.append(birth) # amount of fish that haven given brirth = new fish added at 8

def faster_way(all_nums):
    for day in all_nums:
        days[day] += 1
    
    for _ in range(18):
        life_cycle(days)
    
    print(sum(days))

if __name__ == "__main__":
    faster_way(all_nums)
