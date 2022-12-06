shapes = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

points = [3, 6, 0]
choices = ["A", "B", "C", "X", "Y", "Z"]

def parse_input(file_name: str="input.txt"):
    
    with open(file_name, "r") as f:
        outcomes = f.read().replace(" ", "").split("\n")
    
    return outcomes

def get_points(round: str):
    result = choices.index(round[1]) - choices.index(round[0])
    my_points = points[result % 3] + shapes[round[1]]
    return my_points

outcomes = parse_input()
total_score = 0

for outcome in outcomes:
    total_score += get_points(outcome)
    
print(total_score)
