filename = '/Users/alisonburgess/Documents/advent of code/2021/day10/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)


def find_corrupted_chunk(line):
    pairs = {')':'(', ']':'[', '}':'{', '>':'<'}

    open_pieces = ['(', '[', '{', '<']
    closed_pieces = [')', ']', '}', '>']
    already_opened = []

    for char in line:
        if char in open_pieces:
            already_opened.append(char)
        elif char in closed_pieces:
            if already_opened[-1] != pairs.get(char):
                return char
            else:
                already_opened.pop()

def fix_incomplete_line(line):
    pairs = {')':'(', ']':'[', '}':'{', '>':'<'}

    open_pieces = ['(', '[', '{', '<']
    closed_pieces = [')', ']', '}', '>']
    already_opened = []

    corrupted = False
    for char in line:
        if char in open_pieces:
            already_opened.append(char)
        elif char in closed_pieces:
            if already_opened[-1] != pairs.get(char):
                corrupted = True
            else:
                already_opened.pop()
        
        if corrupted:
            return None
    
    if not corrupted:
        return already_opened

    
def calculate_score_pt1(all_chunks):
    total = 0
    mapp = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for chunk in all_chunks:
        score = mapp.get(chunk)
        total += score
    print(total)


def calculate_score_pt2(chunks_list):
    mapp = {'(': 1, '[': 2, '{': 3, '<': 4}
    all_scores = []

    for needs_closing in chunks_list:
        total = 0
        needs_closing.reverse()
        for chunk in needs_closing:
            total *= 5
            score = mapp.get(chunk)
            total += score
        all_scores.append(total)

    all_scores.sort()
    middle_index = (len(all_scores) - 1) / 2
    print(all_scores[middle_index])

    
def part1():
    corrupted_chunks = []
    for line in all_lines:
        c_chunk = find_corrupted_chunk(line)
        if c_chunk:
            corrupted_chunks.append(c_chunk)
    calculate_score_pt1(corrupted_chunks)

def part2():
    needs_fixing = []
    for line in all_lines:
        needed_closing = fix_incomplete_line(line)
        if needed_closing:
            needs_fixing.append(needed_closing)

    calculate_score_pt2(needs_fixing)

if __name__ == "__main__":
    # part1()
    part2()

               
