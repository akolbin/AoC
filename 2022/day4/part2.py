def parse_input(file_name: str="input.txt"):
    
    parsed = []
    f = open(file_name, 'r')
    lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        line = line.replace("-", " ")
        line = line.replace(",", " ")
        line = line.split(" ")
        parsed.append(line)

    return parsed


def answer(pairs = list):

    total_overlap = 0
    for pair in pairs:

        if int(pair[0]) <= int(pair[2]) and int(pair[1]) >= int(pair[2]):
            total_overlap += 1
        else:
            if int(pair[2]) <= int(pair[0]) and int(pair[3]) >= int(pair[0]):
                total_overlap += 1
    return total_overlap

pairs = parse_input()
print(answer(pairs))