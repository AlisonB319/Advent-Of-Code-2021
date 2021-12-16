import numpy as np
filename = '/Users/alisonburgess/Documents/advent of code/2021/day15/input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)


def get_matrix(all_lines):
    matrix = []
    for line in all_lines:
        new_row = []
        for num in line:
            new_row.append(int(num))
        matrix.append(new_row)
    return matrix


def part1(cost):
    (M, N) = (len(cost), len(cost[0]))

    tc = [[0 for x in range(N)] for y in range(M)]

    for i in range(M):
        for j in range(M):
            tc[i][j] = cost[i][j]

            # fill the first row. only one direction 
            if i == 0 and j > 0:
                tc[0][j] += tc[0][j-1]
            
            # fill the first col only one idirection
            elif j == 0 and i > 0:
                tc[i][0] += tc[i-1][0]

            # fill the rest
            elif i > 0 and j > 0:
                tc[i][j] += min(tc[i-1][j], tc[i][j-1])

    return tc[M-1][N-1] - tc[0][0] # starting pos is not counted
    
import heapq
def expand_matrix(cost):  # generate the full map

    (M, N) = (len(cost), len(cost[0]))

    counter = 1
    while (counter < 5):
        new_cost = []
        for i in range(M):
            cur_row = cost[i]
            new_row = []
            for j in range(N):
                new_num = cost[i][j] + counter
                if new_num > 9:
                    new_num = new_num - 9
                cur_row.append(new_num)

            new_cost.append(cur_row)
        cost = new_cost
        counter += 1
    
    (M, N) = (len(cost), len(cost[0]))
    counter = 1
    while (counter < 5):
        new_rows = []
        for i in range(M):
            new_row = []
            for j in range(N):
                new_num = cost[i][j] + counter
                if new_num > 9:
                    new_num = new_num - 9
                new_row.append(new_num)
            new_rows.append(new_row)

        for row in new_rows:
            cost.append(row)
        counter += 1

    return cost
    

def get_neighbors(node, graph):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    results = []
    for direction in directions:
        neighbor = (node[0] + direction[0],node[1] + direction[1])
        if neighbor in graph:
            results.append(neighbor)
    return results

def find_loweset_risk(graph, begin, end):
    frontier = []
    heapq.heappush(frontier, (0, begin))
    risk_so_far = dict()
    risk_so_far[begin] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]
        if current == end:
            break
        for neighbor in get_neighbors(current, graph):
            new_risk = risk_so_far[current] + graph[neighbor]
            if neighbor not in risk_so_far or new_risk < risk_so_far[neighbor]:
                risk_so_far[neighbor] = new_risk
                priority = new_risk
                heapq.heappush(frontier, (priority, neighbor))
    return risk_so_far[end]




if __name__ == "__main__":
    matrix = get_matrix(all_lines)
    # tc = part1(matrix)

    new_matrix = expand_matrix(matrix) # wrote myself

    '''
    had to look up how to make a priority queue and how to create
    the dict that would work in the solution
    '''
    filename = '/Users/alisonburgess/Documents/advent of code/2021/day15/cop_out.txt'
    with open(filename, 'w') as txtfile:
        for row in new_matrix:
            cur_string = ''
            for num in row:
                cur_string += str(num)
            txtfile.write(cur_string + '\n') 

    with open(filename,'r') as infile:
        graph = {(x,y):int(cost) for y,line in enumerate(infile.readlines(),1) for x,cost in enumerate(line.strip(),1)}

    begin = (1,1)
    end = (max(x for x,y in graph.keys()),max(y for x,y in graph.keys()))
    lowest_risk = find_loweset_risk(graph, begin, end)
    print(lowest_risk)

