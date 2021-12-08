filename = '/Users/alisonburgess/Documents/advent of code/2021/day8/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)

split_input = []
for line in all_lines:
    split = line.split("|")
    split_input.append(split[1])

def part1():
    # 1, 4, 7, 8
    acceptable_lengths = [2, 3, 4, 7]
    counter = 0
    for split in split_input:
        all_strings = split.split(" ")
        all_strings.pop(0) # remove a space at index 0
        for string in all_strings:
            if len(string) in acceptable_lengths:
                counter += 1
    print(counter)

def part2():    
    totals = []
    decoder_nums = []
    nums_to_decode = []
    for line in all_lines:
        split = line.split("|")
        decoder_nums.append(split[0])
        nums_to_decode.append(split[1])

    # create a dict with key: len(word) value: list(word)
    # {2: ['ab'], 3: ['dab'], 4: ['eafb'], 5: ['cdfbe', 'gcdfa', 'fbcad'], 
    #  6: ['cefabd', 'cdfgeb', 'cagedb'], 7: ['acedgfb']}
    counter = 0
    full_decoder_msg = []
    for full_decode_str in decoder_nums:
        str_sizes = {}
        decode_str_list = full_decode_str.split(" ")
        for num in decode_str_list:
            if len(num) <= 0:
                continue
            elif len(num) not in str_sizes:  # key is not yet in dict
                str_sizes[len(num)] = [num]
            else:
                num_list = str_sizes[len(num)]
                num_list.append(num)
                str_sizes[len(num)] = num_list
        full_decoder_msg.append(str_sizes)
    
    for decoder_dict in full_decoder_msg:
        clock_pos = [''] * 7
        position_dict = 0
        # top letter = clock_pos[0] will be in num7 len(3) but not in num1 len(2)
        clock_pos[0] = [letter for letter in decoder_dict[3][0] if letter not in decoder_dict[2][0]][0]

        # get num occurances of every letter in the words
        num_occurances = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        for length, decoder_str_list in decoder_dict.iteritems():
            for small in decoder_str_list:
                for letter in small:
                    num = num_occurances[letter]
                    num_occurances[letter] = num + 1
  
        # back left will be a letter that is only in the words 4 times back right 6 times
        # back left = clock_pos[4]
        # top left = clock_pos[5]
        for letter, length in num_occurances.iteritems():
            if length == 4:
                clock_pos[4] = letter
            if length == 6:
                clock_pos[5] = letter

        # middle has top right, bottom right, top left
        # it wont have anything in len(2) or clock_pos[5]
        # middle = clock_pos[6]
        clock_pos[6] = [letter for letter in decoder_dict[4][0] if (letter not in decoder_dict[2][0]) 
                                                                    and letter != clock_pos[5]][0]

        # bottom has top, top left, bottom left, not in len(2) WONT HAVE middle
        # bottom = clock_pos[3]
        needed_letters = []
        needed_letters.append(clock_pos[0]) #top
        needed_letters.append(clock_pos[4]) # bl
        needed_letters.append(clock_pos[5]) #tl
        needed_letters.append(decoder_dict[2][0][0])
        needed_letters.append(decoder_dict[2][0][1])
        has_bottom = ''
        for decod_str in decoder_dict[6]:
            if ((clock_pos[0] in decod_str) and (clock_pos[4] in decod_str) and 
                (decoder_dict[2][0][0] in decod_str) and (decoder_dict[2][0][1] in decod_str) and 
                (clock_pos[6] not in decod_str)):
                has_bottom = decod_str
        clock_pos[3] = [letter for letter in has_bottom if letter not in needed_letters][0]

        # bottom_right getting it from clock 2
        # it has top, tr, bottom, bl, mid
        # will have only one letter from Num1 len(2)
        needed_letters = []
        needed_letters.append(clock_pos[0]) # top
        needed_letters.append(clock_pos[6]) # mid
        needed_letters.append(clock_pos[4]) # bl
        needed_letters.append(clock_pos[3]) # bottom
        br_string = ''
        for decod_str in decoder_dict[5]:
            match = True
            for letter in needed_letters:
                if letter in decod_str and match:
                    br_string = decod_str
                else:
                    match = False
                    br_string = ''
            if match:
                break
        clock_pos[1] = [letter for letter in br_string if letter in decoder_dict[2][0]][0]

        # bottom right will be the letter that is in num1 len(2) but is not clock_pos[1]
        clock_pos[2] = [letter for letter in decoder_dict[2][0] if letter is not clock_pos[1]][0]
        
        zero = [clock_pos[0], clock_pos[1], clock_pos[2], clock_pos[3], clock_pos[4], clock_pos[5]]
        one = [clock_pos[1], clock_pos[2]]
        two = [clock_pos[0], clock_pos[1], clock_pos[3], clock_pos[4], clock_pos[6]]
        three = [clock_pos[0], clock_pos[1], clock_pos[2], clock_pos[3], clock_pos[6]]
        four = [clock_pos[1], clock_pos[2], clock_pos[5], clock_pos[6]]
        five = [clock_pos[0], clock_pos[2], clock_pos[3], clock_pos[5], clock_pos[6]]
        six = [clock_pos[0], clock_pos[2], clock_pos[3], clock_pos[4], clock_pos[5], clock_pos[6]]
        seven = [clock_pos[0], clock_pos[1], clock_pos[2]]
        eight = [clock_pos[0], clock_pos[1], clock_pos[2], clock_pos[3], clock_pos[4], clock_pos[5], clock_pos[6]]
        nine = [clock_pos[0], clock_pos[1], clock_pos[2], clock_pos[3], clock_pos[5], clock_pos[6]]

        mapped_clock = {0:zero, 1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine}

        # strings that need decoding from input
        nums_decode = nums_to_decode[counter] # ' cdfeb fcadb cdfeb cdbaf'
        nums_list = nums_decode.split(" ")
        nums_list.pop(0) # get right of empty list

        # figure out which number each word corresponds to
        str_num = ''
        for num in nums_list:
            for real_number, required_letters in mapped_clock.iteritems():
                if len(num) == len(required_letters):
                    not_a_match = [letter for letter in num if letter not in required_letters]

                    if len(not_a_match) == 0:
                        str_num += str(real_number)
        totals.append(str_num)

        counter += 1

    total = 0
    for num in totals:
        total += int(num)
    print(total)


if __name__ == "__main__":
    # part1()
    part2()
