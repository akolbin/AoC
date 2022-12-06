import re

crates, steps = [s.split('\n') for s in open("input.txt").read().split("\n\n")]

def parse_input():
    parsed = []
    inst = []

    for crate in crates:
        crate = crate.replace("[", "")
        crate = crate.replace("]", "")
        crate = crate.replace("    ", "  ")
        parsed.append(crate)

    for step in steps:
        step = re.findall(r'\d+', step)
        step = [int(x) for x in step]
        inst.append(step)

    parsed.pop()
    return parsed, inst

def assemble(crates=list):
    assembled = []
    for i in range(9):
        assembled.append([])
    for row in crates:
        for i in range(9):
            crate = row[i*2]
            if crate != " ":
                assembled[i].append(crate)
    return assembled

def move(assembled=list, inst=list):
    for step in inst:
        for i in range(step[0]):
            moved = assembled[step[1]-1].pop(0)
            assembled[step[2]-1].insert(0, moved)
    return assembled
    

test, inst = parse_input()
assembled = assemble(test)
x = move(assembled, inst)
for idk in x:
    print(idk[0], end ="")


