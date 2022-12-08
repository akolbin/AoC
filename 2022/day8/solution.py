def parse_input(file_name: str="input.txt"):
    by_row = []
    f = open(file_name, 'r')
    lines = f.readlines()
    
    for line in lines:
        by_row.append(list(map(int, line.strip())))
    # Rotate rows to represent columns
    by_col = list(zip(*by_row))

    return by_row, by_col

def scores(cur, lst):
    score = 0

    for height in lst:
        score += 1
        if height >= cur:
            return score

    return score

def get_score(cur, left, right, above, below):
    score = scores(cur, left) * scores(cur, right) * scores(cur, above) * scores(cur, below)

    return score

def find_vis(grid_rows: list, grid_cols: list):
    total_vis = len(grid_rows)*2 + (len(grid_rows)-2)*2
    highest_score = 0
    for row in range(1, len(grid_rows)-1):

        for idx in range(1, len(grid_rows[row])-1):

            cur = grid_rows[row][idx] # Current tree's height
            left = list(reversed(grid_rows[row][:idx])) # List of heights to the left
            right = grid_rows[row][idx+1:] # List of heights to the right
            above = list(reversed(list(list(grid_cols)[idx][:row]))) # List of heights above
            below = list(grid_cols)[idx][row+1:] # List of heights below

            if cur > max(left) or cur > max(right) or cur > max(above) or cur > max(below): # For part1
                total_vis +=1

            score = get_score(cur, left, right, above, below) # Get part2 scenic score
            highest_score = max(highest_score, score)

    return total_vis, highest_score

grid_rows, grid_cols = parse_input()
print(find_vis(grid_rows, grid_cols))