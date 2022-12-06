def parse_input(file_name: str="input.txt"):
    
    grouped = []
    parsed = []
    f = open(file_name, 'r')
    lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        grouped.append(line)
        if len(grouped) == 3:
            parsed.append(grouped)
            grouped = []

    return parsed

def is_member(compart = list, char = str):

    for i in range(0, len(compart)):
        if char == compart[i]:
            return compart[i]
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
print(comparts)
total_prio = 0
values = alpha_values()
for compartments in comparts:
    common = set.intersection(*map(set, compartments))
    badge = (list(common)[0])
    print(badge)
    total_prio += values[badge]

print(total_prio)

