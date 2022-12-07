# Need to debug this

dirs = {
    "/": {
        "size": 0,
        "parent": "none"
    }
}

def parse_input(file_name: str="input.txt"):
    
    parsed = []
    f = open(file_name, 'r')
    lines = f.readlines()
    
    for line in lines:
       parsed.append(line.strip())
    return parsed

def get_sizes(commands: list):
    cur_dir = "/"
    for command in commands:
        # If we have a "cd"
        if command[0:4] == "$ cd":
            arg = command.replace("$ cd ", "")
            # If it's "cd ..", update current dir
            if arg == "..":
                if dirs[cur_dir]["parent"] != "none":
                    cur_dir = dirs[cur_dir]["parent"]
            # If we are going deeper
            else:
                prev = cur_dir
                cur_dir = command.replace("$ cd ", "")
                # Create a new dir and add it set its parent
                if not cur_dir in dirs:
                    dirs[cur_dir] = {
                        "size": 0,
                        "parent": ""
                    }
                    dirs[cur_dir]["parent"] = prev
        # If it's not a "cd" and it's a file size
        else:
            if command[0].isdigit():
                val = int(command.split(" ")[0])
                dirs[cur_dir]["size"] += val
                parent = dirs[cur_dir]["parent"]
                while parent != "none":
                    dirs[parent]["size"] += val
                    parent = dirs[parent]["parent"]
    return dirs

def solve(sizes: dict):
    total = 0
    for info in sizes.values():
        if info["size"] <= 100000:
            total += info["size"]
    print(total)



commands = parse_input()
sizes = get_sizes(commands)
solve(sizes)