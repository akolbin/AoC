total = 0
candidates = []

class Tree:
    def __init__(self, name):
        self.children = []
        self.parent = None
        self.name = name
        self.size = 0

def parse_input(file_name: str="input.txt"):
    parsed = []
    f = open(file_name, 'r')
    lines = f.readlines()
    
    for line in lines:
       parsed.append(line.strip())
    return parsed

def create_tree(root: Tree, commands: list):
    cur_node = root
    for command in commands:
        # If changing dir
        if command[0:4] == "$ cd":
            # Retrieve dir we are going to
            arg = command.replace("$ cd ", "")
            # If going back a dir, set cur node to parent
            if arg == "..":
                cur_node = cur_node.parent
            # If going to new dir, create a new tree.
            # Append it to cur node's children and set new cur node
            else:
                child = Tree(arg)
                child.parent = cur_node
                cur_node.children.append(child)
                cur_node = child
        # If not cd, add the file size to node's size attribute
        else:
            if command[0].isdigit():
                val = int(command.split(" ")[0])
                cur_node.size += val
    return root

def part1(root):
    global total
    if root:
        # Recursively call function on all children
        for child in root.children:
             part1(child)
        if root.size <= 100000:
            total += root.size
        # Update child's parent size 
        if root.parent:
            root.parent.size += root.size

    return root, total

def part2(root):
    global needed_space
    global candidates
    if root:
        for child in root.children:
             part2(child)
        if root.size >= needed_space:
            candidates.append(root.size)

    return candidates

# Creating Tree 
parsed = parse_input()
root = Tree("/")
tree = create_tree(root, parsed)

# Part 1 
updated, total = part1(tree)
print(total)

# Part 2
used_space = 70000000 - updated.size
needed_space = 30000000 - used_space
num = part2(updated)
print(min(num))