# Check if a string has unique characters
def is_unique(substr: str):
    if len(substr) != len(set(substr)):
        return False
    return True

# Iterate through input string, plugging substrings into above function
def find_marker(buf: str, num_distinct: int):
    found = False
    cur = 0
    while(not found):
        substr = buf[cur:cur+num_distinct]
        if is_unique(substr):
            found = True
            print(substr)
            print(cur+num_distinct)
        cur += 1

input = open("input.txt", "r").read()
find_marker(input, 4)
find_marker(input, 14)