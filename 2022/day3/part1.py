def parse_input(file_name: str="input.txt"):
    
    parsed = []
    f = open(file_name, 'r')
    lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        num_items = len(line)
        compart_one = slice(0,(num_items//2))
        compart_two = slice((num_items//2),num_items)
        
        comparts = []
        comparts.append(line[compart_one])
        comparts.append(line[compart_two])
        parsed.append(comparts)

    return parsed

def is_member(compart = list, char = str):

    for i in range(0, len(compart)):
        if char == compart[i]:
            return compart[i]
    return False

def find_match(compart_one = list, compart_two = list):

    for char in compart_one:
        if is_member(compart_two, char):
            return char
    return False

def alpha_values():
    values = {}
    start = 'a'
    half = 'A'
    for i in range (0,26):
        values[start] = i + 1
        start = chr(ord(start)+1)
    for i in range (0,26):
        values[half] = i + 27
        half = chr(ord(half)+1)
    return values

comparts = parse_input()
total_prio = 0
values = alpha_values()
for compartments in comparts:
    match = find_match(compartments[0], compartments[1])
    total_prio += values[match]

print(total_prio)
