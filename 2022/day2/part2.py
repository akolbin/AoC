shapes = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

choices1 = ["A", "B", "C"]
choices2 = ["X", "Y", "Z"]


def parse_input(file_name: str="input.txt"):
    
    with open(file_name, "r") as f:
        outcomes = f.read().replace(" ", "").split("\n")
    
    return outcomes

def get_score(round: str):
    my_points = 0
    if round[1] == "X": # Lose
        my_move = choices2[(choices1.index(round[0]) - 1) % 3]
        my_points = shapes[my_move]
    if round[1] == "Y": # Draw
        my_move = choices2[choices1.index(round[0])]
        my_points = 3 + shapes[my_move]
    if round[1] == "Z": # Win
        my_move = choices2[(choices1.index(round[0]) + 1) % 3]
        my_points = 6 + shapes[my_move]
    return my_points

outcomes = parse_input()
total_score = 0
for outcome in outcomes:
    total_score += get_score(outcome)

print(total_score)