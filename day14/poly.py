import numpy as np
filename = '/Users/alisonburgess/Documents/advent of code/2021/day14/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)


def part1(all_lines, num_iterations):
    polymer_template = all_lines.pop(0)
    all_lines.pop(0) # remove blank space

    # create a dictionary of 'NN': 'C"
    pairs = {}
    for line in all_lines:
        split_line = line.split(" -> ")
        pairs[split_line[0]] = split_line[1]
    
    # get a list of all the combos from the polymer_template
    # this could change per round
    for i in range(num_iterations):
        needed_keys = []
        template_size = len(polymer_template)
        for j in range(template_size):
            if j+1 < template_size:
                first_letter = polymer_template[j]
                second_letter = polymer_template[j+1]
                letter_pair = first_letter + second_letter
                needed_keys.append(letter_pair)
        
        new_polymer_template = ''
        for k in range(len(polymer_template)):
            if k+1 < template_size:
                first_letter = polymer_template[k]
                second_letter = polymer_template[k+1]
                letter_pair = first_letter + second_letter
    
                if letter_pair in pairs:
                    inserted_letter = pairs.get(letter_pair)
                    new_polymer_template += first_letter + inserted_letter
                else:
                    new_polymer_template += first_letter + second_letter
            else:
                new_polymer_template += polymer_template[k]
        
        polymer_template = new_polymer_template
    
    # count the occurances of each unique letter
    unique_chars = list(set(polymer_template))
    num_occurances = {}
    for char in unique_chars:
        num_char = polymer_template.count(char)
        num_occurances[char] = num_char
    
    max_occurance = num_occurances.get(max(num_occurances, key=num_occurances.get))
    min_occurance = num_occurances.get(min(num_occurances, key=num_occurances.get))
    print(max_occurance - min_occurance)

from collections import defaultdict
def part2(all_lines, num_iterations):
    polymer_template = all_lines.pop(0)
    all_lines.pop(0) # remove blank space

    pairs = {}
    for line in all_lines:
        split_line = line.split(" -> ")
        pairs[split_line[0]] = split_line[1]
    
    current_pairs = defaultdict(int) 
    element_count = defaultdict(int) 
    # initalize the fictionary of pairs
    for i in range(len(polymer_template) - 1):
        cur_pair = polymer_template[i] + polymer_template[i+1]
        current_pairs[cur_pair] += 1
        element_count[polymer_template[i]] += 1
    
    # you need to count the final element
    element_count[polymer_template[-1]] += 1

    for i in range(num_iterations):
        new_pairs = defaultdict(int)
        for cur_pair in current_pairs:
            new_element = pairs[cur_pair]

            # create new pairs for the inseration rules AB -> C changes AB into 2 new paris AC and CB
            pair1 = cur_pair[0] + new_element
            pair2 = new_element + cur_pair[1]

            # add 2 new pairs to the new pairs dict += the count in the old pairs
            new_pairs[pair1] += current_pairs[cur_pair]
            new_pairs[pair2] += current_pairs[cur_pair]

            # the quanity of the new emelemnt is the same as the amount of its key used in the string
            element_count[new_element] += current_pairs[cur_pair]
        current_pairs = new_pairs

    print(max(element_count.values()) - min(element_count.values()))

if __name__ == "__main__":
    # part1(all_lines, 10) #part1
    part2(all_lines, 40) #part2
